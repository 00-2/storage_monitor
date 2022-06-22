import google.auth.exceptions
import gspread
import requests
import psycopg2
from datetime import datetime
import logging
import tg_logger

#--------LOAD_CREDENTIALS------
import credentials
token = credentials.tg_token


#--------TG LOGGER INIT-----------
# Base logger
u_tg_logger = logging.getLogger('exec_tg')
u_tg_logger.setLevel(logging.INFO)
tg_logger.setup(u_tg_logger, token=token, users=["868052746"])




def get_dollar_quote() -> float:
    today = datetime.today().strftime("%d/%m/%y")
    try:
        listing_all_valute = requests.get(f"https://www.cbr-xml-daily.ru/daily_json.js")
    except requests.exceptions.ConnectionError:
        print("Проверьте интернет соединение")
    dollar_quote_json = listing_all_valute.json()
    try:
        return dollar_quote_json['Valute']['USD']['Value']
    except KeyError:
        print("Проверьте формат возвращаемых данных")

def is_valid_date(order_id, delivery_date):
    return datetime.strptime(delivery_date, "%d.%m.%Y") <= datetime.today()

conn = psycopg2.connect(database="storage_monitor",
                        host=credentials.host,
                        user=credentials.user,
                        password=credentials.password,
                        port="5432")

try:
    sa = gspread.service_account()
    sh = sa.open("storage_monitor_table")
    wks = sh.worksheets()
except google.auth.exceptions.TransportError:
    print("Проверьте интернет соединение")
dollar_quote = get_dollar_quote()
for sheet_ in wks:
    all_records = sheet_.get_all_records()
    for record in all_records:
        db_id, order_id, cost_US, delivery_date = record.values()
        cost_RUB = cost_US*dollar_quote
        if not is_valid_date(order_id, delivery_date):
            u_tg_logger.info(f"order {order_id} with delivery date {delivery_date} expired on { (datetime.strptime(delivery_date, '%d.%m.%Y') - datetime.today()) .days} days")
        with conn.cursor() as cursor:
            cursor.execute(
                    f"""
                    INSERT INTO orders(order_num, cost_usd, cost_rub, delivery_date)
                    VALUES ({order_id}, {cost_US}, {cost_RUB}, CAST('{delivery_date}' AS DATE) )
                    ON CONFLICT (order_num) DO UPDATE 
                    SET cost_usd = {cost_US},
                        cost_rub = {cost_RUB},
                        delivery_date =  CAST('{delivery_date}' AS DATE) ;
                    """
            )
            conn.commit()
import backend.lib as lib
import os.path
import flask
import flask_cors
import json
env = os.environ.get("APP_ENV", "dev")
print(f"Starting application in {env} mode")


class StorageMonitor(flask.Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # CORS позволит нашему фронтенду делать запросы к нашему
        # бэкенду несмотря на то, что они на разных хостах
        # (добавит заголовок Access-Control-Origin в респонсы).
        # Подтюним его когда-нибудь потом.
        flask_cors.CORS(self)


app = StorageMonitor("monitor")

app.config.from_object(f"backend.{env}_settings")



@app.route('/members')
def members():
    data = lib.rcv_data_from_bd()
    data = [ {"order_id":x[0] ,"cost_usd":x[1], "cost_rub":x[2], "delivery_date":x[3]} for x in data]
    return json.dumps({"members": data})

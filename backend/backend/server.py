
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
    return json.dumps({"members": [{"count":1,"pv":100 },{"count":2,"pv":200 },{"count":3,"pv":300 }]})

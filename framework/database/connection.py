import json
import pyodbc


class Connection:
    __instance = None

    def __init__(self):
        if Connection.__instance is not None:
            self.conn = Connection.__instance
        else:
            file = open("connection_config.json")
            json_data = json.load(file)
            conn_str = 'DRIVER={' + json_data["driver"] + '}; \
                                SERVER=' + json_data["server"] + '; \
                                DATABASE=' + json_data["db"] + '; \
                                UID=' + json_data["user"] + '; \
                                PWD=' + json_data["password"]
            self.conn = pyodbc.connect(conn_str)
            Connection.__instance = self.conn

    def clear(self):
        Connection.__instance = None
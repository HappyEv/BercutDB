import json
import pyodbc


class Connection:
    __instance = None

    def __init__(self):
        if Connection.__instance is not None:
            raise Exception("More than one instance in Singleton")
        else:
            file = open("resourses/connection_config.json")
            json_data = json.load(file)
            conn_str = 'DRIVER={' + json_data["driver"] + '}; \
                                SERVER=' + json_data["server"] + '; \
                                DATABASE=' + json_data["db"] + '; \
                                UID=' + json_data["user"] + '; \
                                PWD=' + json_data["password"]
            self.conn = pyodbc.connect(conn_str)
            Connection.__instance = self

    def clear(self):
        Connection.__instance = None
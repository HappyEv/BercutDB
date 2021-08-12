import json
import pyodbc


class Connection:
    def __new__(cls, path):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Connection, cls).__new__(cls)
        return cls.instance

    def __init__(self, path):
        file = open(path)
        json_data = json.load(file)
        conn_str = 'DRIVER={' + json_data["driver"] + '}; \
                                SERVER=' + json_data["server"] + '; \
                                DATABASE=' + json_data["db"] + '; \
                                Trusted_Connection=yes;'

        self.conn = pyodbc.connect(conn_str)
        Connection.__instance = self

    def close(self):
        self.conn.close()

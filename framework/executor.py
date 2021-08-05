import pyodbc


class Executor:
    __instance = None

    def __init__(self, driver, server, db, user, password):
        if Executor.__instance is not None:
            self.cursor = Executor.__instance
        else:
            conn_str = 'DRIVER={' + driver + '}; \
                                SERVER=' + server + '; \
                                DATABASE=' + db + '; \
                                UID=' + user + '; \
                                PWD=' + password
            conn = pyodbc.connect(conn_str)
            self.cursor = conn.cursor()
            Executor.__instance = self.cursor

    def execute(self, query):
        self.cursor.execute(query)

    def commit(self):
        self.cursor.commit()

    def clear(self):
        Executor.__instance = None
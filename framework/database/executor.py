class Executor:
    __instance = None

    def __init__(self, connection):
        if Executor.__instance is not None:
            raise Exception("More than one instance in Singleton")
        else:
            self.cursor = connection.cursor()
            Executor.__instance = self

    def select(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def modify(self, query):
        self.cursor.execute(query)
        self.cursor.commit()

    def clear(self):
        Executor.__instance = None
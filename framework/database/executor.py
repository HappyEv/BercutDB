class Executor:

    def __init__(self, connection):
        self.cursor = connection.cursor()

    def select(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def modify(self, query):
        self.cursor.execute(query)
        self.cursor.commit()

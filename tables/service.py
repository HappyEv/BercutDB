import datetime


class Service:
    ADD = "INSERT INTO SERVICE (SERV_ID, NAME, CRE_DATE, SUMM_INCL, COMMENT)"\
          "VALUES ({}, '{}', '{}', {}, {});"
    SELECT = "SELECT SERV_ID FROM SERVICE ORDER BY SERV_ID"
    DELETE = "DELETE FROM SERVICE WHERE SERV_ID = {}"

    def __init__(self, id, name, summ, comment='NULL'):
        self.id = id
        self.name = name
        self.cre_date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.summ = summ
        self.comment = comment

    def add_to_table(self, executor):
        executor.execute(self.ADD.format(self.id, self.name, self.cre_date, self.summ, self.comment))
        executor.commit()

    def is_in_table(self, executor):
        executor.execute(self.SELECT)
        ids = executor.cursor.fetchall()
        id = [self.id]
        for i in ids:
            if tuple(i) == tuple(id):
                return True
        return False

    def del_from_table(self, executor):
        executor.execute(self.DELETE.format(self.id))
        executor.commit()
import datetime


class Tariff:
    ADD = "INSERT INTO TARIFF (TRPL_ID, NAME, CRE_DATE, SUMM_INCL, COMMENT)"\
          "VALUES ({}, '{}', '{}', {}, {});"
    SELECT = "SELECT TRPL_ID FROM TARIFF ORDER BY TRPL_ID"
    DELETE = "DELETE FROM TARIFF WHERE TRPL_ID = {}"

    def __init__(self, id, name, summ, comment='NULL'):
        self.id = id
        self.name = name
        self.cre_date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.summ = summ
        self.comment = comment

    def add_to_table(self, executor):
        executor.modify(self.ADD.format(self.id, self.name, self.cre_date, self.summ, self.comment))

    def is_in_table(self, executor):
        ids = executor.select(self.SELECT)
        id = [self.id]
        for i in ids:
            if tuple(i) == tuple(id):
                return True
        return False

    def del_from_table(self, executor):
        executor.modify(self.DELETE.format(self.id))

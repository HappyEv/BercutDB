from tables.base_table import BaseTable


class Tariff(BaseTable):
    _SQL_INSERT = "INSERT INTO TARIFF (TRPL_ID, NAME, CRE_DATE, SUMM_INCL, COMMENT)"\
          "VALUES ({}, '{}', '{}', {}, {});"
    _SQL_SELECT = "SELECT TRPL_ID FROM TARIFF ORDER BY TRPL_ID"
    _SQL_DELETE = "DELETE FROM TARIFF WHERE TRPL_ID = {}"
    _SQL_GET_LAST_ID = "SELECT TOP 1 TRPL_ID FROM TARIFF ORDER BY TRPL_ID DESC"

    def __init__(self, executor, name, summ, comment='NULL'):
        super(Tariff, self).__init__(executor)
        self.name = name
        self.summ = summ
        self.comment = comment

    def add_to_table(self, executor):
        executor.modify(self._SQL_INSERT.format(self.id, self.name, self.cre_date, self.summ, self.comment))


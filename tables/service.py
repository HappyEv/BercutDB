from tables.base_table import BaseTable


class Service(BaseTable):
    _SQL_INSERT = "INSERT INTO SERVICE (SERV_ID, NAME, CRE_DATE, SUMM_INCL, COMMENT)"\
          "VALUES ({}, '{}', '{}', {}, {});"
    _SQL_SELECT = "SELECT SERV_ID FROM SERVICE ORDER BY SERV_ID"
    _SQL_DELETE = "DELETE FROM SERVICE WHERE SERV_ID = {}"
    _SQL_GET_LAST_ID = "SELECT TOP 1 SERV_ID FROM SERVICE ORDER BY SERV_ID DESC"

    def __init__(self, executor, name, summ, comment='NULL'):
        super(Service, self).__init__(executor)
        self.name = name
        self.summ = summ
        self.comment = comment

    def add_to_table(self):
        self.executor.modify(self._SQL_INSERT.format(self.id, self.name, self.cre_date, self.summ, self.comment))


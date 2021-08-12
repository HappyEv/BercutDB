import datetime

from tables.base_table import BaseTable


class SubsService(BaseTable):
    _SQL_SELECT = "SELECT SUBS_SERV_ID FROM SUBS_SERVICE ORDER BY SUBS_SERV_ID"
    _SQL_SELECT_STATUS = "SELECT SERV_STAT_ID FROM SUBS_SERVICE WHERE SUBS_SERV_ID = {}"
    _SQL_DELETE = "DELETE FROM SUBS_SERVICE WHERE SUBS_SERV_ID = {}"
    _SQL_GET_LAST_ID = "SELECT TOP 1 SUBS_SERV_ID FROM SUBS_SERVICE ORDER BY SUBS_SERV_ID DESC"

    def __init__(self, executor, subs_id, serv_id):
        self.id = tuple(executor.select(self._SQL_GET_LAST_ID)[0])[0]
        self.cre_date = datetime.datetime.now().strftime("%Y-%m-%d %X")
        self.subs_id = subs_id
        self.serv_id = serv_id
        self.serv_status_id = 4
        self.executor = executor

    def get_status(self):
        return tuple(self.executor.select(self._SQL_SELECT_STATUS.format(self.id))[0])[0]

    def update_status(self):
        self.serv_status_id = self.get_status()
import datetime
from abc import ABC, abstractmethod


class BaseTable(ABC):
    def __init__(self, executor):
        self.id = tuple(executor.select(self._SQL_GET_LAST_ID)[0])[0] + 1
        self.cre_date = datetime.datetime.now().strftime("%Y-%m-%d %X")

    def is_in_table(self, executor):
        ids = executor.select(self._SQL_SELECT)
        id = [self.id]
        for i in ids:
            if tuple(i) == tuple(id):
                return True
        return False

    def del_from_table(self, executor):
        executor.modify(self._SQL_DELETE.format(self.id))

    @abstractmethod
    def add_to_table(self, executor):
        pass

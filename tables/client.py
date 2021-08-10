from tables.base_table import BaseTable


class Client(BaseTable):
    _SQL_INSERT = """
BEGIN
	DECLARE @id int;

	EXECUTE CreateClient	@Name = '{}',
							@ClntTypeId = {},
							@BalanceSumm = {},
							@ClientId = @id OUTPUT
	print @id
end
    """
    _SQL_SELECT = "SELECT CLNT_ID FROM CLIENT ORDER BY CLNT_ID"
    _SQL_DELETE = """DELETE FROM CLIENT_BALANCE WHERE CLNT_BAL_ID = {}
                     DELETE FROM CLIENT WHERE CLNT_ID = {}
                  """
    _SQL_GET_LAST_ID = "SELECT TOP 1 CLNT_ID FROM CLIENT ORDER BY CLNT_ID DESC"

    def __init__(self, executor, type_id, name, summ, addr_city='NULL', addr_street='NULL', addr_house='NULL',
                 email='NULL', comment='NULL'):
        super(Client, self).__init__(executor)
        self.type_id = type_id
        self.name = name
        self.summ = summ
        self.addr_city = addr_city
        self.addr_street = addr_street
        self.addr_house = addr_house
        self.email = email
        self.comment = comment

    def del_from_table(self, executor):
        executor.modify(self._SQL_DELETE.format(self.id, self.id))

    def add_to_table(self, executor):
        executor.modify(self._SQL_INSERT.format(self.name, self.type_id, self.summ))
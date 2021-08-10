from tables.base_table import BaseTable


class Subscriber(BaseTable):
    _SQL_INSERT = """
BEGIN
	DECLARE @id int;
	EXECUTE CreateSubscriber	@Name = '{}',
								@ClientId = {},
                                @TrplId = {},
								@Msisdn = '{}',
								@SubscriberId = @id OUTPUT
	print @id
end"""
    _SQL_SELECT = "SELECT SUBS_ID FROM SUBSCRIBER ORDER BY SUBS_ID"
    _SQL_DELETE = "DELETE FROM SUBSCRIBER WHERE SUBS_ID = {}"
    _SQL_GET_LAST_ID = "SELECT TOP 1 SUBS_ID FROM SUBSCRIBER ORDER BY SUBS_ID DESC"

    def __init__(self, executor, client_id, tariff_id, phone, name, comment='NULL'):
        super(Subscriber, self).__init__(executor)
        self.client_id = client_id
        self.tariff_id = tariff_id
        self.phone = phone
        self.name = name
        self.comment = comment

    def add_to_table(self, executor):
        executor.modify(self._SQL_INSERT.format(self.name, self.client_id, self.tariff_id, self.phone))

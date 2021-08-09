import datetime


class TariffService:
    _SQL_INSERT_PROCEDURE = """
                            BEGIN
                                "DECLARE @id int;"
	                            Execute AddServiceToTrpl	@TrplId = {},
								                            @ServId = {},
								                            @TarServId = @id output
                            end
                            """
    _SQL_SELECT = "SELECT TAR_SERV_ID FROM TARIFF_SERVICE ORDER BY TAR_SERV_ID"
    _SQL_DELETE = "DELETE FROM TARIFF_SERVICE WHERE TAR_SERV_ID = {}"

    def __init__(self, id, tariff_id, service_id):
        self.id = id
        self.tariff_id = tariff_id
        self.service_id = service_id
        self.cre_date = datetime.datetime.now().strftime("%Y-%m-%d")

    def add_to_table(self, executor):
        executor.modify(self._SQL_INSERT_PROCEDURE.format(self.tariff_id, self.service_id))

    def is_in_table(self, executor):
        ids = executor.select(self._SQL_SELECT)
        id = [self.id]
        for i in ids:
            if tuple(i) == tuple(id):
                return True
        return False

    def del_from_table(self, executor):
        executor.modify(self._SQL_DELETE.format(self.id))
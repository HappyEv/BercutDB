from tables.base_table import BaseTable


class TariffService(BaseTable):
    _SQL_INSERT_PROCEDURE = """
                            BEGIN
                                DECLARE @id int;
	                            Execute AddServiceToTrpl	@TrplId = {},
								                            @ServId = {},
								                            @TarServId = @id output
                            end
                            """
    _SQL_SELECT = "SELECT TAR_SERV_ID FROM TARIFF_SERVICE ORDER BY TAR_SERV_ID"
    _SQL_DELETE = "DELETE FROM TARIFF_SERVICE WHERE TAR_SERV_ID = {}"
    _SQL_GET_LAST_ID = "SELECT TOP 1 TAR_SERV_ID FROM TARIFF_SERVICE ORDER BY TAR_SERV_ID DESC"

    def __init__(self, executor, tariff_id, service_id):
        super(TariffService, self).__init__(executor)
        self.tariff_id = tariff_id
        self.service_id = service_id

    def add_to_table(self):
        self.executor.modify(self._SQL_INSERT_PROCEDURE.format(self.tariff_id, self.service_id))

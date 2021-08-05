import pytest
from tables.service import Service
from file_manager import FileManager
from tables.tariff import Tariff


@pytest.mark.usefixtures("setup")
class TestCases:
    def test_1(self):
        params = FileManager.get_data("test_1", "../test_data.json")
        service = Service(params["service"]["id"], params["service"]["name"], params["service"]["summ"])
        service.add_to_table(self.executor)
        assert service.is_in_table(self.executor)
        params = FileManager.get_data("test_1", "../test_data.json")
        tariff = Tariff(params["tariff"]["id"], params["tariff"]["name"], params["tariff"]["summ"])
        tariff.add_to_table(self.executor)
        assert tariff.is_in_table(self.executor)

        tariff.del_from_table(self.executor)
        service.del_from_table(self.executor)

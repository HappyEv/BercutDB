import pytest
from tables.service import Service
from tables.tariff import Tariff
from tables.tariff_service import TariffService


@pytest.mark.usefixtures("setup")
class TestCases:
    def test_1(self):
        params = self.test_data.get_data("test_1")
        service = Service(self.executor, params["service"]["name"], params["service"]["summ"])
        self.post_delete.append(service)
        service.add_to_table(self.executor)
        assert service.is_in_table(self.executor)
        params = self.test_data.get_data("test_1")
        tariff = Tariff(self.executor, params["tariff"]["name"], params["tariff"]["summ"])
        self.post_delete.append(tariff)
        tariff.add_to_table(self.executor)
        assert tariff.is_in_table(self.executor)
        tariff_service = TariffService(self.executor, tariff.id, service.id)
        self.post_delete.append(tariff_service)
        tariff_service.add_to_table(self.executor)
        assert tariff.is_in_table(self.executor)
        
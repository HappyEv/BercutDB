import pytest
from tables.service import Service
from tables.tariff import Tariff
from tables.tariff_service import TariffService
from tables.client import Client
from tables.subscriber import Subscriber


@pytest.mark.usefixtures("setup")
class TestBercutDB:
    def test_1(self):
        params = self.test_data.get_data("test_1")
        service = Service(self.executor, params["service"]["name"], params["service"]["summ"])
        self.post_delete.append(service)
        service.add_to_table(self.executor)
        assert service.is_in_table(self.executor)

        tariff = Tariff(self.executor, params["tariff"]["name"], params["tariff"]["summ"])
        self.post_delete.append(tariff)
        tariff.add_to_table(self.executor)
        assert tariff.is_in_table(self.executor)

        client = Client(self.executor, params["client"]["type_id"], params["client"]["name"], params["client"]["balance"])
        self.post_delete.append(client)
        client.add_to_table(self.executor)
        assert client.is_in_table(self.executor)

        subscriber = Subscriber(self.executor, client.id, tariff.id, params["subscriber"]["phone"], params["subscriber"]["name"])
        self.post_delete.append(subscriber)
        subscriber.add_to_table(self.executor)
        assert subscriber.is_in_table(self.executor)

        tariff_service = TariffService(self.executor, tariff.id, service.id)
        self.post_delete.append(tariff_service)
        tariff_service.add_to_table(self.executor)
        assert tariff.is_in_table(self.executor)

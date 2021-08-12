import pytest
import pyodbc
import allure
from framework.database.executor import Executor
from framework.database.connection import Connection
from framework.utils.file_manager import FileManager
from tables.service import Service
from tables.tariff import Tariff
from tables.tariff_service import TariffService
from tables.client import Client
from tables.subscriber import Subscriber
from tables.subs_service import SubsService


@pytest.fixture(scope="class")
def connection(request):
    connection = Connection("D:\\BercutDB\\resourses\\connection_config.json")
    executor = Executor(connection.conn)
    test_data = FileManager("D:\\BercutDB\\resourses\\test_data.json")
    request.cls.executor = executor
    request.cls.test_data = test_data
    yield
    connection.close()


@pytest.fixture(scope="function")
def clear_db(request):
    post_delete = []
    request.cls.post_delete = post_delete
    yield
    for i in reversed(request.cls.post_delete):
        try:
            i.del_from_table()
        except pyodbc.IntegrityError:
            continue


@pytest.fixture(scope="function")
def create_product(request):
    with allure.step("Шаг 1: Создать услугу"):
        params = request.cls.test_data.get_data("test_1")
        request.cls.service = Service(request.cls.executor, params["service"]["name"], params["service"]["summ"])
        request.cls.post_delete.append(request.cls.service)
        request.cls.service.add_to_table()
        assert request.cls.service.is_in_table()

    with allure.step("Шаг 2: Создать ТП"):
        request.cls.tariff = Tariff(request.cls.executor, params["tariff"]["name"], params["tariff"]["summ"])
        request.cls.post_delete.append(request.cls.tariff)
        request.cls.tariff.add_to_table()
        assert request.cls.tariff.is_in_table()

    with allure.step("Шаг 3: Добавить услугу на ТП"):
        request.cls.tariff_service = TariffService(request.cls.executor, request.cls.tariff.id, request.cls.service.id)
        request.cls.post_delete.append(request.cls.tariff_service)
        request.cls.tariff_service.add_to_table()
        assert request.cls.tariff.is_in_table()

    with allure.step("Шаг 4: Создать клиента"):
        request.cls.client = Client(request.cls.executor, params["client"]["type_id"], params["client"]["name"],
                                    params["client"]["balance"])
        request.cls.post_delete.append(request.cls.client)
        request.cls.client.add_to_table()
        assert request.cls.client.is_in_table()

    with allure.step("Шаг 5: Создать абонента"):
        request.cls.subscriber = Subscriber(request.cls.executor, request.cls.client.id, request.cls.tariff.id,
                                            params["subscriber"]["phone"],
                                            params["subscriber"]["name"])
        request.cls.post_delete.append(request.cls.subscriber)
        request.cls.subscriber.add_to_table()
        assert request.cls.subscriber.is_in_table()

    with allure.step("Шаг 6: Проверить услуги в таблице SUBS_SERVICE"):
        request.cls.subs_service = SubsService(request.cls.executor, request.cls.subscriber.id, request.cls.service.id)
        request.cls.post_delete.append(request.cls.subs_service)
        assert request.cls.subs_service.is_in_table()

import allure
import pyodbc
import pytest
from steps import steps


@pytest.mark.usefixtures("connection", "clear_db", "create_product")
class TestBercutDB:
    @allure.story("Тест-кейс 1: Создание абонента с базовым ТП")
    def test_1_create_subscriber_with_basic_tp(self):
        pass

    @allure.story("Тест-кейс 2: Активация абонента")
    def test_2_activate_subscriber(self):
        steps.activate_sub(self.subscriber, 1)
        steps.check_service_stat(self.subs_service, 1)
        steps.check_client_balance(self.client, self.test_data.get_data("test_2")["balance_summ"], 1)

    @allure.story("Тест-кейс 3: Ошибка активации абонента")
    def test_3_activate_subscriber_error(self):
        steps.set_client_balance(self.client, self.test_data.get_data("test_3")["balance_summ"])

        with allure.step("Выполнить активацию клиента(ожидается ошибка)"):
            with pytest.raises(pyodbc.ProgrammingError):
                self.subscriber.activate()
            assert self.subscriber.subs_stat_id == 4

        steps.check_service_stat(self.subs_service, 4)
        steps.check_client_balance(self.client, self.test_data.get_data("test_3")["balance_summ_expected"], 1)

    @allure.story("Тест-кейс 4: Блокирование абонента при активации")
    def test_4_blocked_subscriber_activation(self):
        steps.set_client_balance(self.client, self.test_data.get_data("test_4")["balance_summ"])
        steps.activate_sub(self.subscriber, 1) # по условию должно быть 3
        steps.check_service_stat(self.subs_service, 1)
        steps.check_client_balance(self.client, self.test_data.get_data("test_4")["balance_summ_expected"], 3)
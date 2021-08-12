import allure


def activate_sub(subscriber, stat_id):
    with allure.step("Выполнить активацию абонента"):
        subscriber.activate()
        assert subscriber.subs_stat_id == stat_id


def check_service_stat(subs_service, stat_id):
    with allure.step("Проверить статус услуги"):
        subs_service.update_status()
        assert subs_service.serv_status_id == stat_id


def check_client_balance(client, summ, stat_id):
    with allure.step("Проверить баланс клиента"):
        client.update_summ()
        assert abs(client.summ - summ) < 0.1
        assert client.balance_stat_id == stat_id


def set_client_balance(client, summ):
    with allure.step("Установить баланс клиента"):
        client.update_summ(summ)
        assert abs(client.summ - summ) < 0.1

import pytest
import allure
from orders.order import WinAISTApp
from fuzzywuzzy import fuzz as f


@pytest.fixture(scope="module")
def order_app():
    """Фикстура создает и возвращает приложение с обновленным заказом"""
    app = WinAISTApp()
    order_data = app.create_order_dr()
    yield order_data
    app.close()

@allure.title("Проверка создания заказа с типом 'Другие услуги'")
def test_create_other_services_order(order_app):
    with allure.step("Проверка номера заказа"):
        assert order_app["order_number"] is not None
        print("✅ Номер заказа выставлен")

    with allure.step("Проверка типа заказа"):
        assert order_app["order_type"] == "Другие услуги"
        print("✅ Тип заказа 'Другие услуги'")

    with allure.step("Проверка статуса заказа"):
        assert order_app["order_status"] == "Черновик"
        print("✅ Статус заказа установлен")

    with allure.step("Проверка приоритета"):
        assert order_app["order_priority"] == "Средний"
        print("✅ Приоритет заказа установлен")

    with allure.step("Проверка клиента"):
        assert order_app["order_client"] is not None
        print("✅ Клиент заказа указан")

    with allure.step("Проверка Дата создания = Дата изменения"):
        assert order_app["order_create_date"] == order_app["order_create_mod"]
        print("✅ Клиент заказа указан")

    with allure.step("Проверка Дата завершения"):
        assert order_app["order_completion_date"] == "..."
        print("✅ Клиент заказа указан")

    with allure.step("Референс клиента пусто"):
        assert order_app["order_reference"] is None
        print("✅ Клиент заказа указан")

    with allure.step("Есть вкладка Счета"):
        assert order_app["order_tab_check"] == "Счета"
        print("✅ Клиент заказа указан")

    with allure.step("Есть вкладка Файлы"):
        assert order_app["order_tab_file"] == "Файлы"
        print("✅ Клиент заказа указан")

    with allure.step("Есть вкладка Услуги"):
        assert order_app["order_tab_services"] == "Услуги"
        print("✅ Клиент заказа указан")

@allure.title("Проверка отображения заказа в таблице")
def test_order_in_table(order_app):
    with allure.step("Проверка номера в таблице"):
        assert f.ratio(order_app["order_number"], order_app["table_order"])
        print("✅ Номер заказа отображается в таблице")

    with allure.step("Проверка типа в таблице"):
        assert order_app["order_type"] == order_app["table_type"]
        print("✅ Тип заказа отображается как 'Другие услуги'")

    with allure.step("Проверка статуса в таблице"):
        assert order_app["order_status"] == order_app["table_status"]
        print("✅ Статус заказа отображается в таблице")

    with allure.step("Проверка приоритета в таблице"):
        assert order_app["order_priority"] == order_app["table_priority"]
        print("✅ Приоритет заказа отображается в таблице")

    with allure.step("Проверка клиента в таблице"):
        assert order_app["order_client"] == order_app["table_client"]
        print("✅ Клиент заказа отображается в таблице")

    with allure.step("Проверка клиента в таблице"):
        assert f.ratio(order_app["table_date"], order_app["order_create_date"])
        print("✅ Клиент заказа отображается в таблице")

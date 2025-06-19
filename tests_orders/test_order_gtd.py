import pytest
import allure
from orders.order import WinAISTApp
from fuzzywuzzy import fuzz as f


@pytest.fixture(scope="module")
def order_data():
    """Фикстура создает и возвращает данные из приложения"""
    app = WinAISTApp()
    data = app.gtd()
    yield data
    app.close()


@allure.title("Комплексная проверка данных заказа и ГТД")
def test_full_order_validation(order_data):
    with allure.step("Проверка номера заказа"):
        assert f.ratio(order_data["order_number"], order_data["order_number_dialogue"])
        print("✅ Номер заказа соответствует")

    with allure.step("Проверка клиента заказа и клиента в ГТД"):
        assert order_data["client_order"] == order_data["client_gtd"]
        print("✅ Клиент соответствует в заказе")

    with allure.step("Проверка процедуры ГТД"):
        assert order_data["procedure_gtd"] == "ИМ 40"
        print("✅ Процедура ИМ 40 подтверждена")

    with allure.step("Проверка номера груза (ТЭ)"):
        assert order_data["number_te"] == order_data["number_te_order"]
        print("✅ Номер груза соответствует")

    with allure.step("Проверка статуса записей"):
        assert order_data["all_status"] == "Всего записей: 0 | Выделено записей: 0"
        print("✅ Всего записей 0")

import pytest
import allure
from fuzzywuzzy import fuzz as f
from orders.order import WinAISTApp


@pytest.fixture(scope="module")
def order_app():
    """Фикстура создает и возвращает приложение с созданным заказом"""
    app = WinAISTApp()
    order_data = app.forwarding()
    yield order_data
    app.close()


@allure.title("Полная проверка экспедирования (создание, атрибуты, таблица)")
@pytest.mark.order(1)
def test_forwarding_order_full_check(order_app):
    with allure.step("Сравниваем номер заказа с номером экспедирования"):
        assert f.ratio(order_app["order_number"], order_app["forwarding_order_number"])

    with allure.step("Проверяем, что тип экспедирования — 'Портовое'"):
        assert order_app["forwarding_type"] == "Портовое"

    with allure.step("Проверяем, что статус экспедирования — 'Черновик'"):
        assert order_app["forwarding_status"] == "Черновик"

    with allure.step("Проверяем, что приоритет — 'Средний'"):
        assert order_app["forwarding_priority"] == "Средний"

    with allure.step("Проверяем, что ответственный — 'Administrator S.'"):
        assert order_app["forwarding_otv"] == "Administrator S."

    with allure.step("Проверяем, что дата создания равна дате модификации"):
        assert order_app["forwarding_create_date"] == order_app["forwarding_mode_date"]

    with allure.step("Проверяем, что в таблице отображается 'Портовое'"):
        assert order_app["forwarding_order_table"] == "Портовое"

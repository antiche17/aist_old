import pytest
import allure
from difflib import SequenceMatcher as f
from orders.order import WinAISTApp
import pytest_check as check


@pytest.fixture(scope="module")
def order_app():
    """Фикстура создает и возвращает приложение с созданным заказом"""
    app = WinAISTApp()
    order_data = app.order_del2()
    yield order_data
    app.close()


@allure.title("Проверка создание Входящий платеж в заказе. 19 проверок")
@pytest.mark.order(1)
def test_value_order(order_app):
    with allure.step("1. Первый заказ"):
        check.is_true(order_app["order1"] in order_app["del_window"], "❌ ФР: ВП не совпадает")

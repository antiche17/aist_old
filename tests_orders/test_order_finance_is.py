import pytest
import allure
from difflib import SequenceMatcher as f
from orders.order import WinAISTApp
import pytest_check as check


@pytest.fixture(scope="module")
def order_app():
    """Фикстура создает и возвращает приложение с созданным заказом"""
    app = WinAISTApp()
    order_data = app.finance_is()
    yield order_data
    app.close()


@allure.title("Проверка создание Исходящего счета в заказе")
@pytest.mark.order(1)
def test_value_order(order_app):
    with allure.step("1. Тип заказа — Логистика"):
        check.equal(order_app["is_buyer"], order_app["is_buyer_table"], "❌ ФР: Поле с другим значением, но должно быть Логистика")


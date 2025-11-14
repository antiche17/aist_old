from orders.finance import WinAISTApp
import pytest
import allure
import pytest_check as check
from locators.format_data import compare_dates


@pytest.fixture(scope="module")
def order_app():
    print("")
    app = WinAISTApp()
    try:
        order_data = app.finance_ip()
        yield order_data
    finally:
        print("[TEARDOWN] Закрытие WinAISTApp")
        app.close()

@allure.suite("Проверка ИП")
@allure.title("Проверка ИП, проверок 134")
@pytest.mark.order(1)
def test_finance_is(order_app):
    with allure.step("1. Дата в форме Создание ИС"):
        check.is_true(order_app["is_date"], "❌ ФР: Пустое поле")

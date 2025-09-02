import pytest
import allure
from difflib import SequenceMatcher
from orders.finance import WinAISTApp
import pytest_check as check


@pytest.fixture(scope="module")
def order_app():
    print("[SETUP] Запуск фикстуры order_app")
    app = WinAISTApp()
    order_data = app.finance()
    yield order_data
    print("[TEARDOWN] Закрытие WinAISTApp")
    app.close()

def check_equal_dates(value1, value2, field_name):
    normalized1 = normalize_date(value1)
    normalized2 = normalize_date(value2)
    check.equal(normalized1, normalized2, f"❌ ФР: Не одинаковый {field_name}")

@allure.title("Проверка Таблицы Грузы")
@pytest.mark.order(1)
def test_finance(order_app):
    with allure.step("2. Сравниваем созданного клиента"):
        check.equal(order_app["name_client"], order_app["name_client_order"], "❌ ФР: клиенты не одинаковые")
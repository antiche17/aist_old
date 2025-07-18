import pytest
import allure
from orders.freight import WinAISTApp
import pytest_check as check


@pytest.fixture(scope="module")
def order_app():
    print("[SETUP] Запуск фикстуры order_app")
    app = WinAISTApp()
    order_data = app.freight()
    yield order_data
    print("[TEARDOWN] Закрытие WinAISTApp")
    app.close()


@allure.title("Удаление одного заказа, 2 проверки")
@pytest.mark.order(1)
def test_value_del(order_app):
    with allure.step("1. Сравниваем удалённый заказ с текущим в таблице Заказы"):
        check.is_false(order_app["delete_order"] == order_app["table_order"], "❌ ФР: номера одинаковые")

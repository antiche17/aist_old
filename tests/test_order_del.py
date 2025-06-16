import pytest
import allure
from orders.order import WinAISTApp


@pytest.fixture(scope="module")
def order_app():
    print("[SETUP] Запуск фикстуры order_app")
    app = WinAISTApp()
    order_data = app.create_order_del()
    yield order_data
    print("[TEARDOWN] Закрытие WinAISTApp")
    app.close()


@allure.title("Удаление одного заказа")
@pytest.mark.order(1)
def test_value_del(order_app):
    with allure.step("Сравниваем удалённый заказ с текущим в таблице"):
        assert order_app["delete_order"] != order_app["table_order"]
        print("✅ Прошел тест! Удалился заказ")


@allure.title("Удаление двух заказов")
@pytest.mark.order(2)
def test_value_del_two(order_app):
    with allure.step("Сравниваем удаление двух заказов в таблице"):
        assert order_app["table_order_del1"] != order_app["table_order_1"]
        assert order_app["table_order_del1"] != order_app["table_order_2"]
        assert order_app["table_order_del2"] != order_app["table_order_2"]
        assert order_app["table_order_del2"] != order_app["table_order_1"]
        print("✅ Прошел тест! Удалились два заказа")

import pytest
import allure
from orders.freight import WinAISTApp
import pytest_check as check
from locators.function import Function


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
    with allure.step("1. Сравниваем номер заказ в таблице "):
        check.equal(order_app["order_number"], order_app["order_number_table"], "❌ ФР: номера не одинаковые")

    with allure.step("2. Сравниваем созданного клиента"):
        check.equal(order_app["name_client"], order_app["name_client_order"], "❌ ФР: клиенты не одинаковые")


    with allure.step("3. Сравниваем ТЕ"):
        check.equal(order_app["type_freight"], order_app["type_freight_form"], "❌ ФР: ТЕ не одинаковые")

    with allure.step("4. Сравниваем Тип ТЕ"):
        check.equal(order_app["type_te"], order_app["type_te_form"], "❌ ФР: Тип ТЕ не одинаковые")

    with allure.step("5. Сравниваем количество"):
        check.equal(order_app["quantity"], order_app["quantity_form"], "❌ ФР: количество не одинаковые")

    with allure.step("6. Сравниваем единица измерения"):
        check.equal(order_app["uom"], order_app["uom_form"], "❌ ФР: единица измерения не одинаковые")

    with allure.step("7. Сравниваем номер ТЕ"):
        check.equal(order_app["te_number"], order_app["te_number_form"], "❌ ФР: номер ТЕ не одинаковые")




    with allure.step("2. Сравниваем соданого клиента"):
        check.equal(order_app["name_client"], order_app["name_client_order"], "❌ ФР: клиенты не одинаковые")
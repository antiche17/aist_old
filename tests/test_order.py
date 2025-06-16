import pytest
import allure
from fuzzywuzzy import fuzz as f
from orders.order import WinAISTApp


@pytest.fixture(scope="module")
def order_app():
    """Фикстура создает и возвращает приложение с созданным заказом"""
    app = WinAISTApp()
    order_data = app.create_order()
    yield order_data
    app.close()


@allure.title("Проверка номера заказа")
@pytest.mark.order(1)
def test_value_order(order_app):
    with allure.step("Проверяем, что номер заказа не пустой"):
        assert order_app["order_number"] is not None


@allure.title("Сравнение номера заказа с таблицей")
@pytest.mark.order(2)
def test_value_order_table(order_app):
    with allure.step("Сравниваем номер заказа с отображением в таблице"):
        assert f.ratio(order_app["order_number"], order_app["table_order"])


@allure.title("Проверка типа заказа")
@pytest.mark.order(3)
def test_value_type(order_app):
    with allure.step("Проверяем, что тип заказа — Логистика"):
        assert order_app["order_type"] == "Логистика"


@allure.title("Сравнение типа заказа с таблицей")
@pytest.mark.order(4)
def test_value_type_table(order_app):
    with allure.step("Сравниваем тип заказа с отображением в таблице"):
        assert order_app["order_type"] == order_app["table_type"]


@allure.title("Проверка статуса заказа")
@pytest.mark.order(5)
def test_value_status(order_app):
    with allure.step("Проверяем, что статус заказа — Черновик"):
        assert order_app["order_status"] == "Черновик"


@allure.title("Сравнение статуса заказа с таблицей")
@pytest.mark.order(6)
def test_value_status_table(order_app):
    with allure.step("Сравниваем статус заказа с отображением в таблице"):
        assert order_app["order_status"] == order_app["table_status"]


@allure.title("Проверка приоритета заказа")
@pytest.mark.order(7)
def test_value_priority(order_app):
    with allure.step("Проверяем, что приоритет заказа — Средний"):
        assert order_app["order_priority"] == "Средний"


@allure.title("Сравнение приоритета заказа с таблицей")
@pytest.mark.order(8)
def test_value_priority_table(order_app):
    with allure.step("Сравниваем приоритет заказа с отображением в таблице"):
        assert order_app["order_priority"] == order_app["table_priority"]


@allure.title("Проверка ответственного заказа")
@pytest.mark.order(9)
def test_value_creator(order_app):
    with allure.step("Проверяем, что указанный ответственный существует"):
        assert order_app["order_creator"] is not None


@allure.title("Сравнение ответственного заказа с таблицей")
@pytest.mark.order(10)
def test_value_creator_table(order_app):
    with allure.step("Сравниваем ответственного с таблицей"):
        assert order_app["order_creator"] == order_app["table_creator"]


@allure.title("Проверка клиента заказа")
@pytest.mark.order(11)
def test_value_client(order_app):
    with allure.step("Проверяем, что клиент заказа указан"):
        assert order_app["order_client"] is not None


@allure.title("Сравнение клиента заказа с таблицей")
@pytest.mark.order(12)
def test_value_client_table(order_app):
    with allure.step("Сравниваем клиента заказа с отображением в таблице"):
        assert order_app["order_client"] == order_app["table_client"]

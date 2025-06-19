import pytest
import allure
from fuzzywuzzy import fuzz as f
from orders.order import WinAISTApp


@pytest.fixture(scope="module")
def order_app():
    """Фикстура создает и возвращает приложение с созданным заказом"""
    app = WinAISTApp()
    order_data = app.transportation()
    yield order_data
    app.close()


@allure.title("Проверка создания и удаления морской перевозки")
@pytest.mark.order(1)
def test_sea_transportation(order_app):
    with allure.step("Сравниваем номер заказа с номером морской перевозки"):
        assert f.ratio(order_app["order_number"], order_app["sea_order_number"])

    with allure.step("Проверяем имя заказа"):
        assert order_app["sea_order_name"] == "Морская перевозка: Новая морская перевозка"

    with allure.step("Проверяем тип перевозки"):
        assert order_app["sea_type"] == "Морская перевозка"

    with allure.step("Проверяем статус"):
        assert order_app["sea_status"] == "Черновик"

    with allure.step("Проверяем приоритет"):
        assert order_app["sea_priority"] == "Средний"

    with allure.step("Проверяем ответственного"):
        assert order_app["sea_otv"] == "Administrator S."

    with allure.step("Проверяем дату создания и модификации"):
        assert order_app["sea_create_date"] == order_app["sea_mode_date"]

    with allure.step("Проверяем отображение в таблице"):
        assert order_app["sea_order_table"] == "Морская перевозка"


@allure.title("Проверка создания и удаления автоперевозки")
@pytest.mark.order(2)
def test_auto_transportation(order_app):
    with allure.step("Сравниваем номер заказа с номером автоперевозки"):
        assert f.ratio(order_app["order_number"], order_app["auto_order_number"])

    with allure.step("Проверяем тип перевозки"):
        assert order_app["auto_type"] == "Автоперевозка"

    with allure.step("Проверяем статус"):
        assert order_app["auto_status"] == "Черновик"

    with allure.step("Проверяем приоритет"):
        assert order_app["auto_priority"] == "Средний"

    with allure.step("Проверяем ответственного"):
        assert order_app["auto_otv"] == "Administrator S."

    with allure.step("Проверяем дату создания и модификации"):
        assert order_app["auto_create_date"] == order_app["auto_mode_date"]

    # Переделать
    #with allure.step("Проверяем отображение в таблице"):
        #assert order_app["auto_order_table"] == "Автоперевозка"

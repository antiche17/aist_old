import pytest
import allure
from fuzzywuzzy import fuzz as f
from orders.order import WinAISTApp


@pytest.fixture(scope="module")
def order_app():
    """Фикстура создает и возвращает приложение с созданным заказом"""
    app = WinAISTApp()
    order_data = app.freight()
    yield order_data
    app.close()


@allure.title("Проверка создания и удаления груза Bulkership")
@pytest.mark.order(1)
def test_bulkership_freight(order_app):
    with allure.step("Сравнение номера заказа с номером груза"):
        assert f.ratio(order_app["order_number"], order_app["freight_order_number"])

    with allure.step("Проверка типа груза — Bulkership"):
        assert order_app["freight_type"] , "Bulkership"

    with allure.step("Проверка номера груза — '0000000'"):
        assert order_app["freight_number"] , "0000000"

    with allure.step("Проверка типа транспортной единицы — 'Bag'"):
        assert order_app["freight_te_type"] , "Bag"

    with allure.step("Проверка единицы измерения — 'шт.'"):
        assert order_app["freight_oum"] , "шт."

    with allure.step("Проверка значения в таблице заказа"):
        assert order_app["freight_order_table"] , "Bulkership"


@allure.title("Проверка создания и удаления груза Container")
@pytest.mark.order(2)
def test_container_freight(order_app):
    with allure.step("Сравнение номера заказа с таблицей"):
        assert f.ratio(order_app["freight_order_table_con"], order_app["freight_order_number_con"])

    with allure.step("Проверка типа груза — Container"):
        assert order_app["freight_type_con"] , "Container"

    with allure.step("Проверка номера груза — 'XXXX 0000000'"):
        assert order_app["freight_number_con"] , "XXXX 0000000"

    with allure.step("Проверка типа транспортной единицы — '20\' dc'"):
        assert order_app["freight_te_type_con"] , "20' dc"

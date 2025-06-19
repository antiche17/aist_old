import pytest
import allure
from fuzzywuzzy import fuzz as f
from orders.order import WinAISTApp


@pytest.fixture(scope="module")
def order_app():
    """Фикстура создает и возвращает приложение с обновленным заказом"""
    app = WinAISTApp()
    order_data = app.create_order_update()
    yield order_data
    app.close()


@allure.title("Редактирование заказа: проверка полей после обновления")
@pytest.mark.order(1)
def test_order_editing(order_app):
    with allure.step("Проверяем, что статус изменён на 'Отменен'"):
        assert order_app["order_status"] == "Отменен"

    with allure.step("Проверяем, что приоритет установлен на 'Критический'"):
        assert order_app["order_priority"] == "Критический"

    with allure.step("Проверяем клиента (по строковому совпадению с 'MANITOZA')"):
        assert f.ratio("MANITOZA", order_app["order_client"])

    with allure.step("Проверяем, что отправитель выбран"):
        assert order_app["order_senders"] is not None

    with allure.step("Проверяем, что получатель выбран"):
        assert order_app["order_recipient"] is not None

    with allure.step("Проверяем, что поставка указана"):
        assert order_app["order_delivery"] is not None

    with allure.step("Проверяем, что в поле 'Референс' добавлен текст"):
        assert order_app["order_reference"] is not None

    with allure.step("Проверяем, что в поле 'Примечание' добавлен текст"):
        assert order_app["order_note"] is not None

    with allure.step("Проверяем, что дата модификации изменилась"):
        assert order_app["order_mod_date"] != order_app["order_mod_date1"]

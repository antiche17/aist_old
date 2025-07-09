import pytest
import allure
from difflib import SequenceMatcher as f
from orders.order import WinAISTApp
import pytest_check as check


@pytest.fixture(scope="module")
def order_app():
    """Фикстура создает и возвращает приложение с обновленным заказом"""
    app = WinAISTApp()
    order_data = app.gtd()
    yield order_data
    app.close()


@allure.title("Комплексная проверка данных заказа и ГТД")
@pytest.mark.order(1)
def test_full_order_validation(order_app):
    with allure.step("1. Проверка номера заказа"):
        check.is_true(order_app["gtd_order_number"] in order_app["order_number"], "❌ ❌ ФР: Не одинаковые данные (порог 50%)я")

    with allure.step("2. Проверка клиента заказа и клиента в ГТД"):
        check.equal(order_app["client_order"], order_app["client_gtd"], "ФР: Клиент не соответствует в заказе")

    with allure.step("3. Проверка процедуры ГТД"):
        check.equal(order_app["procedure_gtd"], "ИМ 40", "ФР: Процедура не ИМ 40")

    with allure.step("4. Без ТЕ не создаётся"):
        check.equal(order_app["order_te_not"], "Коносаментная партия должна содержать хотя бы один контейнер", "ФР: Нет окна или текст поменялся")

    with allure.step("5. Сравнение клиента"):
        check.equal(order_app["order_client"], order_app["client_gtd"], "❌ ФР: Не одинаковые данные")

    with allure.step("5. Проверка номера груза (ТЭ)"):
        check.equal(order_app["number_te"], order_app["number_te_order"], "ФР: Номер груза не соответствует")

    with allure.step("6. Проверка статуса записей"):
        check.equal(order_app["all_status"], "Всего записей: 0", "ФР: Есть записи")

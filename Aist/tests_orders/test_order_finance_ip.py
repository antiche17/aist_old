import pytest
import allure
from difflib import SequenceMatcher as f
from orders.order import WinAISTApp
import pytest_check as check


@pytest.fixture(scope="module")
def order_app():
    app = WinAISTApp()
    order_data = app.finance_ip()
    yield order_data
    app.close()


@allure.title("Проверка создание Исходящий платеж в заказе. 19 проверок")
@pytest.mark.order(1)
def test_value_order(order_app):
    with allure.step("1. Входящий счет"):
        check.equal(order_app["ip_create_order"], "Исходящий платеж", "❌ ФР: ИС не совпадает")

    with allure.step("2. Поле Номер счета не пустое"):
        check.is_true(order_app["ip_number"], "❌ ФР: Поле пустое")

    with allure.step("3. Поле Дата не пустое"):
        check.is_true(order_app["ip_date"], "❌ ФР: Поле пустое")

    with allure.step("4. Поле Тип счета Таможенный"):
        check.equal(order_app["ip_list"], "Таможенный", "❌ ФР: Тип счета Товарный")

    with allure.step("5. Поле Поставщик не пустое"):
        check.is_true(order_app["ip_suppler"], "❌ ФР: Поле пустое")

    with allure.step("6. Поле Номер заказа не пустое"):
        check.is_true(order_app["ip_order"], "❌ ФР: Поле пустое")

    with allure.step("8. Покупатель"):
        check.is_true(order_app["ip_buyer"], "❌ ФР: Поле Покупатель пустое")

    # Таблица
    with allure.step("9. Название счета, 2 = Исходящий платеж"):
        check.equal(order_app["ip_type_table"], "2", "❌ ФР: Не совпадает")

    with allure.step("10. Поле Номер счета"):
        check.equal(order_app["ip_number"], order_app["ip_number_table"], "❌ ФР: Не совпадает")

    with allure.step("11. Поле Дата"):
        check.equal(order_app["ip_date"], order_app["ip_date_table"], "❌ ФР: Не совпадает")

    with allure.step("12. Поле Тип счета Товарный"):
        check.equal(order_app["ip_list"], order_app["ip_appointment_table"], "❌ ФР: Не совпадает")

    with allure.step("13. Поле Поставщик"):
        check.equal(order_app["ip_suppler"], order_app["ip_suppler_table"], "❌ ФР: ИС не совпадает")

    with allure.step("14. Валюта, 3 = RUR"):
        check.equal(order_app["ip_currency_table"], "3", "❌ ФР: Валюта не рубли")

    with allure.step("15. Поле Сумма"):
        check.equal(order_app["ip_sum_table"], "0,00", "❌ ФР: ИС не совпадает")

    with allure.step("16. Поле Закрыто"):
        check.equal(order_app.get("ip_closed_table"), "0,00","❌ ФР: Разные клиенты")

    with allure.step("17. Поле Не закрыто"):
        check.equal(order_app["ip_nclosed_table"], "0,00", "❌ ФР: Поле с другим значением")

    with allure.step("18. Поле Не разнесено"):
        check.equal(order_app["ip_nincluded_table"], "0,00", "❌ ФР: Поле с другим значением")

    with allure.step("19. Поле Не закрыто"):
        check.equal(order_app["ip_appointment_table"], order_app["ip_list"], "❌ ФР: Поле с другим значением, но должно быть Логистика")



import pytest
import allure
from difflib import SequenceMatcher as f
from orders.order import WinAISTApp
import pytest_check as check


@pytest.fixture(scope="module")
def order_app():
    """Фикстура создает и возвращает приложение с созданным заказом"""
    app = WinAISTApp()
    order_data = app.finance_is()
    yield order_data
    app.close()


@allure.title("Проверка создание Исходящего счета в заказе. 19 проверок")
@pytest.mark.order(1)
def test_value_order(order_app):
    with allure.step("1. Исходящий счет"):
        check.equal(order_app["is_create_order"], "Исходящий счет", "❌ ФР: ИС не совпадает")

    with allure.step("2. Поле Номер счета не пустое"):
        check.is_true(order_app["is_number"], "❌ ФР: Поле пустое")

    with allure.step("3. Поле Дата не пустое"):
        check.is_true(order_app["is_date"], "❌ ФР: Поле пустое")

    with allure.step("4. Поле Тип счета Товарный"):
        check.equal(order_app["is_list"], "Товарный", "❌ ФР: Тип счета Товарный")

    with allure.step("5. Поле Поставщик не пустое"):
        check.is_true(order_app["is_suppler"], "❌ ФР: Поле пустое")

    with allure.step("6. Поле Номер заказа не пустое"):
        check.is_true(order_app["is_order"], "❌ ФР: Поле пустое")

    with allure.step("7. Клиент одинаковые"):
        check.equal(order_app["order_client"], order_app.get("is_client"),"❌ ФР: Разные клиенты")

    with allure.step("8. Покупатель"):
        check.is_true(order_app["is_buyer"], "❌ ФР: Поле Покупатель пустое")

    # Таблица
    with allure.step("9. Название счета"):
        check.equal(order_app["is_type_table"], "1", "❌ ФР: Не совпадает")

    with allure.step("10. Поле Номер счета"):
        check.equal(order_app["is_number"], order_app["is_number_table"], "❌ ФР: Не совпадает")

    with allure.step("11. Поле Дата"):
        check.equal(order_app["is_date"], order_app["is_date_table"], "❌ ФР: Не совпадает")

    with allure.step("12. Поле Тип счета Товарный"):
        check.equal(order_app["is_list"], order_app["is_appointment_table"], "❌ ФР: Не совпадает")

    with allure.step("13. Поле Поставщик"):
        check.equal(order_app["is_suppler"], order_app["is_suppler_table"], "❌ ФР: ИС не совпадает")

    with allure.step("14. Валюта"):
        check.equal(order_app["is_currency_table"], "3", "❌ ФР: Валюта не рубли")

    with allure.step("15. Поле Сумма"):
        check.equal(order_app["is_sum_table"], "0,00", "❌ ФР: ИС не совпадает")

    with allure.step("16. Поле Закрыто"):
        check.equal(order_app.get("is_closed_table"), "0,00","❌ ФР: Разные клиенты")

    with allure.step("17. Поле Не закрыто"):
        check.equal(order_app["is_nclosed_table"], "0,00", "❌ ФР: Поле с другим значением")

    with allure.step("18. Поле Не разнесено"):
        check.equal(order_app["is_nincluded_table"], "0,00", "❌ ФР: Поле с другим значением")

    with allure.step("19. Поле Не закрыто"):
        check.equal(order_app["is_appointment_table"], order_app["is_list"], "❌ ФР: Поле с другим значением, но должно быть Логистика")



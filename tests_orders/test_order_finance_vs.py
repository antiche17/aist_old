import pytest
import allure
from difflib import SequenceMatcher as f
from orders.order import WinAISTApp
import pytest_check as check


@pytest.fixture(scope="module")
def order_app():
    app = WinAISTApp()
    order_data = app.finance_vs()
    yield order_data
    app.close()


@allure.title("Проверка создание Исходящего счета в заказе. 19 проверок")
@pytest.mark.order(1)
def test_value_order(order_app):
    with allure.step("1. Входящий счет"):
        check.equal(order_app["vs_create_order"], "Входящий счет", "❌ ФР: ИС не совпадает")

    with allure.step("2. Поле Номер счета не пустое"):
        check.is_true(order_app["vs_number"], "❌ ФР: Поле пустое")

    with allure.step("3. Поле Дата не пустое"):
        check.is_true(order_app["vs_date"], "❌ ФР: Поле пустое")

    with allure.step("4. Поле Тип счета Фрахтовый"):
        check.equal(order_app["vs_list"], "Фрахтовый", "❌ ФР: Тип счета Товарный")

    with allure.step("5. Поле Поставщик не пустое"):
        check.is_true(order_app["vs_suppler"], "❌ ФР: Поле пустое")

    with allure.step("6. Поле Номер заказа не пустое"):
        check.is_true(order_app["vs_order"], "❌ ФР: Поле пустое")

    with allure.step("7. Поставщик одинаковые"):
        check.equal(order_app["vs_contractor"], order_app.get("vs_suppler_table"),"❌ ФР: Разные клиенты")

    with allure.step("8. Покупатель"):
        check.is_true(order_app["vs_buyer"], "❌ ФР: Поле Покупатель пустое")

    # Таблица
    with allure.step("9. Название счета, 3 = Входящий счет"):
        check.equal(order_app["vs_type_table"], "3", "❌ ФР: Не совпадает")

    with allure.step("10. Поле Номер счета"):
        check.equal(order_app["vs_number"], order_app["vs_number_table"], "❌ ФР: Не совпадает")

    with allure.step("11. Поле Дата"):
        check.equal(order_app["vs_date"], order_app["vs_date_table"], "❌ ФР: Не совпадает")

    with allure.step("12. Поле Тип счета Товарный"):
        check.equal(order_app["vs_list"], order_app["vs_appointment_table"], "❌ ФР: Не совпадает")

    with allure.step("13. Поле Поставщик"):
        check.equal(order_app["vs_suppler"], order_app["vs_suppler_table"], "❌ ФР: ИС не совпадает")

    with allure.step("14. Валюта, 3 = RUR"):
        check.equal(order_app["vs_currency_table"], "3", "❌ ФР: Валюта не рубли")

    with allure.step("15. Поле Сумма"):
        check.equal(order_app["vs_sum_table"], "0,00", "❌ ФР: ИС не совпадает")

    with allure.step("16. Поле Закрыто"):
        check.equal(order_app.get("vs_closed_table"), "0,00","❌ ФР: Разные клиенты")

    with allure.step("17. Поле Не закрыто"):
        check.equal(order_app["vs_nclosed_table"], "0,00", "❌ ФР: Поле с другим значением")

    with allure.step("18. Поле Не разнесено"):
        check.equal(order_app["vs_nincluded_table"], "0,00", "❌ ФР: Поле с другим значением")

    with allure.step("19. Поле Не закрыто"):
        check.equal(order_app["vs_appointment_table"], order_app["vs_list"], "❌ ФР: Поле с другим значением, но должно быть Логистика")



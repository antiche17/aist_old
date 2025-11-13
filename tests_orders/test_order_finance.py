import pytest
import allure
from orders.order import WinAISTApp
import pytest_check as check
from locators.format_data import compare_dates


@pytest.fixture(scope="module")
def order_app():
    app = WinAISTApp()
    order_data = app.finance()
    yield order_data
    app.close()


@allure.title("Проверка создание Исходящий платеж в заказе. 19 проверок")
def test_value_order(order_app):
    with allure.step("1. Исходящий платеж"):
        check.equal(order_app["ip_create_order"], "Исходящий платеж", "❌ ФР: ИП не совпадает")

    with allure.step("2. Поле Номер счета не пустое"):
        check.is_true(order_app["ip_number"], "❌ ФР: Поле пустое")

    with allure.step("3. Поле Дата не пустое"):
        check.is_true(order_app["ip_date"], "❌ ФР: Поле пустое")

    with allure.step("4. Поле Тип счета Таможенный"):
        check.equal(order_app["ip_list"], "Таможенный", "❌ ФР: Тип счета Товарный")

    with allure.step("5. Поле Поставщик не пустое"):
        check.is_true(order_app["ip_suppler"], "❌ ФР: Поле Поставщик пустое")

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
        compare_dates(order_app["ip_date"], order_app["ip_date_table"], "❌ ФР: Не совпадает")

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

@allure.title("Проверка создание Входящий счет в заказе. 19 проверок")
def test_value_vs(order_app):
    with allure.step("1. Входящий счет"):
        check.equal(order_app["vs_create_order"], "Входящий счет", "❌ ФР: ВС не совпадает")

    with allure.step("2. Поле Номер счета не пустое"):
        check.is_true(order_app["vs_number"], "❌ ФР: Поле пустое")

    with allure.step("3. Поле Дата не пустое"):
        check.is_true(order_app["vs_date"], "❌ ФР: Поле пустое")

    with allure.step("4. Поле Тип счета Фрахтовый"):
        check.equal(order_app["vs_list"], "Фрахтовый", "❌ ФР: Тип счета Товарный")

    with allure.step("5. Поле Поставщик не пустое"):
        check.is_true(order_app["vs_suppler"], "❌ ФР: Поле Поставщик пустое")

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
        compare_dates(order_app["vs_date"], order_app["vs_date_table"], "❌ ФР: Не совпадает")

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

@allure.title("Проверка создание Исходящего счета в заказе. 19 проверок")
def test_value_is(order_app):
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
        compare_dates(order_app["is_date"], order_app["is_date_table"], "❌ ФР: Не совпадает")

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

@allure.title("Проверка создание Входящий платеж в заказе. 19 проверок")
def test_value_vp(order_app):
    with allure.step("1. Входящий платеж"):
        check.equal(order_app["vp_create_order"], "Входящий платеж", "❌ ФР: ВП не совпадает")

    with allure.step("2. Поле Номер счета не пустое"):
        check.is_true(order_app["vp_number"], "❌ ФР: Поле пустое")

    with allure.step("3. Поле Дата не пустое"):
        check.is_true(order_app["vp_date"], "❌ ФР: Поле пустое")

    with allure.step("4. Поле Тип счета Товарный"):
        check.equal(order_app["vp_list"], "Экспедиторский", "❌ ФР: Тип счета Товарный")

    with allure.step("5. Поле Поставщик не пустое"):
        check.is_true(order_app["vp_suppler"], "❌ ФР: Поле пустое")

    with allure.step("6. Поле Номер заказа не пустое"):
        check.is_true(order_app["vp_order"], "❌ ФР: Поле пустое")

    with allure.step("7. Клиент одинаковые"):
        check.equal(order_app["order_client"], order_app.get("vp_client"),"❌ ФР: Разные клиенты")

    with allure.step("8. Покупатель"):
        check.is_true(order_app["vp_buyer"], "❌ ФР: Поле Покупатель пустое")

    # Таблица
    with allure.step("9. Название счета, 4 = Входящий платеж"):
        check.equal(order_app["vp_type_table"], "4", "❌ ФР: Не совпадает")

    with allure.step("10. Поле Номер счета"):
        check.equal(order_app["vp_number"], order_app["vp_number_table"], "❌ ФР: Не совпадает")

    with allure.step("11. Поле Дата"):
        compare_dates(order_app["vp_date"], order_app["vp_date_table"], "❌ ФР: Не совпадает")

    with allure.step("12. Поле Тип счета Товарный"):
        check.equal(order_app["vp_list"], order_app["vp_appointment_table"], "❌ ФР: Не совпадает")

    with allure.step("13. Поле Поставщик"):
        check.equal(order_app["vp_suppler"], order_app["vp_suppler_table"], "❌ ФР: ИС не совпадает")

    with allure.step("14. Валюта"):
        check.equal(order_app["vp_currency_table"], "3", "❌ ФР: Валюта не рубли")

    with allure.step("15. Поле Сумма"):
        check.equal(order_app["vp_sum_table"], "0,00", "❌ ФР: ИС не совпадает")

    with allure.step("16. Поле Закрыто"):
        check.equal(order_app.get("vp_closed_table"), "0,00","❌ ФР: Разные клиенты")

    with allure.step("17. Поле Не закрыто"):
        check.equal(order_app["vp_nclosed_table"], "0,00", "❌ ФР: Поле с другим значением")

    with allure.step("18. Поле Не разнесено"):
        check.equal(order_app["vp_nincluded_table"], "0,00", "❌ ФР: Поле с другим значением")

    with allure.step("19. Поле Не закрыто"):
        check.equal(order_app["vp_appointment_table"], order_app["vp_list"], "❌ ФР: Поле с другим значением, но должно быть Логистика")
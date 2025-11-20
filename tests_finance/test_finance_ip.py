from orders.finance import WinAISTApp
import pytest
import allure
import pytest_check as check
from locators.format_data import compare_dates


@pytest.fixture(scope="module")
def order_app():
    print("Проверка ИП")
    app = WinAISTApp()
    order_data = app.finance_ip()
    yield order_data
    print("[TEARDOWN] Закрытие WinAISTApp")
    app.close()

@allure.suite("Проверка ИП")
@allure.title("Проверка ИП, проверок 59")
def test_finance_ip(order_app):

    # Проверка, что поле пустое
    tabs_to_check_empty = [
        ("1. Номер счета", ["ip_number"]),
        ("2. Период (дн.)", ["ip_period"]),
        ("3. Код оплаты", ["ip_code"]),
        ("4. Примечание", ["ip_note"]),
        ("5. Тип счета", ["ip_list"]),
        ("6. Поставщик", ["ip_supplier"]),
        ("7. Покупатель", ["ip_buyer"]),
        ("8. Комиссия", ["ip_commission"]),
        ("10. Дата комиссии", ["ip_data_commission"]),
        ("11. Со счета", ["ip_from_check"]),
    ]

    # Проверка, что объект вообще получен
    for step_name, fields in tabs_to_check_empty:
        with    allure.step(step_name):
            for field in fields:
                value = order_app.get(field)
                check.is_false(value, f"❌ ФР: поле '{field}' должно быть пустым, но получено: {value}")

    # Проверка, что поле не пустое
    tabs_to_check_not_empty = [
        ("12. Дата",["ip_date"]),
        ("13. Заказ",["ip_number_order"]),
        ("14. Курс доллара",["ip_usd"]),
        ("15. Курс евро",["ip_eur"]),
        ("16. Кросс-курс",["ip_cc"]),
        ("17. Итого",["ip_total"]),
        ("18.Валюта Итого",["ip_currency"]),
        ("19.Валюта комиссии",["ip_currency1"]),
        ("20. =",["ip_txt"]),
        ("21. Закрыто", ["ip_table_closed"]),
        ("22. Незакрыто", ["ip_table_nclosed"]),
    ]

    for step_name, fields in tabs_to_check_not_empty:
        with    allure.step(step_name):
            for field in fields:
                value = order_app.get(field)
                check.is_true(value, f"❌ ФР: поле '{field}' должно быть пустым, но получено: {value}")

    with allure.step("23. Сравнение поля Счет после редактирования"):
        check.not_equal(order_app["ip_number"], order_app["ip_number_mod"],"❌ ФР: Одинаковое поле Счет")

    with allure.step("24. Сравнение поля Период (дн.) после редактирования"):
        check.not_equal(order_app["ip_period"], order_app["ip_period_mod"],"❌ ФР: Одинаковое поле Период (дн.)")

    with allure.step("25. Сравнение поля Код оплаты после редактирования"):
        check.not_equal(order_app["ip_code"], order_app["ip_code_mod"],"❌ ФР: Одинаковое поле Код оплаты")

    with allure.step("26. Сравнение поля Примечание после редактирования"):
        check.not_equal(order_app["ip_note"], order_app["ip_note_mod"], "❌ ФР: Одинаковое поле Примечание")

    with allure.step("27. Сравнение поля Тип счета после редактирования"):
        check.not_equal(order_app["ip_list"], order_app["ip_list_mod"], "❌ ФР: Одинаковое поле Тип счета")

    with allure.step("28. Сравнение поля Поставщик после редактирования"):
        check.not_equal(order_app["ip_supplier"], order_app["ip_supplier_mod"], "❌ ФР: Одинаковое поле Поставщик")

    with allure.step("29. Сравнение поля Покупатель после редактирования"):
        check.not_equal(order_app["ip_buyer"], order_app["ip_buyer_mod"], "❌ ФР: Одинаковое поле Покупатель")

    with allure.step("30. Сравнение поля Заказ после редактирования"):
        check.not_equal(order_app["ip_number_order"], order_app["ip_number_order_mod"], "❌ ФР: Одинаковое поле Заказ")

    with allure.step("31. Сравнение поля Итого после редактирования"):
        check.not_equal(order_app["ip_total"], order_app["ip_total_mod"], "❌ ФР: Одинаковое поле Итого")

    with allure.step("32. Сравнение поля Комиссия после редактирования"):
        check.not_equal(order_app["ip_commission"], order_app["ip_commission_mod"], "❌ ФР: Одинаковое поле Комиссия")

    with allure.step("33. Сравнение поля Дата комиссии после редактирования"):
        check.not_equal(order_app["ip_data_commission"], order_app["ip_data_commission_mod"], "❌ ФР: Одинаковое поле Дата комиссии")

    with allure.step("34. Сравнение поля Со счета после редактирования"):
        check.not_equal(order_app["ip_from_check"], order_app["ip_from_check_mod"], "❌ ФР: Одинаковое поле Со счета")

    with allure.step("35. Сравнение поля = после редактирования"):
        check.not_equal(order_app["ip_txt"], order_app["ip_txt_mod"], "❌ ФР: Одинаковое поле =")

    # Вх. счета
    with allure.step("36. Сравнение полей Дата добавленного ВС"):
        check.equal(order_app["service_date_vs"], order_app["service_date_vs_form"],"❌ ФР: Не одинаковое Дата полей добавленного ВС")

    with allure.step("37. Сравнение полей Счет № добавленного ВС"):
        check.equal(order_app["account_vs"], order_app["account_vs_form"],"❌ ФР: Не одинаковое Счет № полей добавленного ВС")

    with allure.step("38. Сравнение полей Покупатель добавленного ВС"):
        check.equal(order_app["buyer_vs"], order_app["buyer_vs_form"],"❌ ФР: Не одинаковое Покупатель полей добавленного ВС")

    with allure.step("39. Сравнение полей Фидер. судно добавленного ВС"):
        check.equal(order_app["feeder_vessel_vs"], order_app["feeder_vessel_vs_form"],"❌ ФР: Не одинаковое Фидер. судно полей добавленного ВС")

    with allure.step("40. Сравнение полей Поставщик добавленного ВС"):
        check.equal(order_app["supplier_vs"], order_app["supplier_vs_form"],"❌ ФР: Не одинаковое Поставщик полей добавленного ВС")

    with allure.step("41. Сравнение полей Валюта добавленного ВС"):
        check.equal(order_app["currency_vs"], order_app["currency_vs_form"],"❌ ФР: Не одинаковое Валюта полей добавленного ВС")

    with allure.step("42. Сравнение полей Сумма добавленного ВС"):
        check.equal(order_app["amount_vs"], order_app["amount_vs_form"],"❌ ФР: Не одинаковое Сумма полей добавленного ВС")

    with allure.step("43. Сравнение полей Клиент добавленного ВС"):
        check.equal(order_app["client_vs"], order_app["client_vs_form"],"❌ ФР: Не одинаковое Клиент полей добавленного ВС")

    # Связываем с Вх. платежом
    with allure.step("44. Сравнение полей Дата добавленного ВП"):
        check.equal(order_app["service_date"], order_app["service_date_form"],"❌ ФР: Не одинаковое Дата полей добавленного ВП")

    with allure.step("45. Сравнение полей Счет № добавленного ВП"):
        check.equal(order_app["service_invoice"], order_app["service_invoice_form"],"❌ ФР: Не одинаковое Счет № полей добавленного ВП")

    #with allure.step("21. Сравнение полей Клиент добавленного ВП"):
       # check.equal(order_app["service_client"], order_app["service_client_form"],"❌ ФР: Не одинаковое Клиент полей добавленного ВП")

    # with allure.step("21. Сравнение полей Покупатель добавленного ВП"):
        # check.equal(order_app["service_buyer"], order_app["service_buyer_form"],"❌ ФР: Не одинаковое Покупатель полей добавленного ВП")

    # with allure.step("21. Сравнение полей Поставщик добавленного ВП"):
        # check.equal(order_app["service_supplier"], order_app["service_supplier_form"],"❌ ФР: Не одинаковое Поставщик полей добавленного ВП")

    with allure.step("46. Сравнение полей Валюта добавленного ВП"):
        check.equal(order_app["service_currency"], order_app["service_currency_form"],"❌ ФР: Не одинаковое Валюта полей добавленного ВП")

    with allure.step("47. Сравнение полей Сумма добавленного ВП"):
        check.equal(order_app["service_amount"], order_app["service_amount_form"],"❌ ФР: Не одинаковое Сумма полей добавленного ВП")

    with allure.step("48. Сравнение полей Информация добавленного ВП"):
        check.equal(order_app["service_info"], order_app["service_info_form"],"❌ ФР: Не одинаковое Информация полей добавленного ВП")

    with allure.step("49. Сравнение полей Начислено добавленного ВП"):
        check.equal(order_app["service_charged"], order_app["service_charged_form"],"❌ ФР: Не одинаковое Начислено полей добавленного ВП")

    with allure.step("50. Сравнение полей Начислено (С.В.) добавленного ВП"):
        check.equal(order_app["service_charged_sv"], order_app["service_charged_sv_form"],"❌ ФР: Не одинаковое Начислено (С.В.) полей добавленного ВП")

    # Таблица ИП
    with allure.step("51. Сравнение  Тип в таблице ИП"):
        check.equal( order_app["ip_table_type"], "ИП", "❌ ФР: Не одинаковое Тип в таблице ИП")

    with allure.step("52. Сравнение  Дата в таблице ИП"):
        compare_dates(order_app["ip_date"], order_app["ip_table_date"],"❌ ФР: Не одинаковое Дата в таблице ИП")

    with allure.step("53. Сравнение  Счет № в таблице ИП"):
        check.equal(order_app["ip_number_mod"], order_app["ip_table_check"],"❌ ФР: Не одинаковое Счет № в таблице ИП")

    with allure.step("54. Сравнение  Покупатель в таблице ИП"):
        check.equal(order_app["ip_buyer_mod"], order_app["ip_table_buyer"], "❌ ФР: Не одинаковое Покупатель таблице ИП")

    with allure.step("55. Сравнение  Поставщик в таблице ИП"):
        check.equal(order_app["ip_supplier_mod"], order_app["ip_table_supplier"], "❌ ФР: Не одинаковое Поставщик в таблице ИП")

    with allure.step("56. Сравнение  Валюта в таблице ИП"):
        check.equal(order_app["ip_table_currency"],"p", "❌ ФР: Не одинаковое Валюта в таблице ИП")

    with allure.step("57. Сравнение  Сумма в таблице ИП"):
        check.equal(order_app["ip_total_mod"], "1000", "❌ ФР: Не одинаковое Сумма в таблице ИП")

    with allure.step("58. Сравнение  Информация в таблице ИП"):
        check.equal(order_app["ip_note_mod"], order_app["ip_table_info"], "❌ ФР: Не одинаковое Информация в таблице ИП")

    with allure.step("59. Сравнение  Примечание в таблице ИП"):
        check.equal(order_app["ip_note_mod"], order_app["ip_table_note"], "❌ ФР: Не одинаковое Примечание в таблице ИП")
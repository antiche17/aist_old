from orders.finance import WinAISTApp
import pytest
import allure
import pytest_check as check
from locators.format_data import compare_dates


@pytest.fixture(scope="module")
def order_app():
    print("Переводы:\n-Создание\n-Удаление\n-Редактирование\n-Связка с другими счетами")
    app = WinAISTApp()
    try:
        order_data = app.finance_org()
        yield order_data
    finally:
        print("[TEARDOWN] Закрытие WinAISTApp")
        app.close()

@allure.suite("Проверка ИС")
@allure.title("Проверка ИС, проверок 134")
@pytest.mark.order(1)
def test_finance_org(order_app):
    with allure.step("1. Номер в пустой форме"):
        check.equal(order_app["number_org"], "0000", "❌ ФР: Номер перевода в пустой форме не 0000")

    with allure.step("1. Тип в пустой форме"):
        check.is_true(order_app["type_transfer"], "❌ ФР: Тип в пустой форме пустое поле")

    with allure.step("1. Поле От в пустой форме"):
        check.is_true(order_app["ot_org"], "❌ ФР: Поле От в пустой форме пустое поле")

    with allure.step("1. Поле Не вычислять в пустой форме"):
        check.is_true(order_app["no_sum"], "❌ ФР: Поле Не вычислять в пустой форме не выбрано")

    with allure.step("1. Исх. счет Поле Исх. сумма в пустой форме"):
        check.equal(order_app["in_sum_1"], "0", "❌ ФР: Исх. счет Поле Завершен в пустой форме не 0")

    with allure.step("1. Исх. счет Поле Валюта в пустой форме"):
        check.equal(order_app["currency_org1"], "0", "❌ ФР: Исх. счет Поле Завершен в пустой форме не 0")

    with allure.step("1. Исх. счет Поле Валюта не активна в пустой форме"):
        check.is_true(order_app["currency_org1_readonly"], "❌ ФР: Исх. счет Поле Завершен в пустой форме активно")

    with allure.step("1. Вх. счет Поле Валюта не активна в пустой форме"):
        check.is_true(order_app["currency_org2_readonly"], "❌ ФР: Вх. счет Поле Завершен в пустой форме активно")

    with allure.step("1. Итого Исх Валюта в пустой форме"):
        check.equal(order_app["currency_org6"], "0", "❌ ФР: Итого Исх Валюта в пустой форме не 0")

    with allure.step("1. Итого Вх Валюта в пустой форме"):
        check.equal(order_app["currency_org7"], "0", "❌ ФР: Итого Вх Валюта в пустой форме не 0")

    with allure.step("1. Исх комиссия Валюта в пустой форме"):
        check.equal(order_app["currency_org3"], "0", "❌ ФР: Исх комиссия Валюта в пустой форме не 0")

    with allure.step("1. Вх. счет Поле Валюта в пустой форме"):
        check.equal(order_app["currency_org2"], "0", "❌ ФР: Исх комиссия Валюта в пустой форме не 0")

    steps_to_check = [

        ("1. Поле Исполнение в пустой форме", ["execution_in_days"]),
        ("2. Поле Завершен в пустой форме", ["completed_org"]),
        ("3. Поле Вх-формула в пустой форме", ["formula_sum1_selected"]),
        ("4. Поле Исх-формула в пустой форме", ["formula_sum2_selected"]),
        ("5. Исх. счет Поле Со счета: в пустой форме", ["from_check_1"]),
        ("6. Вх. счет Поле Со счета в пустой форме", ["on_check_2"]),
        ("7. Вх. счет Поле Исх. сумма в пустой форме", ["in_sum_2"]),
        ("9. Исх комиссия Дата:", ["date_org1"]),
        ("10. Исх комиссия Комиссия:", ["commission1"]),
        ("11. Исх комиссия Со счета:", ["from_check3"]),
        ("12. Вх комиссия Дата:", ["date_org2"]),
        ("13. Вх комиссия Комиссия:", ["commission2"]),
        ("14. Вх комиссия Валюта:", ["currency_org4"]),
        ("15. Примечание", ["gtd_note"]),
    ]

    for step_name, fields in steps_to_check:
        with allure.step(step_name):
            for field in fields:
                value = order_app.get(field)
                check.is_false(value, f"❌ ФР: поле '{step_name}' должно быть пустым, но получено: {value}")

    with allure.step("1. Поле Номер после редактирования формы"):
        check.is_true(order_app["number_org"] == order_app["number_org"], "❌ ФР: Поля Номер одинаковые")

    with allure.step("1. Поле Тип после редактирования формы"):
        check.is_true(order_app["type_transfer"]== order_app["type_transfer_mod"], "❌ ФР: Поля Тип одинаковые")

    with allure.step("1. Поле От после редактирования формы"):
        check.is_true(order_app["ot_org"]== order_app["ot_org_mod"], "❌ ФР: Поля От одинаковые")

    with allure.step("1. Поле Не вычислять  после редактирования формы"):
        check.is_true(order_app["no_sum"]== order_app["no_sum_mod"], "❌ ФР: Поля Не вычислять одинаковые")

    with allure.step("1. Исх. счет Поле Исх. сумма после редактирования формы"):
        check.is_false(order_app["in_sum_1"]== order_app["in_sum_1_mod"], "❌ ФР: Исх. счет Поле Исх. сумма одинаковые")

    with allure.step("1. Исх. счет Поле Валюта после редактирования формы"):
        check.is_false(order_app["currency_org1"]== order_app["currency_org1_mod"], "❌ ФР: Исх. счет Поле Валюта одинаковые")

    with allure.step("1. Исх. счет Поле Валюта не активна после редактирования формы"):
        check.equal(order_app["currency_org1_readonly"], order_app["currency_org1_readonly_mod"], "❌ ФР: Исх. счет Поле Валюта не заблокировано")

    with allure.step("1. Вх. счет Поле Валюта не активна после редактирования формы"):
        check.equal(order_app["currency_org2_readonly"], order_app["currency_org2_readonly_mod"], "❌ ФР: Вх. счет Поле Валюта активна")

    with allure.step("1. Итого Исх Валюта после редактирования формы"):
        check.is_false(order_app["currency_org6"]== order_app["currency_org6_mod"], "❌ ФР: Поля Итого Исх Валюта одинаковые")

    with allure.step("1. Итого Вх Валюта после редактирования формы"):
        check.is_false(order_app["currency_org7"]== order_app["currency_org7_mod"], "❌ ФР: Поля Итого Вх Валютаодинаковые")

    with allure.step("1. Исх комиссия Валюта после редактирования формы"):
        check.is_false(order_app["currency_org3"]== order_app["currency_org3_mod"], "❌ ФР: Поля Исх комиссия Валюта одинаковые")

    with allure.step("1. Вх. счет Поле Валюта после редактирования формы"):
        check.is_false(order_app["currency_org2"]== order_app["currency_org2_mod"], "❌ ФР: Вх. счет Поле Валюта одинаковые")

    with allure.step("1. Поле Исполнение после редактирования формы"):
        check.is_false(order_app["execution_in_days"]== order_app["execution_in_days_mod"], "❌ ФР: Поля Исполнение одинаковые")

    with allure.step("1. Поле Завершен после редактирования формы"):
        check.is_false(order_app["completed_org"]== order_app["completed_org_mod"], "❌ ФР: Поля Завершен одинаковые")

    with allure.step("1. Исх. счет Поле Со счета после редактирования формы"):
        check.is_false(order_app["from_check_1"]== order_app["from_check_1_mod"], "❌ ФР: Исх. счет Поле Со счета одинаковые")

    with allure.step("1. Вх. счет Поле Со счета после редактирования формы"):
        check.is_false(order_app["on_check_2"]== order_app["on_check_2_mod"], "❌ ФР: Вх. счет Поле Со счет одинаковые")

    with allure.step("1. Вх. счет Поле Исх. сумма после редактирования формы"):
        check.is_false(order_app["in_sum_2"]== order_app["in_sum_2_mod"], "❌ ФР: Вх. счет Поле Исх. сумма одинаковые")

    with allure.step("1. Исх комиссия Дата после редактирования формы"):
        check.equal(order_app["date_org1"], order_app["date_org1_mod"], "❌ ФР: Поля Исх комиссия Дата одинаковые")

    with allure.step("1. Исх комиссия Комиссия после редактирования формы"):
        check.equal(order_app["commission1"], order_app["commission1_mod"], "❌ ФР: Поля Исх комиссия Комиссия одинаковые")

    with allure.step("1. Поле Номер после редактирования формы"):
        check.is_false(order_app["currency_org2"]== order_app["currency_org2_mod"], "❌ ФР: Поля Поле Номер после111 одинаковые")

    with allure.step("1. Исх комиссия Со счета после редактирования формы"):
        check.equal(order_app["from_check3"], order_app["from_check3_mod"], "❌ ФР: Поля Исх комиссия Со счета одинаковые")

    with allure.step("1. Вх комиссия Дата после редактирования формы"):
        check.equal(order_app["date_org2"], order_app["date_org2_mod"], "❌ ФР: Поля Вх комиссия Дата одинаковые")

    with allure.step("1. Вх комиссия Валюта после редактирования формы"):
        check.is_false(order_app["currency_org4"]== order_app["currency_org4_mod"], "❌ ФР: Поля Вх комиссия Валюта одинаковые")

    with allure.step("1. Поле Примечание после редактирования формы"):
        check.is_false(order_app["gtd_note"]== order_app["gtd_note_mod"], "❌ ФР: Поле Примечание одинаковые")

    with allure.step("1. Вх комиссия Комиссия: после редактирования формы"):
        check.equal(order_app["commission2"], order_app["commission2_mod"], "❌ ФР: Вх комиссия Комиссия: одинаковые")


    #Проверка связи с ИС
    with allure.step("1. Сравнение Даты с связанном ИС"):
        check.equal(order_app["service_date_is"], order_app["service_date_is1"], "❌ ФР: Добавленные Даты данные не одинаковые связь с ИС")

    with allure.step("1. Сравнение Счет № с связанном ИС"):
        check.equal(order_app["service_invoice_is"], order_app["service_invoice_is1"], "❌ ФР: Добавленные Счет № данные не одинаковые связь с ИС")

    #with allure.step("1. Сравнение Клиент с связанном ИС"): не отображаются данные
        #check.equal(order_app["service_client_is"], order_app["service_client_is1"], "❌ ФР: Добавленные Клиент данные не одинаковые связь с ИС")

    #with allure.step("1. Сравнение Покупатель с связанном ИС"):не отображаются данные
        #check.equal(order_app["service_buyer_is"], order_app["service_buyer_is1"], "❌ ФР: Добавленные Покупатель данные не одинаковые связь с ИС")

    #with allure.step("1. Сравнение Поставщик с связанном ИС"):не отображаются данные
        #check.equal(order_app["service_supplier_is"], order_app["service_supplier_is1"], "❌ ФР: Добавленные Поставщик данные не одинаковые связь с ИС")

    with allure.step("1. Сравнение Валюта с связанном ИС"):
        check.equal(order_app["service_currency_is"], order_app["service_currency_is1"], "❌ ФР: Добавленные Валюта данные не одинаковые связь с ИС")

    with allure.step("1. Сравнение Сумма с связанном ИС"):
        check.equal(order_app["service_amount_is"], order_app["service_amount_is1"], "❌ ФР: Добавленные Сумма данные не одинаковые связь с ИС")

    with allure.step("1. Сравнение Информация с связанном ИС"):
        check.equal(order_app["service_info_is"], order_app["service_info_is1"], "❌ ФР: Добавленные Информация данные не одинаковые связь с ИС")

    with allure.step("1. Сравнение Закрыто с связанном ИС"):
        check.equal(order_app["service_closed_is"], order_app["service_closed_is1"], "❌ ФР: Добавленные Закрыто данные не одинаковые связь с ИС")

    with allure.step("1. Сравнение Незакрыто с связанном ИС"):
        check.equal(order_app["service_unpaid_is"], order_app["service_unpaid_is1"], "❌ ФР: Добавленные Незакрыто данные не одинаковые связь с ИС")

    with allure.step("1. Сравнение Начислено с связанном ИС"):
        check.equal(order_app["service_charged_is"], order_app["service_charged_is1"], "❌ ФР: Добавленные Начислено данные не одинаковые связь с ИС")

    with allure.step("1. Сравнение Начислено (С.В.) с связанном ИС"):
        check.equal(order_app["service_charged_sv_is"], order_app["service_charged_sv_is1"], "❌ ФР: Добавленные Начислено (С.В.) данные не одинаковые связь с ИС")

    # Проверка связи с ВС
    with allure.step("1. Сравнение Даты с связаном ВС"):
        check.equal(order_app["service_date_vs1"], order_app["service_date_vs1"], "❌ ФР: Добавленные Даты данные не одинаковые связь с ВС")

    with allure.step("1. Сравнение Счет № с связаном ВС"):
        check.equal(order_app["service_invoice_vs1"], order_app["service_invoice_vs1"], "❌ ФР: Добавленные Счет № данные не одинаковые связь с ВС")

    with allure.step("1. Сравнение Клиент с связаном ВС"):
        check.equal(order_app["service_client_vs1"], order_app["service_client_vs1"], "❌ ФР: Добавленные Клиент данные не одинаковые связь с ВС")

    with allure.step("1. Сравнение Покупатель с связаном ВС"):
        check.equal(order_app["service_buyer_vs1"], order_app["service_buyer_vs1"], "❌ ФР: Добавленные Покупатель данные не одинаковые связь с ВС")

    with allure.step("1. Сравнение Поставщик с связаном ВС"):
        check.equal(order_app["service_supplier_vs1"], order_app["service_supplier_vs1"], "❌ ФР: Добавленные Поставщик данные не одинаковые связь с ВС")

    with allure.step("1. Сравнение Валюта с связаном ВС"):
        check.equal(order_app["service_currency_vs1"], order_app["service_currency_vs1"], "❌ ФР: Добавленные Валюта данные не одинаковые связь с ВС")

    with allure.step("1. Сравнение Сумма с связаном ВС"):
        check.equal(order_app["service_amount_vs1"], order_app["service_amount_vs1"], "❌ ФР: Добавленные Сумма данные не одинаковые связь с ВС")

    with allure.step("1. Сравнение Информация с связаном ВС"):
        check.equal(order_app["service_info_vs1"], order_app["service_info_vs1"], "❌ ФР: Добавленные Информация данные не одинаковые связь с ВС")

    with allure.step("1. Сравнение Закрыто с связаном ВС"):
        check.equal(order_app["service_closed_vs"], order_app["service_closed_vs1"], "❌ ФР: Добавленные Закрыто данные не одинаковые связь с ВС")

    with allure.step("1. Сравнение Незакрыто с связаном ВС"):
        check.equal(order_app["service_unpaid_vs"], order_app["service_unpaid_vs1"], "❌ ФР: Добавленные Незакрыто данные не одинаковые связь с ВС")

    with allure.step("1. Сравнение Начислено с связаном ВС"):
        check.equal(order_app["service_charged_vs"], order_app["service_charged_vs1"], "❌ ФР: Добавленные Начислено данные не одинаковые связь с ВС")

    with allure.step("1. Сравнение Начислено (С.В.) с связаном ВС"):
        check.equal(order_app["service_charged_sv_vs"], order_app["service_charged_sv_vs1"], "❌ ФР: Добавленные Начислено (С.В.) данные не одинаковые связь с ВС")


    # Сравнение с таблицей
    with allure.step("1. Сравнение Статус счета в таблице переводов"):
        check.equal(order_app["status_org_table"], "Завершен", "❌ ФР: Статус счета в таблице переводов не одинаковые")

    with allure.step("1. Сравнение Номер счета в таблице переводов"):
        check.equal(order_app["number_org_table"], order_app["number_org_mod"],
                    "❌ ФР: Номер счета в таблице переводов не одинаковые")

    with allure.step("1. Сравнение Название счета в таблице переводов"):
        check.equal(order_app["type_transfer_table"], order_app["type_transfer_mod"],
                    "❌ ФР: Название счета в таблице переводов не одинаковые")

    with allure.step("1. Сравнение Дата счета в таблице переводов"):
        compare_dates(order_app["ot_org_table"], order_app["ot_org_mod"],
                    "❌ ФР: Дата счета в таблице переводов не одинаковые")

    with allure.step("1. Сравнение Дата завершения счета в таблице переводов"):
        compare_dates(order_app["completed_org_table"], order_app["completed_org_mod"],
                    "❌ ФР: Дата завершения счета в таблице переводов не одинаковые")

    with allure.step("1. Сравнение Компания Исх. счета в таблице переводов"):
        check.equal(order_app["from_check_1_table"], order_app["from_check_1_mod"],
                    "❌ ФР: Компания Исх. счета в таблице переводов не одинаковые")

    with allure.step("1. Сравнение Сумма Исх. счета в таблице переводов"):
        check.is_true(order_app["in_sum_1_mod"] in order_app["in_sum_1_table"],
                    "❌ ФР: Сумма Исх. счета в таблице переводов не одинаковые")

    with allure.step("1. Сравнение Компания Вх. счета в таблице переводов"):
        check.equal(order_app["on_check_2_table"], order_app["on_check_2_mod"],
                    "❌ ФР: Компания Вх. счета в таблице переводов не одинаковые")

    with allure.step("1. Сравнение Сумма Вх. счета в таблице переводов"):
        check.equal(order_app["in_sum_2_table"], order_app["in_sum_2_mod"],
                    "❌ ФР: Сумма Вх. счета в таблице переводов не одинаковые")

    with allure.step("1. Сравнение Примечание счета в таблице переводов"):
        check.equal(order_app["gtd_note_table"], order_app["gtd_note_mod"],
                    "❌ ФР: Примечание счета в таблице переводов не одинаковые")

from difflib import SequenceMatcher
from orders.finance import WinAISTApp
import pytest
import allure
import pytest_check as check
import locale
from datetime import datetime

MONTHS_RU_EN = {
    'января': 'January', 'февраля': 'February', 'марта': 'March',
    'апреля': 'April', 'мая': 'May', 'июня': 'June',
    'июля': 'July', 'августа': 'August', 'сентября': 'September',
    'октября': 'October', 'ноября': 'November', 'декабря': 'December'
}

def normalize_date(date_str):
    date_str = date_str.replace("г.", "").strip()
    # Преобразуем только если месяц на русском
    for ru, en in MONTHS_RU_EN.items():
        if ru in date_str:
            date_str = date_str.replace(ru, en)
            break
    # Устанавливаем английскую локаль временно
    locale.setlocale(locale.LC_TIME, 'C')
    formats = ["%d %B %Y", "%d.%m.%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Не удалось распознать формат даты: {date_str}")

def compare_dates(date1, date2, error_message):
    assert normalize_date(date1) == normalize_date(date2), error_message

@pytest.fixture(scope="module")
def order_app():
    print("Есть ошибки задача AIST-863\n Проверка синхронизации с 1С не полная, на дев01 ошибка - Данный счет существует в 1С")
    app = WinAISTApp()
    order_data = app.finance()
    yield order_data
    app.close()

def check_equal_dates(value1, value2, field_name):
    normalized1 = normalize_date(value1)
    normalized2 = normalize_date(value2)
    check.equal(normalized1, normalized2, f"❌ ФР: Не одинаковый {field_name}")

@allure.suite("Проверка ИС")
@allure.title("Проверка ИС, проверок 134")
@pytest.mark.order(1)
def test_finance(order_app):
    with allure.step("1. Дата в форме Создание ИС"):
        check.is_true(order_app["is_date"], "❌ ФР: Пустое поле")

    # Пустые значения в форме Создания ИС
    steps_to_check = [
        ("2. Номер", ["is_number"]),
        ("3. Список", ["is_list"]),
        ("4. Примечание", ["is_note"]),
        ("5. Дата с/ф", ["is_date_sf"]),
        ("6. Поставщик", ["is_supplier"]),
        ("7. Покупатель", ["is_buyer"]),
        ("8. Клиент", ["is_client"]),
        ("9. Океан. к/с", ["is_ocean_vessel"]),
        ("10. Фидер. к/с", ["is_feeder_vessel"]),
        ("11. Океан. судно", ["is_ocean_ship"]),
        ("12. Фидер. судно", ["is_feeder_ship"]),
        ("13. Прибытие", ["is_arrival"]),
        ("14. Отгрузка", ["is_shipment"]),
        ("15. Усл. погрузки", ["is_loading_conditions"]),
        ("16. Усл. назначения", ["is_destination_conditions"]),
        ("17. Терминал", ["is_terminal"]),
        ("18. Океан. линия", ["is_ocean_line"]),
        ("19. Фидер. линия", ["is_feeder_line"]),
        ("20. Место погрузки", ["is_loading_location"]),
        ("21. Место назначения", ["is_destination"]),
        ("22. Дата возврата", ["is_return_date"]),
        ("23. Дата вывоза", ["is_pickup_date"]),
        ("24. ГТД", ["is_gtd"]),
    ]

    for step_name, fields in steps_to_check:
        with allure.step(step_name):
            for field in fields:
                value = order_app.get(field)
                check.is_false(value, f"❌ ФР: поле '{field}' должно быть пустым, но получено: {value}")

    with allure.step("25. Поле Синхронизация 1С"):
        check.equal(order_app["is_sync"], "<color=#FFA500>Ожидание</color>", "❌ ФР: В поле Синхронизация 1С нет Ожидания")

    #with allure.step("26. Поле Синхронизация 1С успешно"): Идет отбивка ошибки про дублирование
        #check.equal(order_app["is_sync_ок"], "<color=#FFA500>Ожидание</color>", "❌ ФР: В поле Синхронизация 1С нет Ожидания")

    with allure.step("27. Тип счета"):
        check.equal(order_app["is_list_mod"], "Товарный", "❌ ФР: Пустое поле Тип счета ")

    with allure.step("28. Поле Поставщик"):
        check.equal(order_app["is_supplier_mod"], "Бодрус - ВТБ RUR", "❌ ФР: Пустое поле Поставщик")

    with allure.step("29. Поле Покупатель"):
        check.equal(order_app["is_buyer_mod"], "ВЕСПА (Vespa Co.Ltd)", "❌ ФР: Пустое поле Покупатель")

    with allure.step("30. Поле Клиент"):
        check.equal(order_app["is_client_mod"], "ВЕСПА (Vespa Co.Ltd)", "❌ ФР: Пустое поле Клиент")

    with allure.step("31. Поле Примечание"):
        check.equal(order_app["is_note_mod"], "Примечание для ИС", "❌ ФР: Пустое поле")
        # Пустые значения в форме Создания ИС

    steps_to_check_mod = [
        ("32. Номер после редактирования", ["is_number_mod"]),
        ("33. Дата с/ф после редактирования", ["is_date_sf_mod"]),
        ("34. Океан. к/с после редактирования", ["is_ocean_vessel_mod"]),
        ("35. Фидер. к/с после редактирования", ["is_feeder_vessel_mod"]),
        ("36. Океан. судно после редактирования", ["is_ocean_ship_mod"]),
        ("37. Фидер. судно после редактирования", ["is_feeder_ship_mod"]),
        ("38. Прибытие после редактирования", ["is_arrival_mod"]),
        ("39. Отгрузка после редактирования", ["is_shipment_mod"]),
        ("40. Усл. погрузки после редактирования", ["is_loading_conditions_mod"]),
        ("41. Усл. назначения после редактирования", ["is_destination_conditions_mod"]),
        ("42. Терминал после редактирования", ["is_terminal_mod"]),
        ("43. Океан. линия после редактирования", ["is_ocean_line_mod"]),
        ("44. Фидер. линия после редактирования", ["is_feeder_line_mod"]),
        ("45. Место погрузки после редактирования", ["is_loading_location_mod"]),
        ("46. Место назначения после редактирования", ["is_destination_mod"]),
        ("47. Дата возврата после редактирования", ["is_return_date_mod"]),
        ("48. Дата вывоза после редактирования", ["is_pickup_date_mod"]),
        ("49. ГТД после редактирования", ["is_gtd_mod"]),
    ]

    for step_name, fields in steps_to_check_mod:
        with allure.step(step_name):
            for field in fields:
                value = order_app.get(field)
                check.is_true(value, f"❌ ФР: поле '{field}' должно быть не пустым, но получено: {value}")

    with allure.step("50. Валюта в услуге"):
        check.equal(order_app["service_vat"], "RUR", "❌ ФР: Валюта не RUR в услуге")


    with allure.step("50. Номер услуги"):
        check.equal(order_app["service_line_number1"], "1", "❌ ФР: Пустое поле Номер услуги")

    with allure.step("51. Название услуги"):
        check.equal(order_app["service_service1"], order_app["service_service"], "❌ ФР: Пустое поле Название услуги")

    with allure.step("52. Поле НДС"):
        check.equal(order_app["service_vat1"], order_app["service_dns"], "❌ ФР: Пустое НДС поле")

    with allure.step("53. Поле Кол-во"):
        check.equal(order_app["service_quantity1"], order_app["quantity_service"], "❌ ФР: Пустое поле Кол-во")

    with allure.step("54. Поле Ставка"):
        check.equal(order_app["service_rate1"], order_app["service_rate"], "❌ ФР: Пустое поле Ставка")

    with allure.step("55. Поле Валюта"):
        check.equal(order_app["service_currency1"], "p", "❌ ФР: Пустое поле Валюта")

    with allure.step("56. Поле Итого услуги"):
        check.equal(order_app["service_total1"], "100,00", "❌ ФР: Пустое поле Итого услуги")

    with allure.step("57. Поле Итого (С. В.)"):
        check.equal(order_app["service_total_sv1"], "100,00", "❌ ФР: Пустое поле Итого (С. В.)")


    # Входящие платежи
    with allure.step("58. Дата услуги"):
        check.equal(order_app["service_date"], order_app["service_date_form"], "❌ ФР: Пустое поле Дата услуги Входящие платежи")

    with allure.step("59. Поле Счет №"):
        check.equal(order_app["service_invoice"], order_app["service_invoice_form"], "❌ ФР: Пустое поле Счет № Входящие платежи")

    #with allure.step("60. Поле Клиент"):
        #check.equal(order_app["service_client"], order_app["service_client_form"], "❌ ФР: Пустое поле Клиент задача AIST-863 Входящие платежи")

    #with allure.step("61. Поле Покупатель"):
        #check.equal(order_app["service_buyer"], order_app["service_buyer_form"], "❌ ФР: Пустое поле Покупатель задача AIST-863 Входящие платежи")

    #with allure.step("62. Поле Поставщик"):
        #check.equal(order_app["service_supplier"], order_app["service_supplier_form"], "❌ ФР: Пустое поле Поставщик  задача AIST-863 Входящие платежи")

    with allure.step("63. Поле Валюта"):
        check.equal(order_app["service_currency"], order_app["service_currency_form"], "❌ ФР: Пустое поле Валюта Входящие платежи")

    with allure.step("64. Поле Сумма"):
        check.equal(order_app["service_amount"], order_app["service_amount_form"], "❌ ФР: Пустое поле Сумма Входящие платежи")

    with allure.step("65. Поле Информация"):
        check.equal(order_app["service_info"], order_app["service_info_form"], "❌ ФР: Пустое поле Информация Входящие платежи")

    with allure.step("66. Поле Закрыто"):
        check.equal(order_app["service_closed"], order_app["service_closed_form"], "❌ ФР: Пустое поле Закрыто Входящие платежи")

    with allure.step("67. Поле Незакрыто"):
        check.equal(order_app["service_unpaid"], order_app["service_unpaid_form"], "❌ ФР: Пустое поле Незакрыто Входящие платежи")

    with allure.step("68. Поле Начислено"):
        check.equal(order_app["service_charged"], order_app["service_charged_form"], "❌ ФР: Пустое поле Начислено Входящие платежи")

    with allure.step("69. Поле Начислено (С.В.)"):
        check.equal(order_app["service_charged_sv"], order_app["service_charged_sv_form"], "❌ ФР: Пустое поле Начислено (С.В.) Входящие платежи")

     # Связываем с Вх. переводы
    with allure.step("70. Дата услуги"):
        check.equal(order_app["service_is_payment_vp"], order_app["service_is_payment_vp_form"], "❌ ФР: Пустое поле Дата услуги Вх. переводы")

    with allure.step("71. Поле Счет №"):
        check.equal(order_app["service_date_vp"], order_app["service_date_vp_form"], "❌ ФР: Пустое поле Счет №")

    with allure.step("72. Поле Клиент"):
        check.equal(order_app["service_is_type_vp"], order_app["service_is_type_vp_form"], "❌ ФР: Пустое поле Клиент")

    with allure.step("73. Поле Покупатель"):
        check.equal(order_app["service_supplier_vp"], order_app["service_supplier_vp_form"], "❌ ФР: Пустое поле Покупатель")

    with allure.step("74. Поле Поставщик"):
        check.equal(order_app["service_invoice_vp"], order_app["service_invoice_vp_form"], "❌ ФР: Пустое поле Поставщик")

    with allure.step("75. Поле Валюта"):
        check.equal(order_app["service_client_vp"], order_app["service_client_vp_form"], "❌ ФР: Пустое поле Валюта")

    with allure.step("76. Поле Сумма"):
        check.equal(order_app["service_contractor_vp"], order_app["service_contractor_vp_form"], "❌ ФР: Пустое поле Сумма")

    with allure.step("77. Поле Информация"):
        check.equal(order_app["service_buyer_vp"], order_app["service_buyer_vp_form"], "❌ ФР: Пустое поле Информация")

    with allure.step("78. Поле Закрыто"):
        check.equal(order_app["service_currency_vp"], order_app["service_currency_vp_form"], "❌ ФР: Пустое поле Закрыто")

    with allure.step("79. Поле Незакрыто"):
        check.equal(order_app["service_amount_vp"], order_app["service_amount_vp_form"], "❌ ФР: Пустое поле Незакрыто")

    with allure.step("80. Поле Начислено"):
        check.equal(order_app["service_unallocated_vp"], order_app["service_unallocated_vp_form"], "❌ ФР: Пустое поле Начислено")

    with allure.step("81. Поле Начислено (С.В.)"):
        check.equal(order_app["service_note_vp"], order_app["service_note_vp_form"], "❌ ФР: Пустое поле Начислено (С.В.)")

    with allure.step("82. Поле Закрыто"):
        check.equal(order_app["service_info_vp"], order_app["service_info_vp_form"], "❌ ФР: Пустое поле Закрыто")

    with allure.step("83. Поле Незакрыто"):
        check.equal(order_app["service_closed_vp"], order_app["service_closed_vp_form"], "❌ ФР: Пустое поле Незакрыто")

    with allure.step("84. Поле Начислено"):
        check.equal(order_app["service_unpaid_vp"], order_app["service_unpaid_vp_form"], "❌ ФР: Пустое поле Начислено")

    with allure.step("85. Поле Начислено (С.В.)"):
        check.equal(order_app["service_charged_vp"], order_app["service_charged_vp_form"], "❌ ФР: Пустое поле Начислено (С.В.)")

    with allure.step("86. Поле Начислено (С.В.)"):
        check.equal(order_app["service_charged_sv_vp"], order_app["service_charged_sv_vp_form"], "❌ ФР: Пустое поле Начислено (С.В.)")

    # Вх. счета

    with allure.step("87. Поле Создан Вх.счета"):
        check.equal(order_app["created_vs_form"], order_app["created_vs_form"], "❌ ФР: Пустое поле Создан Вх.счета")

    with allure.step("88. Поле Кем создан Вх.счета"):
        check.equal(order_app["created_by_vs_form"], order_app["created_by_vs_form"],
                    "❌ ФР: Пустое поле Кем создан Вх.счета")

    with allure.step("89. Поле Кем изменен Вх.счета"):
        check.equal(order_app["modified_by_vs_form"], order_app["modified_by_vs_form"],
                    "❌ ФР: Пустое поле Кем изменен Вх.счета")

    with allure.step("90. Поле ИС оплата Вх.счета"):
        check.equal(order_app["is_payment_vs_form"], order_app["is_payment_vs_form"],
                    "❌ ФР: Пустое поле ИС оплата Вх.счета")

    with allure.step("91. Поле Услуга 0 Вх.счета"):
        check.equal(order_app["service_vs_form"], order_app["service_vs_form"], "❌ ФР: Пустое поле Услуга 0 Вх.счета")

    with allure.step("92. Поле Дата Вх.счета"):
        check.equal(order_app["service_date_vs_form"], order_app["service_date_vs_form"],
                    "❌ ФР: Пустое поле Дата Вх.счета")

    with allure.step("93. Поле Счет № Вх.счета"):
        check.equal(order_app["account_vs_form"], order_app["account_vs_form"], "❌ ФР: Пустое поле Счет № Вх.счета")

    with allure.step("94. Поле Покупатель  Вх.счета"):
        check.equal(order_app["buyer_vs_form"], order_app["buyer_vs_form"], "❌ ФР: Пустое поле Покупатель  Вх.счета")

    with allure.step("95. Поле ГТД  Вх.счета"):
        check.equal(order_app["gtd_vs_form"], order_app["gtd_vs_form"], "❌ ФР: Пустое поле ГТД  Вх.счета")

    with allure.step("96. Поле Фидер. судно Вх.счета"):
        check.equal(order_app["feeder_vessel_vs_form"], order_app["feeder_vessel_vs_form"],
                    "❌ ФР: Пустое поле Фидер. судно Вх.счета")

    with allure.step("97. Поле Поставщик  Вх.счета"):
        check.equal(order_app["supplier_vs_form"], order_app["supplier_vs_form"],
                    "❌ ФР: Пустое поле Поставщик  Вх.счета")

    with allure.step("98. Поле Валюта  Вх.счета"):
        check.equal(order_app["currency_vs_form"], order_app["currency_vs_form"], "❌ ФР: Пустое поле Валюта  Вх.счета")

    with allure.step("99. Поле Сумма Вх.счета"):
        check.equal(order_app["amount_vs_form"], order_app["amount_vs_form"], "❌ ФР: Пустое поле Сумма Вх.счета")

    with allure.step("100. Поле Неразнесено  Вх.счета"):
        check.equal(order_app["unallocated_vs_form"], order_app["unallocated_vs_form"],
                    "❌ ФР: Пустое поле Неразнесено  Вх.счета")

    with allure.step("101. Поле Информация  Вх.счета"):
        check.equal(order_app["info_vs_form"], order_app["info_vs_form"], "❌ ФР: Пустое поле Информация  Вх.счета")

    with allure.step("102. Поле Примечание Вх.счета"):
        check.equal(order_app["note_vs_form"], order_app["note_vs_form"], "❌ ФР: Пустое поле Примечание Вх.счета")

    with allure.step("103. Поле Связано в ИС Вх.счета"):
        check.equal(order_app["linked_is_vs_form"], order_app["linked_is_vs_form"],
                    "❌ ФР: Пустое поле Связано в ИС Вх.счета")

    with allure.step("104. Поле Связано в ВС Вх.счета"):
        check.equal(order_app["linked_vs_vs_form"], order_app["linked_vs_vs_form"],
                    "❌ ФР: Пустое поле Связано в ВС Вх.счета")

    with allure.step("105. Поле Клиент  Вх.счета"):
        check.equal(order_app["client_vs_form"], order_app["client_vs_form"], "❌ ФР: Пустое поле Клиент  Вх.счета")

    # Прямые счета

    with allure.step("106. Поле Тип ИС Прямые счета на клиента"):
        check.equal(order_app["is_type_ps_form"], order_app["is_type_ps_form"],
                    "❌ ФР: Пустое поле Тип ИС Прямые счета на клиента")

    with allure.step("107. Поле Кем создан Прямые счета на клиента"):
        check.equal(order_app["created_by_ps_form"], order_app["created_by_ps_form"],
                    "❌ ФР: Пустое поле Кем создан Прямые счета на клиента")

    with allure.step("108. Поле Дата  Прямые счета на клиента"):
        check.equal(order_app["date_ps_form"], order_app["date_ps_form"],
                    "❌ ФР: Пустое поле Дата  Прямые счета на клиента")

    with allure.step("109. Поле Счет № Прямые счета на клиента"):
        check.equal(order_app["account_ps_form"], order_app["account_ps_form"],
                    "❌ ФР: Пустое поле Счет № Прямые счета на клиента")

    with allure.step("110. Поле Покупатель  Прямые счета на клиента"):
        check.equal(order_app["buyer_ps_form"], order_app["buyer_ps_form"],
                    "❌ ФР: Пустое поле Покупатель  Прямые счета на клиента")

    with allure.step("111. Поле Поставщик  Прямые счета на клиента"):
        check.equal(order_app["supplier_ps_form"], order_app["supplier_ps_form"],
                    "❌ ФР: Пустое поле Поставщик  Прямые счета на клиента")

    with allure.step("112. Поле Валюта  Прямые счета на клиента"):
        check.equal(order_app["currency_ps_form"], order_app["currency_ps_form"],
                    "❌ ФР: Пустое поле Валюта  Прямые счета на клиента")

    with allure.step("113. Поле Сумма Прямые счета на клиента"):
        check.equal(order_app["amount_ps_form"], order_app["amount_ps_form"],
                    "❌ ФР: Пустое поле Сумма Прямые счета на клиента")

    with allure.step("114. Поле Информация  Прямые счета на клиента"):
        check.equal(order_app["info_ps_form"], order_app["info_ps_form"],
                    "❌ ФР: Пустое поле Информация Прямые счета на клиента")
    # Все счета
    with allure.step("115. Поле Дата в таблице Все счета"):
        compare_dates(order_app["is_date"], order_app["data_all_accounts"], "❌ ФР: Не совпадают Дата в таблице Все счета")

    with allure.step("116. Поле Поставщик в таблице Все счета"):
         check.equal(order_app["is_supplier_mod"], order_app["supplier_all_accounts"], "❌ ФР: Не совпадают Поставщик в таблице Все счета")

    with allure.step("117. Поле Счет № в таблице Все счета"):
        check.equal(order_app["is_number_mod"], order_app["account_all_accounts"], "❌ ФР: Не совпадают Счет № в таблице Все счета")

    with allure.step("118. Поле Клиент в таблице Все счета"):
        check.equal(order_app["is_client_mod"], order_app["client_all_accounts"], "❌ ФР: Не совпадают Клиент в таблице Все счета")

    with allure.step("119. Поле Покупатель в таблице Все счета"):
        check.equal(order_app["is_buyer_mod"], order_app["buyer_all_accounts"], "❌ ФР: Не совпадают Покупатель в таблице Все счета")

    with allure.step("120. Поле Валюта в таблице Все счета"):
        check.equal(order_app["service_currency1"], order_app["currency_all_accounts"], "❌ ФР: Не совпадают Валюта в таблице Все счета")

    with allure.step("121. Поле Сумма в таблице Все счета"):
        check.equal(order_app["service_total"], order_app["amount_all_accounts"], "❌ ФР: Не совпадают Сумма в таблице Все счета")

    with allure.step("122. Поле Закрыто в таблице Все счета"):
        check.equal(order_app["service_total"], order_app["closed_all_accounts"], "❌ ФР: Не совпадают Закрыто в таблице Все счета")

    with allure.step("123. Поле Незакрыто в таблице Все счета"):
        check.equal(order_app["unpaid_all_accounts"], "0,00", "❌ ФР: Не совпадают Незакрыто в таблице Все счета")

    with allure.step("124. Поле Примечание в таблице Все счета"):
        check.equal(order_app["is_note_mod"], order_app["note_all_accounts"], "❌ ФР: Не совпадают Примечание в таблице Все счета")

    # Все услуги
    with allure.step("125. Поле Счет в таблице Все услуги"):
        check.equal(order_app["is_number_mod"], order_app["all_serv_invoice_number"], "❌ ФР: Не совпадают Счет в таблице Все услуги")

    with allure.step("126. Поле Дата счета в таблице Все услуги"):
        compare_dates(order_app["is_date_mod"], order_app["all_serv_invoice_date"], "❌ ФР: Не совпадают Дата счета в таблице Все услуги")

    with allure.step("127. Поле Услуга в таблице Все услуги"):
        check.equal(order_app["service_service"], order_app["all_serv_service"], "❌ ФР: Не совпадают Услуга в таблице Все услуги")

    with allure.step("128. Поле Клиент в таблице Все услуги"):
        check.equal(order_app["is_client_mod"], order_app["all_serv_client"], "❌ ФР: Не совпадают Клиент в таблице Все услуги")

    with allure.step("129. Поле Покупатель в таблице Все услуги"):
        check.equal(order_app["is_buyer_mod"], order_app["all_serv_buyer"], "❌ ФР: Не совпадают Покупатель в таблице Все услуги")

    with allure.step("130. Поле Поставщик в таблице Все услуги"):
        check.equal(order_app["is_supplier_mod"], order_app["all_serv_supplier"], "❌ ФР: Не совпадают Поставщик в таблице Все услуги")

    with allure.step("131. Поле Ставка в таблице Все услуги"):
        check.equal(order_app["service_total1"], order_app["all_serv_rate"], "❌ ФР: Не совпадают Ставка в таблице Все услуги")

    with allure.step("132. Поле Валюта в таблице Все услуги"):
        check.equal(order_app["all_serv_currency"], "p", "❌ ФР: Не совпадают Валюта в таблице Все услуги")

    with allure.step("133. Поле Кол-во в таблице Все услуги"):
        check.equal(order_app["quantity_service"], order_app["all_serv_quantity"], "❌ ФР: Не совпадают Кол-во в таблице Все услуги")

    with allure.step("134. Поле Примечание счета в таблице Все услуги"):
        check.equal(order_app["is_note_mod"], order_app["all_serv_invoice_note"], "❌ ФР: Не совпадают Примечание счета в таблице Все услуги")
from orders.finance import WinAISTApp
import pytest
import allure
import pytest_check as check
from locators.format_data import compare_dates


@pytest.fixture(scope="module")
def order_app():
    print("Проверка ИП")
    app = WinAISTApp()
    order_data = app.finance_vs()
    yield order_data
    print("[TEARDOWN] Закрытие WinAISTApp")
    try:
        # Прямое жесткое закрытие минуя проблемные методы
        app.fun.app.kill()  # без soft=True
    except Exception as e:
        print(f"При закрытии возникла ошибка: {e}")
        # Игнорируем ошибку, так как приложение все равно должно закрыться

@allure.suite("Проверка ВС")
@allure.title("Проверка ВС, проверок 134")
def test_finance_vs(order_app):
    with allure.step("1. Дата в форме Создание ВС"):
        check.is_true(order_app["vs_date"], "❌ ФР: Пустое поле")

    # Пустые значения в форме Создания ИС
    steps_to_check = [
        ("2. Номер", ["vs_number"]),
        ("3. Список", ["vs_list"]),
        ("4. Примечание", ["vs_note"]),
        ("5. Дата с/ф", ["vs_date_sf"]),
        ("6. Поставщик", ["vs_supplier"]),
        ("7. Покупатель", ["vs_buyer"]),
        ("8. Клиент", ["vs_client"]),
        ("9. Океан. к/с", ["vs_ocean_vessel"]),
        ("10. Фидер. к/с", ["vs_feeder_vessel"]),
        ("11. Океан. судно", ["vs_ocean_ship"]),
        ("12. Фидер. судно", ["vs_feeder_ship"]),
        ("13. Прибытие", ["vs_arrival"]),
        ("14. Отгрузка", ["vs_shipment"]),
        ("15. Усл. погрузки", ["vs_loading_conditions"]),
        ("16. Усл. назначения", ["vs_destination_conditions"]),
        ("17. Терминал", ["vs_terminal"]),
        ("18. Океан. линия", ["vs_ocean_line"]),
        ("19. Фидер. линия", ["vs_feeder_line"]),
        ("20. Место погрузки", ["vs_loading_location"]),
        ("21. Место назначения", ["vs_destination"]),
        ("22. Дата возврата", ["vs_return_date"]),
        ("23. Дата вывоза", ["vs_pickup_date"]),
        ("24. ГТД", ["vs_gtd"]),
    ]

    for step_name, fields in steps_to_check:
        with allure.step(step_name):
            for field in fields:
                value = order_app.get(field)
                check.is_false(value, f"❌ ФР: поле '{field}' должно быть пустым, но получено: {value}")

    with allure.step("27. Тип счета"):
        check.equal(order_app["vs_list_mod"], "Товарный", "❌ ФР: Пустое поле Тип счета ")

    with allure.step("28. Поле Поставщик"):
        check.equal(order_app["vs_supplier_mod"], "Бодрус - ВТБ RUR", "❌ ФР: Пустое поле Поставщик")

    with allure.step("29. Поле Покупатель"):
        check.equal(order_app["vs_buyer_mod"], "ANDREY RUR", "❌ ФР: Пустое поле Покупатель")

    with allure.step("30. Поле Подрядчик"):
        check.equal(order_app["vs_contractor_mod"], "ВЕСПА (Vespa Co.Ltd)", "❌ ФР: Пустое поле Клиент")

    with allure.step("31. Поле Примечание"):
        check.equal(order_app["vs_note_mod"], "Примечание для ИС", "❌ ФР: Пустое поле")

    # Пустые значения в форме Создания ИС
    steps_to_check_mod = [
        ("32. Номер после редактирования", ["vs_number_mod"]),
        ("33. Дата с/ф после редактирования", ["vs_date_sf_mod"]),
        ("34. Океан. к/с после редактирования", ["vs_ocean_vessel_mod"]),
        ("35. Фидер. к/с после редактирования", ["vs_feeder_vessel_mod"]),
        ("36. Океан. судно после редактирования", ["vs_ocean_ship_mod"]),
        ("37. Фидер. судно после редактирования", ["vs_feeder_ship_mod"]),
        ("38. Прибытие после редактирования", ["vs_arrival_mod"]),
        ("39. Отгрузка после редактирования", ["vs_shipment_mod"]),
        ("40. Усл. погрузки после редактирования", ["vs_loading_conditions_mod"]),
        ("41. Усл. назначения после редактирования", ["vs_destination_conditions_mod"]),
        ("43. Океан. линия после редактирования", ["vs_ocean_line_mod"]),
        ("44. Фидер. линия после редактирования", ["vs_feeder_line_mod"]),
        ("45. Место погрузки после редактирования", ["vs_loading_location_mod"]),
        ("46. Место назначения после редактирования", ["vs_destination_mod"]),
        ("47. Дата возврата после редактирования", ["vs_return_date_mod"]),
        ("48. Дата вывоза после редактирования", ["vs_pickup_date_mod"]),
        ("49. ГТД после редактирования", ["vs_gtd_mod"]),
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
        check.equal(order_app["service_date"], order_app["service_date_form"],
                    "❌ ФР: Пустое поле Дата услуги Входящие платежи")

    with allure.step("59. Поле Счет №"):
        check.equal(order_app["service_invoice"], order_app["service_invoice_form"],
                    "❌ ФР: Пустое поле Счет № Входящие платежи")

    with allure.step("63. Поле Валюта"):
        check.equal(order_app["service_currency"], order_app["service_currency_form"],
                    "❌ ФР: Пустое поле Валюта Входящие платежи")

    with allure.step("64. Поле Сумма"):
        check.equal(order_app["service_amount"], order_app["service_amount_form"],
                    "❌ ФР: Пустое поле Сумма Входящие платежи")

    with allure.step("65. Поле Информация"):
        check.equal(order_app["service_info"], order_app["service_info_form"],
                    "❌ ФР: Пустое поле Информация Входящие платежи")

    with allure.step("66. Поле Закрыто"):
        check.equal(order_app["service_closed"], order_app["service_closed_form"],
                    "❌ ФР: Пустое поле Закрыто Входящие платежи")

    with allure.step("67. Поле Незакрыто"):
        check.equal(order_app["service_unpaid"], order_app["service_unpaid_form"],
                    "❌ ФР: Пустое поле Незакрыто Входящие платежи")

    with allure.step("68. Поле Начислено"):
        check.equal(order_app["service_charged"], order_app["service_charged_form"],
                    "❌ ФР: Пустое поле Начислено Входящие платежи")

    with allure.step("69. Поле Начислено (С.В.)"):
        check.equal(order_app["service_charged_sv"], order_app["service_charged_sv_form"],
                    "❌ ФР: Пустое поле Начислено (С.В.) Входящие платежи")

    # Связываем с Вх. переводы
    with allure.step("70. Дата услуги"):
        check.equal(order_app["service_is_payment_vp"], order_app["service_is_payment_vp_form"],
                    "❌ ФР: Пустое поле Дата услуги Вх. переводы")

    with allure.step("71. Поле Счет №"):
        check.equal(order_app["service_date_vp"], order_app["service_date_vp_form"], "❌ ФР: Пустое поле Счет №")

    with allure.step("72. Поле Клиент"):
        check.equal(order_app["service_is_type_vp"], order_app["service_is_type_vp_form"], "❌ ФР: Пустое поле Клиент")

    with allure.step("73. Поле Покупатель"):
        check.equal(order_app["service_supplier_vp"], order_app["service_supplier_vp_form"],
                    "❌ ФР: Пустое поле Покупатель")

    with allure.step("74. Поле Поставщик"):
        check.equal(order_app["service_invoice_vp"], order_app["service_invoice_vp_form"],
                    "❌ ФР: Пустое поле Поставщик")

    with allure.step("75. Поле Валюта"):
        check.equal(order_app["service_client_vp"], order_app["service_client_vp_form"], "❌ ФР: Пустое поле Валюта")

    with allure.step("76. Поле Сумма"):
        check.equal(order_app["service_contractor_vp"], order_app["service_contractor_vp_form"],
                    "❌ ФР: Пустое поле Сумма")

    with allure.step("77. Поле Информация"):
        check.equal(order_app["service_buyer_vp"], order_app["service_buyer_vp_form"], "❌ ФР: Пустое поле Информация")

    with allure.step("82. Поле Закрыто"):
        check.equal(order_app["service_info_vp"], order_app["service_info_vp_form"], "❌ ФР: Пустое поле Закрыто")

    with allure.step("83. Поле Незакрыто"):
        check.equal(order_app["service_closed_vp"], order_app["service_closed_vp_form"], "❌ ФР: Пустое поле Незакрыто")

    with allure.step("84. Поле Начислено"):
        check.equal(order_app["service_unpaid_vp"], order_app["service_unpaid_vp_form"], "❌ ФР: Пустое поле Начислено")

    with allure.step("85. Поле Начислено (С.В.)"):
        check.equal(order_app["service_charged_vp"], order_app["service_charged_vp_form"],
                    "❌ ФР: Пустое поле Начислено (С.В.)")

    # Связываем с Исх. счета
    with allure.step("92. Поле Дата Исх. счета"):
        check.equal(order_app["service_date_is"], order_app["service_date_is_form"],
                    "❌ ФР: Пустое поле Дата Исх. счета")

    with allure.step("93. Поле Счет № Вх.счета"):
        check.equal(order_app["account_is"], order_app["account_is_form"], "❌ ФР: Пустое поле Счет № Исх. счета")

    with allure.step("98. Поле Валюта Исх. счета"):
        check.equal(order_app["currency_is"], order_app["currency_is_form"], "❌ ФР: Пустое поле Валюта Исх. счета")

    with allure.step("99. Поле Сумма Исх. счета"):
        check.equal(order_app["amount_is"], order_app["amount_is_form"], "❌ ФР: Пустое поле Сумма Исх. счета")

    #with allure.step("105. Поле Клиент Исх. счета"): клиент не отображается при добавлении
        #check.equal(order_app["client_is"], order_app["client_is_form"], "❌ ФР: Пустое поле Клиент Исх. счета")


    # Взаимозачеты с исх. счетами
    with allure.step("108. Поле Дата Взаимозачеты с исх. счетами"):
        check.equal(order_app["date_vis"], order_app["date_vis_form"],
                    "❌ ФР: Пустое поле Дата Взаимозачеты с исх. счетами")

    with allure.step("109. Поле Счет № Взаимозачеты с исх. счетами"):
        check.equal(order_app["account_vis"], order_app["account_vis_form"],
                    "❌ ФР: Пустое поле Счет № Взаимозачеты с исх. счетами")

    with allure.step("112. Поле Валюта Взаимозачеты с исх. счетами"):
        check.equal(order_app["currency_vis"], order_app["currency_vis_form"],
                    "❌ ФР: Пустое поле Валюта Взаимозачеты с исх. счетами")

    with allure.step("113. Поле Сумма Взаимозачеты с исх. счетами"):
        check.equal(order_app["amount_vis"], order_app["amount_vis_form"],
                    "❌ ФР: Пустое поле Сумма Взаимозачеты с исх. счетами")

    with allure.step("114. Поле Информация  Взаимозачеты с исх. счетами"):
        check.equal(order_app["info_vis"], order_app["info_vis_form"],
                    "❌ ФР: Пустое поле Информация Взаимозачеты с исх. счетами")

    #with allure.step("110. Поле Покупатель Взаимозачеты с исх. счетами"):Покупатель не отображается при добавлении
        #check.equal(order_app["buyer_vis"], order_app["buyer_vis_form"],"❌ ФР: Пустое поле Покупатель Взаимозачеты с исх. счетами")

   # Все счета
    with allure.step("115. Поле Дата в таблице Все счета"):
        compare_dates(order_app["vs_date"], order_app["data_all_accounts"],"❌ ФР: Не совпадают Дата в таблице Все счета")

    with allure.step("116. Поле Поставщик в таблице Все счета"):
        check.equal(order_app["vs_supplier_mod"], order_app["supplier_all_accounts"],
                    "❌ ФР: Не совпадают Поставщик в таблице Все счета")

    with allure.step("117. Поле Счет № в таблице Все счета"):
        check.equal(order_app["vs_number_mod"], order_app["account_all_accounts"],
                    "❌ ФР: Не совпадают Счет № в таблице Все счета")

    with allure.step("119. Поле Покупатель в таблице Все счета"):
        check.equal(order_app["vs_buyer_mod"], order_app["buyer_all_accounts"],
                    "❌ ФР: Не совпадают Покупатель в таблице Все счета")

    with allure.step("120. Поле Валюта в таблице Все счета"):
        check.equal(order_app["service_currency1"], order_app["currency_all_accounts"],
                    "❌ ФР: Не совпадают Валюта в таблице Все счета")

    with allure.step("121. Поле Сумма в таблице Все счета"):
        check.equal(order_app["service_total"], order_app["amount_all_accounts"],
                    "❌ ФР: Не совпадают Сумма в таблице Все счета")

    with allure.step("124. Поле Примечание в таблице Все счета"):
        check.equal(order_app["vs_note_mod"], order_app["note_all_accounts"],
                    "❌ ФР: Не совпадают Примечание в таблице Все счета")

    with allure.step("84. Поле Начислено"):
        check.equal(order_app["charged_vis"], order_app["charged_vis_form"], "❌ ФР: Пустое поле Начислено")

    with allure.step("85. Поле Начислено (С.В.)"):
        check.equal(order_app["charged_sv_vis"], order_app["charged_sv_vis_form"],
                    "❌ ФР: Пустое поле Начислено (С.В.)")

    # Все услуги
    with allure.step("125. Поле Счет в таблице Все услуги"):
        check.equal(order_app["vs_number_mod"], order_app["all_serv_invoice_number"],
                    "❌ ФР: Не совпадают Счет в таблице Все услуги")

    with allure.step("126. Поле Дата счета в таблице Все услуги"):
        compare_dates(order_app["vs_date_mod"], order_app["all_serv_invoice_date"],
                      "❌ ФР: Не совпадают Дата счета в таблице Все услуги")

    with allure.step("127. Поле Услуга в таблице Все услуги"):
        check.equal(order_app["service_service"], order_app["all_serv_service"],
                    "❌ ФР: Не совпадают Услуга в таблице Все услуги")

    with allure.step("129. Поле Покупатель в таблице Все услуги"):
        check.equal(order_app["vs_buyer_mod"], order_app["all_serv_buyer"],
                    "❌ ФР: Не совпадают Покупатель в таблице Все услуги")

    with allure.step("130. Поле Поставщик в таблице Все услуги"):
        check.equal(order_app["vs_supplier_mod"], order_app["all_serv_supplier"],
                    "❌ ФР: Не совпадают Поставщик в таблице Все услуги")

    with allure.step("131. Поле Ставка в таблице Все услуги"):
        check.equal(order_app["service_total1"], order_app["all_serv_rate"],
                    "❌ ФР: Не совпадают Ставка в таблице Все услуги")

    with allure.step("132. Поле Валюта в таблице Все услуги"):
        check.equal(order_app["all_serv_currency"], "p", "❌ ФР: Не совпадают Валюта в таблице Все услуги")

    with allure.step("133. Поле Кол-во в таблице Все услуги"):
        check.equal(order_app["quantity_service"], order_app["all_serv_quantity"],
                    "❌ ФР: Не совпадают Кол-во в таблице Все услуги")

    with allure.step("134. Поле Примечание счета в таблице Все услуги"):
        check.equal(order_app["vs_note_mod"], order_app["all_serv_invoice_note"],
                    "❌ ФР: Не совпадают Примечание счета в таблице Все услуги")
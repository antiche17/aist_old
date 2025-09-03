import pytest
import allure
from orders.freight import WinAISTApp
import pytest_check as check
from locators.function import Function


from datetime import datetime

def normalize_date(date_str):
    formats = ["%d %B %Y г.", "%d.%m.%Y"]
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
    print("[SETUP] Запуск фикстуры order_app")
    app = WinAISTApp()
    try:
        order_data = app.freight()
        yield order_data
    finally:
        print("[TEARDOWN] Закрытие WinAISTApp")
        app.close()

def check_equal_dates(value1, value2, field_name):
    normalized1 = normalize_date(value1)
    normalized2 = normalize_date(value2)
    check.equal(normalized1, normalized2, f"❌ ФР: Не одинаковый {field_name}")

@allure.title("Проверка Таблицы Грузы")
@pytest.mark.order(1)
def test_freight(order_app):
    with allure.step("1. Сравниваем созданного клиента"):
        check.equal(order_app["name_client"], order_app["name_client_order"], "❌ ФР: клиенты не одинаковые")

    with allure.step("2. Ответственный"):
        check.equal(order_app["order_otv"], "автотест", "❌ ФР: номер ТЕ не одинаковые")


    #Проверки с таблицей Грузы
    # Проверки bulkership
    with allure.step("3. Сравнение Ответственный Экспедиция"):
        check.equal(order_app["forwarding_otv"], order_app["bul_otv_table"], "❌ ФР: Не одинаковый Ответственный Экспедиция")

    with allure.step("4. Статус автоперевозки"):
        check.equal(order_app["auto_status"], order_app["bul_auto_status_table"], "❌ ФР: Не одинаковый Статус автоперевозки")

    with allure.step("5. Получатель"):
        check.equal(order_app["order_recipient"], order_app["bul_recipient_table"], "❌ ФР: Не одинаковый Получатель")

    with allure.step("6. Клиент"):
        check.equal(order_app["name_client_order"], order_app["bul_client_table"], "❌ ФР: клиенты не одинаковые")

    with allure.step("7. Номер ТЕ"):
        check.equal(order_app["bul_te_number"], order_app["bul_te_number_form"], "❌ ФР: номер ТЕ не одинаковые")

    with allure.step("8. ТЕ"):
        check.equal(order_app["bul_type_freight"], order_app["bul_type_freight_form"], "❌ ФР: ТЕ не одинаковые")

    with allure.step("9. Тип ТЕ"):
        check.equal(order_app["bul_type_te"], order_app["bul_type_te_form"], "❌ ФР: Тип ТЕ не одинаковые")

    with allure.step("10. Вес брутто"):
        check.equal(order_app["bul_te_gross"], order_app["bul_gross_table"], "❌ ФР: Не одинаковый Вес брутто")

    with allure.step("11. Номер пломбы"):
        check.equal(order_app["bul_seal_num_form_mod"], order_app["bul_seal_num_table"], "❌ ФР: Не одинаковый Номер пломбы")

    with allure.step("12. Терминал "):
        check.equal(order_app["sea_terminal_form"], order_app["bul_sea_terminal_table"], "❌ ФР: Не одинаковый Вес нетто")

    with allure.step("13. Порт"):
        check.equal(order_app["sea_port_form"], order_app["bul_port_table"], "❌ ФР: Не одинаковый Вес нетто")

    with allure.step("14. Планируемая дата прибытия"):
        check.equal(order_app["sea_plan_arrival_form"], order_app["bul_plan_arrival_table"], "❌ ФР: Планируемая дата прибытия")

    with allure.step("15. Фактическая дата прибытия"):
        check.equal(order_app["sea_fact_arrival_form"], order_app["bul_fact_arrival_table"], "❌ ФР: Не одинаковый Фактическая дата прибытия")

    with allure.step("16. Дата выгрузки"):
        check.equal(order_app["bul_unloading_mod"], order_app["bul_unloading_table"], "❌ ФР: Не одинаковый Дата выгрузки")

    with allure.step("17. Дата ДО/ДО1"):
        check.equal(order_app["bul_do_form_mod"], order_app["bul_do_table"], "❌ ФР: Не одинаковый Дата ДО/ДО1")

    with allure.step("18. Получение документов"):
        check.equal(order_app["forwarding_receiving_doc"], order_app["bul_forwarding_doc_table"], "❌ ФР: Не одинаковый Получение документов")

    with allure.step("19. Дата номинации экспедитора"):
        check.equal(order_app["forwarding_nomination"], order_app["bul_nomination_table"], "❌ ФР: Не одинаковый Дата номинации экспедитора")

    with allure.step("20. Режим ТО"):
        check.equal(order_app["bul_regime_to_form_mod"], order_app["bul_regime_to_table"], "❌ ФР: Не одинаковый Режим ТО")

    with allure.step("21. Дата выдачи Телекс-релиза"):
        check.equal(order_app["forwarding_telex"], order_app["bul_telex_table"], "❌ ФР: Не одинаковый Телекс-релиза")



    with allure.step("22. Дата ТО"):
        check.equal(order_app["bul_data_to_form_mod"], order_app["bul_data_to_table"], "❌ ФР: Не одинаковый Дата ТО")

    with allure.step("23. Океанская линия"):
        check.equal(order_app["sea_ocean_line_form"], order_app["bul_ocean_line_table"], "❌ ФР: Не одинаковый Океанская линия")

    with allure.step("24. Сравнение Океанское судно"):
        check.equal(order_app["sea_ship_shipment_form"], order_app["bul_sea_ship_shipment_table"], "❌ ФР: Не одинаковый Океанское судно")

    with allure.step("25. Сравнение Океанский коносамент"):
        check.equal(order_app["sea_ocean_konos_form"], order_app["bul_ocean_konos_table"], "❌ ФР: Не одинаковый Океанский коносамент")

    with allure.step("26. Сравнение Фидерная линия"):
        check.equal(order_app["sea_feeder_line_form"], order_app["bul_feeder_line_table"], "❌ ФР: Не одинаковый Фидерная линия")

    with allure.step("27. Сравнение Фидерное судно"):
        check.equal(order_app["sea_ship_trans1_form"], order_app["bul_sea_ship_trans1_table"],"❌ ФР: Не одинаковый Фидерное судно")

    with allure.step("28. Сравнение Фидерный коносамент"):
        check.equal(order_app["sea_feeder_konos_form"], order_app["bul_feeder_konos_table"], "❌ ФР: Не одинаковый Фидерный коносамент")

    with allure.step("29. Перевозка номер морская перевозка"):
        check.is_true(order_app["type_transport1"] in order_app["bul_transport_table"], "❌ ФР: Нет номера перевозки")

    with allure.step("30. Перевозка номер автоперевозка bul"):
        check.is_true(order_app["type_transport2"] in  order_app["bul_transport_table"], "❌ ФР: Не одинаковый Перевозка номер")

    with allure.step("31. Заказ"):
        check.equal(order_app["order_number"], order_app["order_number_table"], "❌ ФР: Не одинаковый Заказ")


    with allure.step("32. Ответственный за Заказ"):
        check.equal(order_app["order_otv"], order_app["bul_order_otv_table"], "❌ ФР: Не одинаковый Ответственный за Заказ")

    with allure.step("33. Номер Экспедирование"):
        check.equal(order_app["forwarding_number"], order_app["bul_forwarding_number_table"], "❌ ФР: Не одинаковый Номер Экспедирование")



    with allure.step("34. Примечание ТЕ"):
        check.equal(order_app["bul_note_form_mod"], order_app["bul_note_table"], "❌ ФР: Не одинаковый Примечание ТЕ")

    with allure.step("35. Адрес доставки автоперевозки"):
        check.equal(order_app["auto_address"], order_app["bul_auto_address_table"], "❌ ФР: Не одинаковый Адрес доставки")

    with allure.step("36. Планируемая дата доставки автоперевозка"):
        check.equal(order_app["auto_plan_data"], order_app["bul_auto_plan_data_table"], "❌ ФР: Не одинаковый Планируемая дата доставки")

    with allure.step("37. Водитель"):
        check.equal(order_app["auto_driver"], order_app["bul_auto_driver_table"], "❌ ФР: Не одинаковый Водитель")

    with allure.step("38. Государственный номер автомобиля"):
        check.equal(order_app["auto_number_auto"], order_app["bul_auto_number_auto_table"], "❌ ФР: Не одинаковый Автомобиль")

    with allure.step("39. Ответственный за автоперевозки"):
        check.equal(order_app["auto_otv"], order_app["bul_auto_otv_table"], "❌ ФР: Не одинаковый Ответственный")

    with allure.step("40. Вес нетто"):
        check.equal(order_app["bul_te_net"], order_app["bul_net_table"], "❌ ФР: Не одинаковый Вес нетто")

    with allure.step("41. Номер ГТД"):
        check.equal(order_app["bul_gtd_form_mod"], order_app["bul_gtd_table"], "❌ ФР: Не одинаковый ГТД")

    with allure.step("42. Количество"):
        check.equal(order_app["bul_quantity"], order_app["bul_quantity_form"], "❌ ФР: количество не одинаковые")

    with allure.step("43. Единица измерения"):
        check.equal(order_app["bul_uom"], order_app["bul_uom_form"], "❌ ФР: единица измерения не одинаковые")

    with allure.step("44. Кем создан ТЕ"):
        check.is_true(order_app["bul_create_table"] in order_app["bul_create_form"], "❌ ФР: Не совпадают Кем создан ТЕ")


    # Проверки container
    with allure.step("45. Сравнение Ответственный Экспедиция"):
        check.equal(order_app["forwarding_otv"], order_app["con_otv_table"], "❌ ФР: Не одинаковый Ответственный Экспедиция")

    with allure.step("46. Статус автоперевозки"):
        check.equal(order_app["auto_status"], order_app["con_auto_status_table"], "❌ ФР: Не одинаковый Статус автоперевозки")

    with allure.step("47. Получатель"):
        check.equal(order_app["order_recipient"], order_app["con_recipient_table"], "❌ ФР: Не одинаковый Получатель")

    with allure.step("48. Клиент"):
        check.equal(order_app["name_client_order"], order_app["con_client_table"], "❌ ФР: клиенты не одинаковые")

    with allure.step("49. Вес брутто"):
        check.equal(order_app["con_te_gross"], order_app["con_gross_table"], "❌ ФР: Не одинаковый Вес брутто")

    with allure.step("50. Номер пломбы"):
        check.equal(order_app["con_seal_num_form_mod"], order_app["con_seal_num_table"], "❌ ФР: Не одинаковый Номер пломбы")

    with allure.step("51. Терминал"):
        check.equal(order_app["sea_terminal_form"], order_app["con_sea_terminal_table"], "❌ ФР: Не одинаковый Терминал")

    with allure.step("52. Порт"):
        check.equal(order_app["sea_port_form"], order_app["con_port_table"], "❌ ФР: Не одинаковый Порт")

    with allure.step("53. Планируемая дата прибытия"):
        check.equal(order_app["sea_plan_arrival_form"], order_app["con_plan_arrival_table"], "❌ ФР: Планируемая дата прибытия")

    with allure.step("54. Фактическая дата прибытия"):
        check.equal(order_app["sea_fact_arrival_form"], order_app["con_fact_arrival_table"], "❌ ФР: Не одинаковый Фактическая дата прибытия")

    with allure.step("55. Дата выгрузки"):
        check.equal(order_app["con_unloading_mod"], order_app["con_unloading_table"], "❌ ФР: Не одинаковый Дата выгрузки")

    with allure.step("56. Дата ДО/ДО1"):
        check.equal(order_app["con_do_form_mod"], order_app["con_do_table"], "❌ ФР: Не одинаковый Дата ДО/ДО1")

    with allure.step("57. Получение документов"):
        check.equal(order_app["forwarding_receiving_doc"], order_app["con_forwarding_doc_table"], "❌ ФР: Не одинаковый Получение документов")

    with allure.step("58. Дата номинации экспедитора"):
        check.equal(order_app["forwarding_nomination"], order_app["con_nomination_table"], "❌ ФР: Не одинаковый Дата номинации экспедитора")

    with allure.step("59. Режим ТО"):
        check.equal(order_app["con_regime_to_form_mod"], order_app["con_regime_to_table"], "❌ ФР: Не одинаковый Режим ТО")

    with allure.step("60. Дата выдачи Телекс-релиза"):
        check.equal(order_app["forwarding_telex"], order_app["con_telex_table"], "❌ ФР: Не одинаковый Телекс-релиза")



    with allure.step("61. Дата ТО"):
        check.equal(order_app["con_data_to_form_mod"], order_app["con_data_to_table"], "❌ ФР: Не одинаковый Дата ТО")

    with allure.step("62. Океанская линия"):
        check.equal(order_app["sea_ocean_line_form"], order_app["con_ocean_line_table"], "❌ ФР: Не одинаковый Океанская линия")

    with allure.step("63. Сравнение Океанское судно"):
        check.equal(order_app["sea_ship_shipment_form"], order_app["con_sea_ship_shipment_table"], "❌ ФР: Не одинаковый Океанское судно")

    with allure.step("64. Сравнение Океанский коносамент"):
        check.equal(order_app["sea_ocean_konos_form"], order_app["con_ocean_konos_table"], "❌ ФР: Не одинаковый Океанский коносамент")

    with allure.step("65. Сравнение Фидерная линия"):
        check.equal(order_app["sea_feeder_line_form"], order_app["con_feeder_line_table"], "❌ ФР: Не одинаковый Фидерная линия")

    with allure.step("66. Сравнение Фидерное судно"):
        check.equal(order_app["sea_ship_trans1_form"], order_app["con_sea_ship_trans1_table"],"❌ ФР: Не одинаковый Фидерное судно")

    with allure.step("67. Сравнение Фидерный коносамент"):
        check.equal(order_app["sea_feeder_konos_form"], order_app["con_feeder_konos_table"], "❌ ФР: Не одинаковый Фидерный коносамент")

    with allure.step("68. Перевозка номер морская перевозка con"):
        check.is_true(order_app["type_transport1"] in order_app["con_transport_table"], "❌ ФР: Нет номера перевозки")

    with allure.step("69. Перевозка номер автоперевозка con"):
        check.is_true(order_app["type_transport2"] in  order_app["con_transport_table"], "❌ ФР: Не одинаковый Перевозка номер")

    with allure.step("70. Заказ"):
        check.equal(order_app["order_number"], order_app["order_number_table"], "❌ ФР: Не одинаковый Заказ")


    with allure.step("71. Ответственный за Заказ"):
        check.equal(order_app["order_otv"], order_app["con_order_otv_table"], "❌ ФР: Не одинаковый Ответственный за Заказ")

    with allure.step("72. Номер Экспедирование"):
        check.equal(order_app["forwarding_number"], order_app["con_forwarding_number_table"], "❌ ФР: Не одинаковый Номер Экспедирование")



    with allure.step("73. Примечание ТЕ"):
        check.equal(order_app["con_note_form_mod"], order_app["con_note_table"], "❌ ФР: Не одинаковый Примечание ТЕ")

    with allure.step("74. Адрес доставки автоперевозки"):
        check.equal(order_app["auto_address"], order_app["con_auto_address_table"], "❌ ФР: Не одинаковый Адрес доставки")

    with allure.step("75. Планируемая дата доставки автоперевозка"):
        check.equal(order_app["auto_plan_data"], order_app["con_auto_plan_data_table"], "❌ ФР: Не одинаковый Планируемая дата доставки")

    with allure.step("76. Водитель"):
        check.equal(order_app["auto_driver"], order_app["con_auto_driver_table"], "❌ ФР: Не одинаковый Водитель")

    with allure.step("77. Государственный номер автомобиля"):
        check.equal(order_app["auto_number_auto"], order_app["con_auto_number_auto_table"], "❌ ФР: Не одинаковый Автомобиль")

    with allure.step("78. Ответственный за автоперевозки"):
        check.equal(order_app["auto_otv"], order_app["con_auto_otv_table"], "❌ ФР: Не одинаковый Ответственный")

    with allure.step("79. Вес нетто"):
        check.equal(order_app["con_te_net"], order_app["con_net_table"], "❌ ФР: Не одинаковый Вес нетто")

    with allure.step("80. Номер ГТД"):
        check.equal(order_app["con_gtd_form_mod"], order_app["con_gtd_table"], "❌ ФР: Не одинаковый ГТД")

    with allure.step("81. Кем создан ТЕ"):
        check.is_true(order_app["con_create_table"] in order_app["con_create_form"], "❌ ФР: Не совпадают Кем создан ТЕ")

    #GПроверка редактируемые поля
    with allure.step("82. Факт. дата выгрузки (bul)"):
        check.equal(order_app["bul_unloading_mod2"] , order_app["unloading_table_bul"], msg="❌ ФР: Не одинаковая Выгрузка")

    with allure.step("83. Номер пломбы (bul)"):
        check.equal(order_app["bul_seal_num_mod2"] , order_app["seal_number_table_bul"], msg="❌ ФР: Не одинаковая Пломба")

    with allure.step("84. ДО/ДО1 Разное (bul)"):
        check.equal(order_app["bul_do_mod2"] , order_app["do_table_bul"], msg="❌ ФР: Одинаковое ДО")

    with allure.step("85. Режим ТО (bul)"):
        check.equal(order_app["bul_regime_to_mod2"] , order_app["regimen_table_bul"], msg="❌ ФР: Не одинаковый Режим")

    with allure.step("86. Дата ТО (bul)"):
        check.equal(order_app["bul_data_to_mod2"] , order_app["data_to_table_bul"], msg="❌ ФР: Не одинаковая Дата")

    with allure.step("87. Примечание (ТЕ) (bul)"):
        check.equal(order_app["bul_note_mod2"] , order_app["note_table_bul"], msg="❌ ФР: Не одинаковое Примечание")

    with allure.step("88. Номер ГТД (bul)"):
        check.equal(order_app["bul_gtd_mod2"] , order_app["gtd_number_table_bul"], msg="❌ ФР: Не одинаковый ГТД")

    with allure.step("89. Выгрузка (con)"):
        check.equal(order_app["con_unloading_mod2"] , order_app["unloading_table_con"], msg="❌ ФР: Не одинаковая Выгрузка")

    with allure.step("90. Пломба (con)"):
        check.equal(order_app["con_seal_num_mod2"] , order_app["seal_number_table_con"], msg="❌ ФР: Не одинаковая Пломба")

    with allure.step("91. ДО (con)"):
        check.equal(order_app["con_do_mod2"] , order_app["do_table_con"], msg="❌ ФР: Не одинаковое ДО")

    with allure.step("92. Режим ТО (con)"):
        check.equal(order_app["con_regime_to_mod2"] , order_app["regimen_table_con"], msg="❌ ФР: Не одинаковый Режим")

    with allure.step("93. Дата ТО (con)"):
        check.equal(order_app["con_data_to_mod2"] , order_app["data_to_table_con"], msg="❌ ФР: Не одинаковая Дата")

    with allure.step("94. Примечание (con)"):
        check.equal(order_app["con_note_mod2"] , order_app["note_table_con"], msg="❌ ФР: Не одинаковое Примечание")

    with allure.step("95. ГТД (con)"):
        check.equal(order_app["con_gtd_mod2"] , order_app["gtd_number_table_con"], msg="❌ ФР: Не одинаковый ГТД")

    with allure.step("96. Терминал (sea)"):
        check.equal(order_app["sea_terminal_mod2"] , order_app["terminal_table"], msg="❌ ФР: Не одинаковый Терминал")

    with allure.step("97. Порт (sea)"):
        check.equal(order_app["sea_port_mod2"] , order_app["port_table"], msg="❌ ФР: Не одинаковый Порт")

    with allure.step("98. План прибытия (sea)"):
        check.equal(order_app["sea_plan_arrival_mod2"] , order_app["plan_arrival_table"], msg="❌ ФР: Не одинаковая Плановая дата")

    with allure.step("99. Факт прибытия (sea)"):
        check.equal(order_app["sea_fact_arrival_mod2"] , order_app["fact_arrival_table"], msg="❌ ФР: Не одинаковая Фактическая дата")

    with allure.step("100. Статус (auto)"):
        check.equal(order_app["auto_status_mod2"] , order_app["status_table"], msg="❌ ФР: Не одинаковый Статус")

    with allure.step("101. Адрес (auto)"):
        check.equal(order_app["auto_address_mod2"] , order_app["address_table"], msg="❌ ФР: Не одинаковый Адрес")

    with allure.step("102. План. дата доставки (auto)"):
        check.equal(order_app["auto_plan_data_mod2"] , order_app["delivery_data_plan_table"], msg="❌ ФР: Не одинаковая Дата доставки")

    with allure.step("103. Водитель (auto)"):
        check.equal(order_app["auto_driver_mod2"] , order_app["driver_table"], msg="❌ ФР: Не одинаковый Водитель")

    with allure.step("104. Номер авто (auto)"):
        check.equal(order_app["auto_number_auto_mod2"] , order_app["car_table"], msg="❌ ФР: Не одинаковый Номер авто")

    with allure.step("105. Ответственный (forwarding)"):
        check.equal(order_app["forwarding_otv_mod2"] , order_app["otv_table"], msg="❌ ФР: Не одинаковый Ответственный")

    with allure.step("106. Телекс (forwarding)"):
        check.equal(order_app["forwarding_telex_mod2"] , order_app["telex_table"], msg="❌ ФР: Не одинаковый Телекс")

    with allure.step("107. Документ (forwarding)"):
        check.equal(order_app["forwarding_receiving_doc_mod2"] , order_app["doc_table"], msg="❌ ФР: Не одинаковый Документ")


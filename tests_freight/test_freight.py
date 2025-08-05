import pytest
import allure
from orders.freight import WinAISTApp
import pytest_check as check
from locators.function import Function


@pytest.fixture(scope="module")
def order_app():
    print("[SETUP] Запуск фикстуры order_app")
    app = WinAISTApp()
    order_data = app.freight()
    yield order_data
    print("[TEARDOWN] Закрытие WinAISTApp")
    app.close()

def check_equal_dates(value1, value2, field_name):
    normalized1 = normalize_date(value1)
    normalized2 = normalize_date(value2)
    check.equal(normalized1, normalized2, f"❌ ФР: Не одинаковый {field_name}")

@allure.title("Проверка Таблицы Грузы")
@pytest.mark.order(1)
def test_value_del(order_app):
    with allure.step("2. Сравниваем созданного клиента"):
        check.equal(order_app["name_client"], order_app["name_client_order"], "❌ ФР: клиенты не одинаковые")

    with allure.step("3. Ответственный"):
        check.equal(order_app["order_otv"], "автотест", "❌ ФР: номер ТЕ не одинаковые")


    #Проверки с таблицей Грузы
    # Проверки bulkership
    with allure.step("4. Сравнение Ответственный Экспедиция"):
        check.equal(order_app["forwarding_otv"], order_app["bul_otv_table"], "❌ ФР: Не одинаковый Ответственный Экспедиция")

    with allure.step("5. Статус автоперевозки"):
        check.equal(order_app["auto_status"], order_app["bul_auto_status_table"], "❌ ФР: Не одинаковый Статус автоперевозки")

    with allure.step("6. Получатель"):
        check.equal(order_app["order_recipient"], order_app["bul_recipient_table"], "❌ ФР: Не одинаковый Получатель")

    with allure.step("7. Клиент"):
        check.equal(order_app["name_client_order"], order_app["bul_client_table"], "❌ ФР: клиенты не одинаковые")

    with allure.step("8. Номер ТЕ"):
        check.equal(order_app["bul_te_number"], order_app["bul_te_number_form"], "❌ ФР: номер ТЕ не одинаковые")

    with allure.step("9. ТЕ"):
        check.equal(order_app["bul_type_freight"], order_app["bul_type_freight_form"], "❌ ФР: ТЕ не одинаковые")

    with allure.step("10. Тип ТЕ"):
        check.equal(order_app["bul_type_te"], order_app["bul_type_te_form"], "❌ ФР: Тип ТЕ не одинаковые")

    with allure.step("11. Вес брутто"):
        check.equal(order_app["bul_te_gross"], order_app["bul_gross_table"], "❌ ФР: Не одинаковый Вес брутто")

    with allure.step("12. Номер пломбы"):
        check.equal(order_app["bul_seal_num_form_mod"], order_app["bul_seal_num_table"], "❌ ФР: Не одинаковый Номер пломбы")

    with allure.step("13. Терминал "):
        check.equal(order_app["sea_terminal_form"], order_app["bul_sea_terminal_table"], "❌ ФР: Не одинаковый Вес нетто")

    with allure.step("14. Порт"):
        check.equal(order_app["sea_port_form"], order_app["bul_port_table"], "❌ ФР: Не одинаковый Вес нетто")

    with allure.step("15. Планируемая дата прибытия"):
        check.equal(order_app["sea_plan_arrival_form"], order_app["bul_plan_arrival_table"], "❌ ФР: Планируемая дата прибытия")

    with allure.step("16. Фактическая дата прибытия"):
        check.equal(order_app["sea_fact_arrival_form"], order_app["bul_fact_arrival_table"], "❌ ФР: Не одинаковый Фактическая дата прибытия")

    with allure.step("17. Дата выгрузки"):
        check.equal(order_app["bul_unloading_mod"], order_app["bul_unloading_table"], "❌ ФР: Не одинаковый Дата выгрузки")

    with allure.step("18. Дата ДО/ДО1"):
        check.equal(order_app["bul_do_form_mod"], order_app["bul_do_table"], "❌ ФР: Не одинаковый Дата ДО/ДО1")

    with allure.step("19. Получение документов"):
        check.equal(order_app["forwarding_receiving_doc"], order_app["bul_forwarding_doc_table"], "❌ ФР: Не одинаковый Получение документов")

    with allure.step("20. Дата номинации экспедитора"):
        check.equal(order_app["forwarding_nomination"], order_app["bul_nomination_table"], "❌ ФР: Не одинаковый Дата номинации экспедитора")

    with allure.step("21. Режим ТО"):
        check.equal(order_app["bul_regime_to_form_mod"], order_app["bul_regime_to_table"], "❌ ФР: Не одинаковый Режим ТО")

    with allure.step("22. Дата выдачи Телекс-релиза"):
        check.equal(order_app["forwarding_telex"], order_app["bul_telex_table"], "❌ ФР: Не одинаковый Телекс-релиза")



    with allure.step("23. Дата ТО"):
        check.equal(order_app["bul_data_to_form_mod"], order_app["bul_data_to_table"], "❌ ФР: Не одинаковый Дата ТО")

    with allure.step("24. Океанская линия"):
        check.equal(order_app["sea_ocean_line_form"], order_app["bul_ocean_line_table"], "❌ ФР: Не одинаковый Океанская линия")

    with allure.step("25. Сравнение Океанское судно"):
        check.equal(order_app["sea_ship_shipment_form"], order_app["bul_sea_ship_shipment_table"], "❌ ФР: Не одинаковый Океанское судно")

    with allure.step("26. Сравнение Океанский коносамент"):
        check.equal(order_app["sea_ocean_konos_form"], order_app["bul_ocean_konos_table"], "❌ ФР: Не одинаковый Океанский коносамент")

    with allure.step("27. Сравнение Фидерная линия"):
        check.equal(order_app["sea_feeder_line_form"], order_app["bul_feeder_line_table"], "❌ ФР: Не одинаковый Фидерная линия")

    with allure.step("28. Сравнение Фидерное судно"):
        check.equal(order_app["sea_ship_trans1_form"], order_app["bul_sea_ship_trans1_table"],"❌ ФР: Не одинаковый Фидерное судно")

    with allure.step("29. Сравнение Фидерный коносамент"):
        check.equal(order_app["sea_feeder_konos_form"], order_app["bul_feeder_konos_table"], "❌ ФР: Не одинаковый Фидерный коносамент")

    with allure.step("29. Перевозка номер морская перевозка"):
        check.is_true(order_app["type_transport1"] in order_app["bul_transport_table"], "❌ ФР: Нет номера перевозки")

    with allure.step("29. Перевозка номер автоперевозка bul"):
        check.is_true(order_app["type_transport2"] in  order_app["bul_transport_table"], "❌ ФР: Не одинаковый Перевозка номер")

    with allure.step("29. Заказ"):
        check.equal(order_app["order_number"], order_app["order_number_table"], "❌ ФР: Не одинаковый Заказ")


    with allure.step("30. Ответственный за Заказ"):
        check.equal(order_app["order_otv"], order_app["bul_order_otv_table"], "❌ ФР: Не одинаковый Ответственный за Заказ")

    with allure.step("31. Номер Экспедирование"):
        check.equal(order_app["forwarding_number"], order_app["bul_forwarding_number_table"], "❌ ФР: Не одинаковый Номер Экспедирование")



    with allure.step("32. Примечание ТЕ"):
        check.equal(order_app["bul_note_form_mod"], order_app["bul_note_table"], "❌ ФР: Не одинаковый Примечание ТЕ")

    with allure.step("8. Адрес доставки автоперевозки"):
        check.equal(order_app["auto_address"], order_app["bul_auto_address_table"], "❌ ФР: Не одинаковый Адрес доставки")

    with allure.step("8. Планируемая дата доставки автоперевозка"):
        check.equal(order_app["auto_plan_data"], order_app["bul_auto_plan_data_table"], "❌ ФР: Не одинаковый Планируемая дата доставки")

    with allure.step("8. Водитель"):
        check.equal(order_app["auto_driver"], order_app["bul_auto_driver_table"], "❌ ФР: Не одинаковый Водитель")

    with allure.step("8. Государственный номер автомобиля"):
        check.equal(order_app["auto_number_auto"], order_app["bul_auto_number_auto_table"], "❌ ФР: Не одинаковый Автомобиль")

    with allure.step("8. Ответственный за автоперевозки"):
        check.equal(order_app["auto_otv"], order_app["bul_auto_otv_table"], "❌ ФР: Не одинаковый Ответственный")

    with allure.step("8. Вес нетто"):
        check.equal(order_app["bul_te_net"], order_app["bul_net_table"], "❌ ФР: Не одинаковый Вес нетто")

    with allure.step("8. Номер ГТД"):
        check.equal(order_app["bul_gtd_form_mod"], order_app["bul_gtd_table"], "❌ ФР: Не одинаковый ГТД")

    with allure.step("5. Количество"):
        check.equal(order_app["bul_quantity"], order_app["bul_quantity_form"], "❌ ФР: количество не одинаковые")

    with allure.step("6. Единица измерения"):
        check.equal(order_app["bul_uom"], order_app["bul_uom_form"], "❌ ФР: единица измерения не одинаковые")

    with allure.step("6. Кем создан ТЕ"):
        check.is_true(order_app["bul_create_table"] in order_app["bul_create_form"], "❌ ФР: Не совпадают Кем создан ТЕ")


    # Проверки container
    with allure.step("4. Сравнение Ответственный Экспедиция"):
        check.equal(order_app["forwarding_otv"], order_app["con_otv_table"], "❌ ФР: Не одинаковый Ответственный Экспедиция")

    with allure.step("5. Статус автоперевозки"):
        check.equal(order_app["auto_status"], order_app["con_auto_status_table"], "❌ ФР: Не одинаковый Статус автоперевозки")

    with allure.step("6. Получатель"):
        check.equal(order_app["order_recipient"], order_app["con_recipient_table"], "❌ ФР: Не одинаковый Получатель")

    with allure.step("7. Клиент"):
        check.equal(order_app["name_client_order"], order_app["con_client_table"], "❌ ФР: клиенты не одинаковые")

    with allure.step("11. Вес брутто"):
        check.equal(order_app["con_te_gross"], order_app["con_gross_table"], "❌ ФР: Не одинаковый Вес брутто")

    with allure.step("12. Номер пломбы"):
        check.equal(order_app["con_seal_num_form_mod"], order_app["con_seal_num_table"], "❌ ФР: Не одинаковый Номер пломбы")

    with allure.step("13. Терминал"):
        check.equal(order_app["sea_terminal_form"], order_app["con_sea_terminal_table"], "❌ ФР: Не одинаковый Терминал")

    with allure.step("14. Порт"):
        check.equal(order_app["sea_port_form"], order_app["con_port_table"], "❌ ФР: Не одинаковый Порт")

    with allure.step("15. Планируемая дата прибытия"):
        check.equal(order_app["sea_plan_arrival_form"], order_app["con_plan_arrival_table"], "❌ ФР: Планируемая дата прибытия")

    with allure.step("16. Фактическая дата прибытия"):
        check.equal(order_app["sea_fact_arrival_form"], order_app["con_fact_arrival_table"], "❌ ФР: Не одинаковый Фактическая дата прибытия")

    with allure.step("17. Дата выгрузки"):
        check.equal(order_app["con_unloading_mod"], order_app["con_unloading_table"], "❌ ФР: Не одинаковый Дата выгрузки")

    with allure.step("18. Дата ДО/ДО1"):
        check.equal(order_app["con_do_form_mod"], order_app["con_do_table"], "❌ ФР: Не одинаковый Дата ДО/ДО1")

    with allure.step("19. Получение документов"):
        check.equal(order_app["forwarding_receiving_doc"], order_app["con_forwarding_doc_table"], "❌ ФР: Не одинаковый Получение документов")

    with allure.step("20. Дата номинации экспедитора"):
        check.equal(order_app["forwarding_nomination"], order_app["con_nomination_table"], "❌ ФР: Не одинаковый Дата номинации экспедитора")

    with allure.step("21. Режим ТО"):
        check.equal(order_app["con_regime_to_form_mod"], order_app["con_regime_to_table"], "❌ ФР: Не одинаковый Режим ТО")

    with allure.step("22. Дата выдачи Телекс-релиза"):
        check.equal(order_app["forwarding_telex"], order_app["con_telex_table"], "❌ ФР: Не одинаковый Телекс-релиза")



    with allure.step("23. Дата ТО"):
        check.equal(order_app["con_data_to_form_mod"], order_app["con_data_to_table"], "❌ ФР: Не одинаковый Дата ТО")

    with allure.step("24. Океанская линия"):
        check.equal(order_app["sea_ocean_line_form"], order_app["con_ocean_line_table"], "❌ ФР: Не одинаковый Океанская линия")

    with allure.step("25. Сравнение Океанское судно"):
        check.equal(order_app["sea_ship_shipment_form"], order_app["con_sea_ship_shipment_table"], "❌ ФР: Не одинаковый Океанское судно")

    with allure.step("26. Сравнение Океанский коносамент"):
        check.equal(order_app["sea_ocean_konos_form"], order_app["con_ocean_konos_table"], "❌ ФР: Не одинаковый Океанский коносамент")

    with allure.step("27. Сравнение Фидерная линия"):
        check.equal(order_app["sea_feeder_line_form"], order_app["con_feeder_line_table"], "❌ ФР: Не одинаковый Фидерная линия")

    with allure.step("28. Сравнение Фидерное судно"):
        check.equal(order_app["sea_ship_trans1_form"], order_app["con_sea_ship_trans1_table"],"❌ ФР: Не одинаковый Фидерное судно")

    with allure.step("29. Сравнение Фидерный коносамент"):
        check.equal(order_app["sea_feeder_konos_form"], order_app["con_feeder_konos_table"], "❌ ФР: Не одинаковый Фидерный коносамент")

    with allure.step("29. Перевозка номер морская перевозка con"):
        check.is_true(order_app["type_transport1"] in order_app["con_transport_table"], "❌ ФР: Нет номера перевозки")

    with allure.step("29. Перевозка номер автоперевозка con"):
        check.is_true(order_app["type_transport2"] in  order_app["con_transport_table"], "❌ ФР: Не одинаковый Перевозка номер")

    with allure.step("29. Заказ"):
        check.equal(order_app["order_number"], order_app["order_number_table"], "❌ ФР: Не одинаковый Заказ")


    with allure.step("30. Ответственный за Заказ"):
        check.equal(order_app["order_otv"], order_app["con_order_otv_table"], "❌ ФР: Не одинаковый Ответственный за Заказ")

    with allure.step("31. Номер Экспедирование"):
        check.equal(order_app["forwarding_number"], order_app["con_forwarding_number_table"], "❌ ФР: Не одинаковый Номер Экспедирование")



    with allure.step("32. Примечание ТЕ"):
        check.equal(order_app["con_note_form_mod"], order_app["con_note_table"], "❌ ФР: Не одинаковый Примечание ТЕ")

    with allure.step("8. Адрес доставки автоперевозки"):
        check.equal(order_app["auto_address"], order_app["con_auto_address_table"], "❌ ФР: Не одинаковый Адрес доставки")

    with allure.step("8. Планируемая дата доставки автоперевозка"):
        check.equal(order_app["auto_plan_data"], order_app["con_auto_plan_data_table"], "❌ ФР: Не одинаковый Планируемая дата доставки")

    with allure.step("8. Водитель"):
        check.equal(order_app["auto_driver"], order_app["con_auto_driver_table"], "❌ ФР: Не одинаковый Водитель")

    with allure.step("8. Государственный номер автомобиля"):
        check.equal(order_app["auto_number_auto"], order_app["con_auto_number_auto_table"], "❌ ФР: Не одинаковый Автомобиль")

    with allure.step("8. Ответственный за автоперевозки"):
        check.equal(order_app["auto_otv"], order_app["con_auto_otv_table"], "❌ ФР: Не одинаковый Ответственный")

    with allure.step("8. Вес нетто"):
        check.equal(order_app["con_te_net"], order_app["con_net_table"], "❌ ФР: Не одинаковый Вес нетто")

    with allure.step("8. Номер ГТД"):
        check.equal(order_app["con_gtd_form_mod"], order_app["con_gtd_table"], "❌ ФР: Не одинаковый ГТД")

    with allure.step("6. Кем создан ТЕ"):
        check.is_true(order_app["con_create_table"] in order_app["con_create_form"], "❌ ФР: Не совпадают Кем создан ТЕ")
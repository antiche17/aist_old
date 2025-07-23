import pytest
import allure
from difflib import SequenceMatcher as f
from orders.order import WinAISTApp
import pytest_check as check


@pytest.fixture(scope="module")
def order_app():
    """Фикстура создает и возвращает приложение с созданным заказом"""
    app = WinAISTApp()
    order_data = app.freight_container()
    yield order_data
    app.close()


@allure.title("Проверка создания и удаления груза Container")
def test_container_freight(order_app):
    with allure.step("1. Тип груза — Container"):
        check.equal(order_app["order_dialog_te"], "Container", "❌ ФР: Тип груза не Container")

    with allure.step("2. Тип ТЕ — 20'dc"):
        check.equal(order_app["order_dialog_type"], "20' dc", "❌ ФР: Тип ТЕ не 20'dc")

    with allure.step("3. Количество 1"):
        check.equal(order_app["order_dialog_quantity"], "1", "❌ ФР: Количество не 1")

    with allure.step("5. Номер ТЕ — XXXX0000000'"):
        check.equal(order_app["order_dialog_number"], "XXXX0000000", "ФР: Номер ТЕ не XXXX 0000000")

    with allure.step("6. Сравнение название ТЕ диалога создания и в таблице заказа"):
        check.equal(order_app["order_dialog_te"], order_app["order_table_te"], "ФР: Не совпадают")

    with allure.step("7. Сравнение Типа ТЕ диалога создания и в таблице заказа"):
        check.equal(order_app["order_dialog_type"], order_app["order_table_type"], "ФР: Не совпадают")

    #Форма
    with allure.step("8. Тип груза — Container"):
        check.equal(order_app["order_dialog_te"], order_app["freight_te"], "❌ ФР: совпадают")

    with allure.step("9. Тип ТЕ — 20'dc"):
        check.equal(order_app["order_dialog_type"], order_app["freight_te_type"], "❌ ФР: совпадают")

    with allure.step("10. Номер ТЕ — XXXX0000000'"):
        check.equal(order_app["order_dialog_number"], order_app["freight_number"], "ФР: совпадают")

    with allure.step("11. Вес нетто кг"):
        check.equal(order_app["freight_net"], "-", "❌ ФР: Не прочерк")

    with allure.step("12. Вес брутто кг"):
        check.equal(order_app["freight_gross"], "-", "❌ ФР: Не прочерк")


    with allure.step("13. Выгрузка"):
        check.is_false(order_app["freight_unloading"], "❌ ФР: Не пусто")

    with allure.step("14. Номер пломбы"):
        check.is_false(order_app["freight_seal_number"],"❌ ФР: Не пусто")

    with allure.step("15. Номер ГТД"):
        check.is_false(order_app["freight_number_gtd"], "❌ ФР: Не пусто")

    with allure.step("16. Режим ТО"):
        check.is_false(order_app["freight_mode_to"],  "❌ ФР: Не пусто")

    with allure.step("17. Получение ДО/ДО1"):
        check.is_false(order_app["freight_do"],"❌ ФР: Не пусто")

    with allure.step("18. Дата создания и дата изменения"):
        check.equal(order_app["freight_data_create"], order_app["freight_data_mod"], "❌ ФР: Не одинаковые")

    with allure.step("19. Примечание"):
        check.is_false(order_app["freight_note"], "❌ ФР: Не пусто")

    tabs_to_check = {
        "freight_tab_info": "Информация",
        "freight_tab_goods": "Товары",
        "freight_tab_file": "Файлы",
        "freight_tab_tracking": "Отслеживание",
    }

    # Цикл по каждой вкладке
    for field_name, expected_value in tabs_to_check.items():
        with allure.step(f"Проверка вкладки {expected_value}'"):
            check.equal(order_app.get(field_name), expected_value, f"❌ ФР: Вкладка '{expected_value}' — поле '{field_name}' имеет неверное значение")

    # Редактирование
    with allure.step("20. Изменили Номер ТЕ"):
        check.equal(order_app["freight_number_up"], order_app["freight_number_save"], "❌ ФР: Не совпадают")

    with allure.step("21. Изменили Тип ТЕ"):
        check.equal(order_app["freight_te_type_up"], order_app["freight_te_type_save"], "❌ ФР: Не совпадают")


    with allure.step("22. Выгрузка"):
        check.equal(order_app["freight_unloading_up"], order_app["freight_unloading_save"],"❌ ФР: Не совпадают")

    with allure.step("23. Номер пломбы"):
        check.equal(order_app["freight_seal_number_up"],order_app["freight_seal_number_save"],"❌ ФР: Не совпадают")

    with allure.step("24. Номер ГТД"):
        check.equal(order_app["freight_number_gtd_up"], order_app["freight_number_gtd_save"],"❌ ФР: Не совпадают")

    with allure.step("25. Режим ТО"):
        check.equal(order_app["freight_mode_to_up"],  order_app["freight_mode_to_save"],"❌ ФР: Не совпадают")

    with allure.step("26. Получение ДО/ДО1"):
        check.equal(order_app["freight_do_up"],order_app["freight_do_save"],"❌ ФР: Не совпадают")

    with allure.step("27. Дата ТО"):
        check.equal(order_app["freight_data_to_up"], order_app["freight_data_to_save"],"❌ ФР: Не совпадают")


    with allure.step("28. Дата создания не поменялась"):
        check.equal(order_app["freight_data_create"], order_app["freight_data_create_save"], "❌ ФР: Поменялась")

    with allure.step("29. Дата изменения  поменялась"):
        check.not_equal(order_app["freight_note_up"], order_app["freight_data_mod_save"], "❌ ФР: Не поменялась")


    with allure.step("30. Всего записей 0"):
        check.equal(order_app["freight_del_table"], "Всего записей: 0", "❌ ФР: Не совпадает")
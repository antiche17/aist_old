import pytest
import allure
import pytest_check as check  # ✅ Внимание: правильный импорт
from orders.order import WinAISTApp


@pytest.fixture(scope="module")
def order_app():
    """Фикстура создает и возвращает приложение с созданным заказом"""
    app = WinAISTApp()
    order_data = app.forwarding()
    yield order_data
    app.close()


@allure.title("Полная проверка экспедирования (создание, атрибуты, таблица, 30 проверок)")
@pytest.mark.order(1)
def test_forwarding_order_full_check(order_app):
    with allure.step("2. тип экспедирования Портовое"):
        check.equal(order_app["forwarding_dialog_type"], order_app["forwarding_type"], "ФР: Поля не одинаковые")

    with allure.step("3. Статус экспедирования Черновик"):
       check.equal(order_app["forwarding_status"], "Черновик", "ФР: Не Черновик")

    with allure.step("4. Приоритет Средний"):
        check.equal(order_app["forwarding_priority"], "Средний", "ФР: Не Средний")

    with allure.step("5. Ответственный"):
        check.equal(order_app["forwarding_dialog_otv"], order_app["forwarding_otv"], "ФР: переделать")

    with allure.step("6. Поле Экспедитор"):
        check.is_false(order_app["forwarding_forwarder"], "ФР: Не пустое")

    with allure.step("7. Дата создания равна Дате изменения"):
        check.equal(order_app["forwarding_create_date"], order_app["forwarding_mode_date"], "ФР: Не равны")


    with allure.step("8. Поле Телекс-релиз"):
        check.is_false(order_app["forwarding_telex"], "ФР: Не пустое")

    with allure.step("9. Поле Получение докум"):
        check.is_false(order_app["forwarding_receiving_doc"], "ФР: Не пустое")

    with allure.step("10. Поле Номинация эксп"):
        check.is_false(order_app["forwarding_nomination"], "ФР: Не пустое")


    with allure.step("12. Поле Примечание"):
        check.is_false(order_app["forwarding_note"], "ФР: Не пустое")

    tabs_to_check = {
        "tab_info": "Информация",
        "tab_forwarding_freight": "Экспедируемый груз",
        "tab_services": "Услуги",
        "tab_file": "Файлы"
    }

    # Цикл по каждой вкладке
    for field_name, expected_value in tabs_to_check.items():
        with allure.step(f"Проверка вкладки {expected_value}'"):
            check.equal(order_app.get(field_name), expected_value, f"❌ ФР: Вкладка '{expected_value}' — поле '{field_name}' имеет неверное значение")

    with allure.step("13. Сравниваем Статус"):
        check.equal(order_app["forwarding_status_up"], order_app["forwarding_status_save"], "ФР: Не совпадают")

    with allure.step("14. Сравниваем Приоритет"):
        check.equal(order_app["forwarding_priority_up"], order_app["forwarding_priority_save"], "ФР: Не совпадают")

    with allure.step("15. Сравниваем Экспедитор"):
        check.equal(order_app["forwarding_forwarder_up"], order_app["forwarding_forwarder_save"], "ФР: Не совпадают")

    with allure.step("16. Сравниваем Телекс-релиз"):
        check.equal(order_app["forwarding_telex_up"], order_app["forwarding_telex_save"], "ФР: Не совпадают")

    with allure.step("17. Сравниваем Получение докум"):
        check.equal(order_app["forwarding_receiving_doc_up"], order_app["forwarding_receiving_doc_save"], "ФР: Не совпадают")

    with allure.step("18. Сравниваем Номинация эксп"):
        check.equal(order_app["forwarding_nomination_up"], order_app["forwarding_nomination_save"], "ФР: Не совпадают")


    with allure.step("20. Сравниваем Примечание"):
        check.equal(order_app["forwarding_note_up"], order_app["forwarding_note_save"], "ФР: Не совпадают")


    with allure.step("21. В таблице Тип экспедирования"):
        check.equal(order_app["forwarding_type_table"], order_app["forwarding_type"], "ФР: Не одинаковые")

    with allure.step("22. Сравниваем Номер экспедирования"):
        check.is_true(order_app["forwarding_order_table"], "❌ ФР: Не пустое")

    with allure.step("23. Сравниваем Статус"):
        check.equal(order_app["forwarding_status_save"], order_app["forwarding_status_table"], "ФР: Не совпадают")

    with allure.step("24. Сравниваем Ответственный"):
        check.equal(order_app["forwarding_otv"], order_app["forwarding_otv_table"], "ФР: Не совпадают")

    with allure.step("25. Сравниваем Экспедитор"):
        check.equal(order_app["forwarding_forwarder_save"], order_app["forwarding_forward_table"], "ФР: Не совпадают")

    with allure.step("26. Сравниваем Количество ТЕ"):
        check.equal(order_app["forwarding_te_table"], "0", "❌ ФР: Значение не равно 0")

    with allure.step("27. Сравниваем Дата создания"):
        check.equal(order_app["forwarding_create_table"], order_app["forwarding_mod_table"], "ФР: Не совпадают")

    with allure.step("29. Сравниваем Примечание"):
        check.equal(order_app["forwarding_note_save"], order_app["forwarding_note_table"], "ФР: Не совпадают")

    with allure.step("30. Сравниваем Удалена строка"):
        check.is_false(order_app["forwarding_panel"], "ФР: Не пусто")
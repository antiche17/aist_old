import pytest
import allure
from orders.order_del import WinAISTApp
import pytest_check as check
from locators.function import Function


@pytest.fixture(scope="module")
def order_app():
    print("[SETUP] Запуск фикстуры order_app")
    app = WinAISTApp()
    order_data = app.order_del()
    yield order_data
    print("[TEARDOWN] Закрытие WinAISTApp")
    app.close()

@allure.title("Проверка создание Входящий платеж в заказе. 39 проверок")
@pytest.mark.order(1)
def test_order_del(order_app):
    # 1–4: Проверка наличия номеров заказов в окне удаления
    order_numbers = {
        "order8": "1. 8 номер заказа есть в тексте окна Удаление",
        "order9": "2. 9 номер заказа есть в тексте окна Удаление",
        "order10": "3. 10 номер заказа есть в тексте окна Удаление"
    }

    for field_name, step_desc in order_numbers.items():
        with allure.step(step_desc):
            check.is_true(order_app[field_name] in order_app["del_window"],
                          f"❌ ФР: Нет номера {order_app[field_name]} в окне предупреждения")

    with allure.step("4. Текст про 10 заказ в окне удаления"):
        expected_text = "ещё 7 с оформленными документами на груз, перевозку, экспедирование, декларирование, счет, услугу."
        check.is_true(expected_text in order_app["del_window"],"❌ ФР: Описание оформления документов не найдено в окне удаления")

    # 5–10: Проверка удаления записей
    deleted_entries = {
        "del_file": ("Фаил", "5. Удалён Фаил"),
        "del_is": ("Исходящий счет", "6. Удален Исходящий счет"),
        "del_vs": ("Входящий счет", "7. Удален Входящий счет"),
        "del_ip": ("Исходящий платеж", "8. Удален Исходящий платеж"),
        "del_vp": ("Входящий платеж", "9. Удален Входящий платеж"),
        "del_sea": ("Морская перевозка", "10. Удалена Морская перевозка"),
        "del_auto": ("Автоперевозка", "11. Удалена Автоперевозка"),
        "del_bul": ("Bulkership", "12. Удален Bulkership"),
        "del_con": ("Container", "13. Удален Container"),
        "del_gtd": ("ГТД", "14. Удален ГТД"),
        "del_exp": ("Экспедирование", "15. Удалено Экспедирование"),
    }

    for field_name, (label, step_desc) in deleted_entries.items():
        with allure.step(step_desc):
            check.equal(order_app.get(field_name), "Всего записей: 0",f"❌ ФР: Запись {label} не удалилась")

    # Повторяющийся текст ошибки при невозможности удаления заказа
    error_text = ("Нельзя удалить заказ с оформленными документами на груз, перевозку, "
                  "экспедирование, декларирование, счет, услугу. Удалите перечисленные документы и "
                  "повторите попытку удаления заказа.")

    # Проверки невозможности удаления заказа
    deleted_entries1 = {
        "del_window_file": ("Фаил", "16. Фаил, Удаление из формы"),
        "del_window_file1": ("Фаил", "17. Фаил, Удаление из таблицы Заказы"),
        "del_window_is": ("Исходящий счет", "18. Удален Исходящий счетиз формы"),
        "del_window_is1": ("Исходящий счет", "19. Удален Исходящий счет из таблицы Заказы"),
        "del_window_vs": ("Входящий счет", "20. Удален Входящий счетиз формы"),
        "del_window_vs1": ("Входящий счет", "21. Удален Входящий счет из таблицы Заказы"),
        "del_window_ip": ("Исходящий платеж", "22. Удален Исходящий платеж из формы"),
        "del_window_ip1": ("Исходящий платеж", "23. Удален Исходящий платеж из таблицы Заказы"),
        "del_window_vp": ("Входящий платеж", "24. Удален Входящий платеж из формы"),
        "del_window_vp1": ("Входящий платеж", "25. Удален Входящий платеж из таблицы Заказы"),
        "del_window_sea": ("Морская перевозка", "26. Удалена Морская перевозка из формы"),
        "del_window_sea1": ("Морская перевозка", "27. Удалена Морская перевозка из таблицы Заказы"),
        "del_window_auto": ("Автоперевозка", "28. Удалена Автоперевозка из формы"),
        "del_window_auto1": ("Автоперевозка", "29. Удалена Автоперевозка из таблицы Заказы"),
        "del_window_bul": ("Bulkership", "30. Удален Bulkership из формы"),
        "del_window_bul1": ("Bulkership", "31. Удален Bulkership из таблицы Заказы"),
        "del_window_con": ("Container", "32. Удален Container из формы"),
        "del_window_con1": ("Container", "33. Удален Container из таблицы Заказы"),
        "del_window_gtd": ("ГТД", "34. Удален ГТД из формы"),
        "del_window_gtd1": ("ГТД", "35. Удален ГТД из таблицы Заказы"),
        "del_window_exp": ("ГТД", "36. Удалено Экспедирование из формы"),
        "del_window_exp1": ("ГТД", "37. Удалено Экспедирование из таблицы Заказы"),
    }

    for field_name1, (label, step_desc) in deleted_entries1.items():
        with allure.step(step_desc):
            check.equal(order_app.get(field_name1), error_text, f"❌ ФР: Неверное сообщение при попытке удаления — {step_desc}")

    with allure.step("38. Сравниваем удалённый заказ с текущим в таблице Заказы"):
        check.is_false(order_app["delete_order"] == order_app["table_order"], "❌ ФР: номера одинаковые 1 заказ")

    with allure.step("39. Сравниваем удаление двух заказов в таблице Заказы"):
        check.is_false(order_app["table_order_del1"] == order_app["table_order_1"], "❌ ФР: номера одинаковые 2 заказа")
        check.is_false(order_app["table_order_del1"] == order_app["table_order_2"], "❌ ФР: номера одинаковые 2 заказа")
        check.is_false(order_app["table_order_del2"] == order_app["table_order_2"], "❌ ФР: номера одинаковые 2 заказа")
        check.is_false(order_app["table_order_del2"] == order_app["table_order_1"], "❌ ФР: номера одинаковые 2 заказа")
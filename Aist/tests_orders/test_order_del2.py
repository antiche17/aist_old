import pytest
import allure
from difflib import SequenceMatcher as f
from orders.order_del2 import WinAISTApp
import pytest_check as check


@pytest.fixture(scope="module")
def order_app():
    """Фикстура создает и возвращает приложение с созданным заказом"""
    app = WinAISTApp()
    order_data = app.order_del2()
    yield order_data
    app.close()

@allure.title("Проверка создание Входящий платеж в заказе. 19 проверок")
@pytest.mark.order(1)
def test_value_order(order_app):
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
        expected_text = "ещё 7 с оформленными документами на груз, перевозку, экспедирование, декларирование, счет."
        check.is_true(expected_text in order_app["del_window"],"❌ ФР: Описание оформления документов не найдено в окне удаления")

    # 5–10: Проверка удаления записей
    deleted_entries = {
        "del_is": ("Исходящий счет", "6. Удален Исходящий счет"),
        "del_vs": ("Входящий счет", "7. Удален Входящий счет"),
        "del_ip": ("Исходящий платеж", "8. Удален Исходящий платеж"),
        "del_vp": ("Входящий платеж", "9. Удален Входящий платеж"),
        "del_sea": ("Морская перевозка", "10. Удалена Морская перевозка"),
        "del_auto": ("Автоперевозка", "11. Удалена Автоперевозка"),
        "del_bul": ("Bulkership", "12. Удален Bulkership"),
        "del_con": ("Container", "13. Удален Container"),
        "del_gtd": ("ГТД", "14. Удален ГТД"),
        "del_exp": ("Экспедирование", "24. Удалено Экспедирование"),
    }

    for field_name, (label, step_desc) in deleted_entries.items():
        with allure.step(step_desc):
            check.equal(order_app.get(field_name), "Всего записей: 0",f"❌ ФР: Запись {label} не удалилась")

    # Повторяющийся текст ошибки при невозможности удаления заказа
    error_text = ("Нельзя удалить заказ с оформленными документами на груз, перевозку, "
                  "экспедирование, декларирование, счет. Удалите перечисленные документы и "
                  "повторите попытку удаления заказа.")

    # Проверки невозможности удаления заказа
    deleted_entries1 = {
        "del_window_is": ("Исходящий счет", "6. Удален Исходящий счет"),
        "del_window_vs": ("Входящий счет", "7. Удален Входящий счет"),
        "del_window_ip": ("Исходящий платеж", "8. Удален Исходящий платеж"),
        "del_window_vp": ("Входящий платеж", "9. Удален Входящий платеж"),
        "del_window_sea": ("Морская перевозка", "10. Удалена Морская перевозка"),
        "del_window_auto": ("Автоперевозка", "11. Удалена Автоперевозка"),
        "del_window_bul": ("Bulkership", "12. Удален Bulkership"),
        "del_window_con": ("Container", "13. Удален Container"),
        "del_window_gtd": ("ГТД", "14. Удален ГТД"),
        "del_window_exp": ("ГТД", "24. Удалено Экспедирование"),
    }

    for field_name1, (label, step_desc) in deleted_entries1.items():
        with allure.step(step_desc):
            check.equal(order_app.get(field_name1), error_text, f"❌ ФР: Неверное сообщение при попытке удаления — {step_desc}")

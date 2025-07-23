import pytest
import allure
from orders.order import WinAISTApp
import pytest_check as check
from datetime import datetime


@pytest.fixture(scope="module")
def order_app():
    """Фикстура создает и возвращает приложение с созданным заказом"""
    app = WinAISTApp()
    order_data = app.transportation()
    yield order_data
    app.close()


@allure.suite("Заказ")
@allure.title("Проверка создания и удаления перевозок")
@pytest.mark.order(1)
def test_sea_transportation(order_app):
    today = datetime.now().strftime("%d.%m.%Y %H:%M")
    allure.dynamic.label("Дата запуска", today)
    # морская перевозка
    with allure.step("1. Номер заказа с номером морской перевозки"):
        check.is_true(order_app["order_number"] in order_app["sea_order_number"], "❌ ФР: Не одинаковые данные")

    with allure.step("2. Проверяем тип перевозки"):
        check.equal(order_app["sea_type"], "Морская перевозка", "❌ ФР: Не Морская перевозка")

    with allure.step("3. Проверяем статус"):
        check.equal(order_app["sea_status"], "Черновик", "❌ ФР: Не Черновик")

    with allure.step("4. Проверяем приоритет"):
        check.equal(order_app["sea_priority"], "Средний", "❌ ФР: Не Средний")

    with allure.step("5. Проверяем ответственного"):
        check.equal(order_app["sea_otv"], order_app["order_dialog_otv"], "❌ ФР: Не одинаковые данные")

    with allure.step("6. Проверяем дату создания и модификации"):
        check.equal(order_app["sea_create_date"], order_app["sea_mode_date"], "❌ ФР: Не одинаковые данные")

    with allure.step("7. Проверяем отображение в таблице"):
        check.equal(order_app["sea_order_table"], order_app["sea_type"], "❌ ФР: Не одинаковые данные")

    with allure.step("8. Всего записей: 0"):
        check.equal(order_app["del_sea"], "Всего записей: 0", "❌ ФР: Не удалилось")

    # автоперевозка
    with allure.step("9. Сравниваем номер заказа с номером автоперевозки"):
        check.is_true(order_app["order_number"] in order_app["auto_order_number"], "❌ ФР: Не одинаковые данные")

    with allure.step("10. Проверяем тип перевозки"):
        check.equal(order_app["auto_type"], "Автоперевозка", "❌ ФР: Не одинаковые данные")

    with allure.step("11. Проверяем статус"):
        check.equal(order_app["auto_status"], "Черновик", "❌ ФР: Не одинаковые данные")

    with allure.step("12. Проверяем приоритет"):
        check.equal(order_app["auto_priority"], "Средний", "❌ ФР: Не одинаковые данные")

    with allure.step("13. Проверяем ответственного"):
        check.equal(order_app["auto_otv"], order_app["order_dialog_otv"], "❌ ФР: Не одинаковые данные")

    with allure.step("14. Проверяем дату создания и модификации"):
        check.equal(order_app["auto_create_date"], order_app["auto_mode_date"], "❌ ФР: Не одинаковые данные")

    with allure.step("15. Проверяем отображение в таблице"):
        check.equal(order_app["auto_order_table"], order_app["auto_type"], "❌ ФР: Не одинаковые данные")

    with allure.step("16. Всего записей: 0"):
        check.equal(order_app["del_auto"], "Всего записей: 0", "❌ ФР: Не удалилось")

# 7–15: Проверка удаления записей
    deleted_entries = {
        "sea_type_freight": ("Тип груза", "7. Пустой Тип груза"),
        "sea_class_freight": ("Класс груза", "8. Пустой Класс груза"),
        "sea_download_method": ("Способ загрузки", "9. Пустой Способ загрузки"),
        "sea_ref_freight": ("Референс груза", "10. Пустой Референс груза"),
        "sea_booking_reference": ("Букинг референс", "11. Пустой Тип груза"),
        "sea_ocean_line": ("Океанская линия", "12. Пустой Океанская линия"),
        "sea_ocean_konos": ("Океанская коносамент", "13. Пустой Океанская коносамент"),
        "sea_feeder_line": ("Фидерная линия", "14. Пустой Фидерная линия"),
        "sea_feeder_konos": ("Фидерн. коносамент", "15. Пустой Фидерн. коносамент"),

        'auto_type_freight': ("Тип груза", "7. Пустой Тип груза"),
        'auto_class_freight': ("Класс груза", "8. Пустой Класс груза"),
        'auto_download_method': ("Способ загрузки", "9. Пустой Способ загрузки"),
        'auto_ref_freight': ("Референс груза", "10. Пустой Референс груза"),
        'auto_carrier': ("Перевозчик", "10. Пустой Перевозчик"),
        'auto_cmr': ("Номер CMR", "10. Пустой Номер CMR"),
        'auto_cmr_por': ("Номер CMR прож.", "10. Номер CMR порож."),
    }

    for field_name, (label, step_desc) in deleted_entries.items():
        with allure.step(step_desc):
            check.is_false(order_app.get(field_name), f"❌ ФР: Поле {label} не пустое")
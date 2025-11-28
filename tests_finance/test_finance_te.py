import pytest
import allure
from orders.finance import WinAISTApp
import pytest_check as check
from locators.format_data import compare_dates


@pytest.fixture(scope="module")
def order_app():
    print("Проверка ВС")
    app = WinAISTApp()
    order_data = app.finance_te()
    yield order_data
    print("[TEARDOWN] Закрытие WinAISTApp")
    try:
        # Прямое жесткое закрытие минуя проблемные методы
        app.fun.app.kill()  # без soft=True
    except Exception as e:
        print(f"При закрытии возникла ошибка: {e}")
        # Игнорируем ошибку, так как приложение все равно должно закрыться

@allure.suite("Проверка ТЕ в счете")
@allure.title("Проверка ТЕ в счете 10 проверок")
def test_freight(order_app):
    with allure.step("1. Сравниваем номер Container"):
        check.equal(order_app["order_dialog_number"].replace(" ", ""), order_app["container_con"], "❌ ФР: Номер Container не одинаковые")

    with allure.step("2. Сравниваем номер Bulkership"):
        check.equal(order_app["bul_dialog_number"], order_app["container_bul"], "❌ ФР: Номер Bulkership не одинаковые")

    with allure.step("3. Сравниваем ТЕ в услуги в таблице Все услуги"):
        check.is_true(order_app["te_service"]in order_app["te_service_tab"], "❌ ФР: ТЕ в услуги в таблице Все услуги не одинаковые")

    with allure.step("4. Сравниваем ТЕ в услуги в таблице Заказы"):
        check.equal(order_app["te_service"].replace("; ", ","), order_app["te_order_tab"], "❌ ФР: ТЕ в услуги в таблице Заказы не одинаковые")

    with allure.step("5. Сравниваем ТЕ Container в заказе"):
        check.equal(order_app["con_dialog_te"], order_app["te_order_con"], "❌ ФР: ТЕ Container в заказе не одинаковые")

    with allure.step("6. Сравниваем тип ТЕ Container в заказе"):
        check.equal(order_app["con_dialog_type"], order_app["type_order_con"], "❌ ФР: Тип ТЕ Container в заказе не одинаковые")

    with allure.step("7. Сравниваем номер ТЕ Container в заказе"):
        check.equal(order_app["order_dialog_number"].replace(" ", ""), order_app["number_order_con"], "❌ ФР: Номер ТЕ Container в заказе не одинаковые")

    with allure.step("8. Сравниваем ТЕ Bulkership в заказе"):
        check.equal(order_app["bul_dialog_te"], order_app["te_order_bul"], "❌ ФР: ТЕ Bulkership в заказе не одинаковые")

    with allure.step("9. Сравниваем тип ТЕ Bulkership в заказе"):
        check.equal(order_app["bul_dialog_type"], order_app["type_order_bul"], "❌ ФР: Тип ТЕ Bulkership в заказе не одинаковые")

    with allure.step("10. Сравниваем номер ТЕ Bulkership в заказе"):
        check.equal(order_app["bul_dialog_number"], order_app["number_order_bul"], "❌ ФР: Номер ТЕ Bulkership в заказе не одинаковые")

    with allure.step("11. Сравниваем окно удаление ТЕ с текстом"):
        check.equal(order_app["te_del_chek1"], "Это действие также удалит все записи, связанные с данной.  Внимание: удаленные записи не восстанавливаются.    Вы хотите продолжить удаление?",
                    "❌ ФР: окно удаление ТЕ с текстом не одинаковые")

    with allure.step("12. Сравниваем окно удаление ТЕ с текстом"):
        check.equal(order_app["te_del_chek2"], "Это действие также удалит все записи, связанные с данной.  Внимание: удаленные записи не восстанавливаются.    Вы хотите продолжить удаление?",
                    "❌ ФР: окно удаление ТЕ с текстом не одинаковые")

    with allure.step("13. Всего 0 поле удаления ТЕ из счета"):
        check.equal(order_app["te_del_0"], "Всего: 0", "❌ ФР: Всего не 0 в счете")

    with allure.step("14. Всего 0 поле удаления счета"):
        check.equal(order_app["te_del_chek"], "Всего записей: 0", "❌ ФР: Всего не 0 в все счета")
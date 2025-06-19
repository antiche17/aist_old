import pytest
import allure
from orders.order import WinAISTApp
from difflib import SequenceMatcher as f
import pytest_check as check


@pytest.fixture(scope="module")
def order_app():
    """Фикстура создает и возвращает приложение с обновленным заказом"""
    app = WinAISTApp()
    order_data = app.create_order_dr()
    yield order_data
    app.close()

@allure.title("Проверка создания заказа с типом 'Другие услуги', 20 проверок")
@pytest.mark.order(1)
def test_create_other_services_order(order_app):
    with allure.step("1. Проверка номера заказа"):
        check.is_false(order_app["order_number"] is None, "❌ ФР: Должно быть поле заполнено")

    with allure.step("2. Проверка типа заказа"):
        check.equal(order_app["order_dialog_type"], "Другие услуги", "❌ ФР: Поле с другим значением, но должно быть Другие услуги")

    with allure.step("3. Проверка типа заказа"):
        check.equal(order_app["order_dialog_type"], order_app["order_type"], "❌ ФР: Не одинаковые, но должно быть одинаковые")

    with allure.step("4. Проверка статуса заказа"):
        check.equal(order_app["order_status"], "Черновик", "❌ ФР: Поле с другим значением, но должно быть Черновик")

    with allure.step("5. Проверка приоритета"):
        check.equal(order_app["order_priority"], "Средний", "❌ ФР: Поле с другим значением, но должно быть Средний")

    with allure.step("6. Проверка Ответственного"):
        check.equal(order_app["order_dialog_otv"], order_app["order_otv"], "❌ ФР: Не одинаковые ответственные, но должны быть одинаковыми")


    with allure.step("7. Проверка клиента"):
        check.equal(order_app["order_dialog_client"], order_app["order_client"], "❌ ФР: Не одинаковые клиенты, но должны быть одинаковыми")

    with allure.step("8. Проверка Дата создания = Дата изменения"):
        check.equal(f(None, order_app["order_create_date"], order_app["order_create_mod"]).ratio() > 65,"❌ ФР: Поля не одинаковые, но должно быть одинаковые, выставлено 65")

    with allure.step("9. Проверка Дата завершения"):
        check.equal(order_app["order_completion_date"], "...", "❌ ФР: Поле с другим значением, но должно быть ... ")

    with allure.step("10. Референс клиента пусто"):
        check.is_not_none(order_app["order_reference"], "❌ ФР: Поле не пустое, но должно быть поле пустым")


    with allure.step("11. Есть вкладка Счета"):
        check.equal(order_app["order_tab_check"], "Счета", "❌ ФР: Поле с другим значением, но должно быть Счета")

    with allure.step("12. Есть вкладка Файлы"):
        check.equal(order_app["order_tab_file"], "Файлы", "❌ ФР: Поле с другим значением, но должно быть Файлы")

    with allure.step("13. Есть вкладка Услуги"):
        check.equal(order_app["order_tab_services"], "Услуги", "❌ ФР: Поле с другим значением, но должно быть Услуги")

    with allure.step("14. Примечание"):
        check.is_not_none(order_app["order_note"], "❌ ФР: Поле не пустое, но должно быть поле пустым")


    with allure.step("15. Проверка номера в таблице"):
        check.equal(None, f(order_app["order_number"], order_app["table_order"]).ratio() > 65, "❌ ФР: Поля не одинаковые, выставлено 65")

    with allure.step("16. Проверка типа в таблице"):
        check.equal(order_app["order_type"], order_app["table_type"], "❌ ФР: Поля не одинаковые")

    with allure.step("17. Проверка статуса в таблице"):
        check.equal(order_app["order_status"], order_app["table_status"], "❌ ФР: Поля не одинаковые")

    with allure.step("18. Проверка приоритета в таблице"):
        check.equal(order_app["order_priority"], order_app["table_priority"], "❌ ФР: Поля не одинаковые")

    with allure.step("19. Проверка клиента в таблице"):
        check.equal(order_app["order_client"], order_app["table_client"], "❌ ФР: Поля не одинаковые")

    with allure.step("20. Проверка даты создания в таблице"):
        check.equal(None, f(order_app["table_date"], order_app["order_create_date"]).ratio() > 60, "❌ ФР: Поля не одинаковые")


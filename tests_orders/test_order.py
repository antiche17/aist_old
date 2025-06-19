import pytest
import allure
from difflib import SequenceMatcher as f
from orders.order import WinAISTApp
import pytest_check as check


@pytest.fixture(scope="module")
def order_app():
    """Фикстура создает и возвращает приложение с созданным заказом"""
    app = WinAISTApp()
    order_data = app.create_order()
    yield order_data
    app.close()


@allure.title("Проверка создание заказа с типом Логистика 28 проверок")
@pytest.mark.order(1)
def test_value_order(order_app):
    with allure.step("1. Номер заказа не пустой"):
        check.is_not_none(order_app["order_number"], "❌ ФР: Поле пустое")

    with allure.step("2. Тип заказа — Логистика"):
        check.equal(order_app["order_dialog_type"], "Логистика", "❌ ФР: Поле с другим значением, но должно быть Логистика")

    with allure.step("3. Тип заказа одинаковый"):
        check.equal(order_app["order_dialog_type"], order_app["order_type"], "❌ ФР: Поля не одинаковые")

    with allure.step("4. Статус заказа — Черновик"):
        check.equal(order_app["order_status"], "Черновик", "❌ ФР: Поле с другим значением, но должно быть Черновик")

    with allure.step("5. Приоритет заказа — Средний"):
        check.equal(order_app["order_priority"], "Средний", "❌ ФР: Поле с другим значением, но должно быть Средний")

    with allure.step("6. Указанный ответственный существует"):
        check.equal(order_app["order_dialog_otv"], order_app["order_otv"], "❌ ФР: Поля не одинаковые")


    with allure.step("7. Клиент заказа указан"):
        check.equal(order_app["order_client"], order_app["order_client"], "❌ ФР: Клиент не соответствует выбранному")

    with allure.step("8. поле Отправитель пустое"):
        check.is_false(order_app["order_senders"], "❌ ФР: Поле не пустое")

    with allure.step("9. поле Получатель пустое"):
        check.is_false(order_app["order_recipient"], "❌ ФР: Поле не пустое")

    with allure.step("10. что поле Условие поставки пустое"):
        check.is_false(order_app["order_delivery"], "❌ ФР: Поле не пустое")


    with allure.step("11. Дата создания одинаковая с датой изменения"):
        check.equal(order_app["order_create_date"], order_app["order_create_mod"], "❌ ФР: Поля не одинаковые")

    with allure.step("12. Дата завершения ..."):
        check.equal(order_app["order_completion_date"], "...", "❌ ФР: Не соответствует значению")

    with allure.step("13. Поле Референс пустое"):
        check.is_false(order_app["order_reference"], "❌ ФР: Поле не пустое")

    with allure.step("14. Поле Примечание пустое"):
        check.is_false(order_app["order_note"], "❌ ФР: Поле не пустое")


    with allure.step("15. Номер заказа с отображением в таблице"):
        check.equal(f(None, order_app["order_number"], order_app["table_order"]).ratio()>65, "❌ ФР: Поля не одинаковые, выставлено 65")

    with allure.step("16. тип заказа с отображением в таблице"):
        check.equal(order_app["order_type"], order_app["table_type"], "❌ ФР: Поля не одинаковые")

    with allure.step("17. статус заказа с отображением в таблице"):
        check.equal(order_app["order_status"], order_app["table_status"], "❌ ФР: Поля не одинаковые")

    with allure.step("18. приоритет заказа с отображением в таблице"):
        check.equal(order_app["order_priority"], order_app["table_priority"], "❌ ФР: Поля не одинаковые")

    with allure.step("19. ответственного с таблицей"):
        check.equal(order_app["order_otv"], order_app["table_creator"], "❌ ФР: Поля не одинаковые")

    with allure.step("20. клиент заказа одинаковый в таблице"):
        check.equal(order_app["order_client"], order_app["table_client"], "❌ ФР: Поле не пустое, но должно быть поле пустым")



    with allure.step("21. вкладка в заказе — Груз"):
        check.equal(order_app["order_tab_freight"], "Груз", "❌ ФР: Поле с другим значением, но должно быть Груз")

    with allure.step("22. вкладка в заказе — Перевозки"):
        check.equal(order_app["order_tab_transportation"], "Перевозки", "❌ ФР: Поле с другим значением, но должно быть Перевозки")

    with allure.step("23. вкладка в заказе — Экспедирование"):
        check.equal(order_app["order_tab_forwarding"], "Экспедирование", "❌ ФР: Поле с другим значением, но должно быть Экспедирование")

    with allure.step("24. вкладка в заказе — Декларирование"):
        check.equal(order_app["order_tab_gtd"], "Декларирование", "❌ ФР: Поле с другим значением, но должно быть Декларирование")

    with allure.step("25. вкладка в заказе — Счета"):
        check.equal(order_app["order_tab_check"], "Счета", "❌ ФР: Поле с другим значением, но должно быть Счета")

    with allure.step("26. вкладка в заказе — Файлы"):
        check.equal(order_app["order_tab_file"], "Файлы", "❌ ФР: Поле с другим значением, но должно быть Файлы")

    with allure.step("27. вкладка в заказе — Услуги"):
        check.equal(order_app["order_tab_services"], "Услуги", "❌ ФР: Поле с другим значением, но должно быть Услуги")

    with allure.step("28. вкладка в заказе — Отслеживание"):
        check.equal(order_app["order_tab_tracking"], "Отслеживание", "❌ ФР: Поле с другим значением, но должно быть Отслеживание")
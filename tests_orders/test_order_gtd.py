import pytest
import allure
from orders.order import WinAISTApp
import pytest_check as check
from locators.format_data import compare_dates


@pytest.fixture(scope="module")
def order_app():
    print("Создание в заказе ГТД.\nСоздание ТЕ для ГТД.\nПроверка, что ГТД не сохраняется без ТЕ\nДобавление ТЕ из заказа\nДобавление ТЕ из К/С партии\nУдаление ГТД.")
    app = WinAISTApp()
    try:
        order_data = app.gtd()
        yield order_data
    finally:
        print("[TEARDOWN] Закрытие WinAISTApp")
        app.close()


@allure.suite("ГТД в заказе" )
@allure.title("Проверка данных заказа и ГТД 38"
              " проверок")
@pytest.mark.order(1)
def test_full_order_validation(order_app):
    with allure.step("1. Проверка номера заказа"):
        check.is_true(order_app["gtd_order_number"] in order_app["order_number"], "❌ ФР: Не одинаковые данные")

    with allure.step("2. Проверка клиента заказа и клиента в ГТД"):
        check.equal(order_app["order_dialog_client"], order_app["gtd_client"], "ФР: Клиент не соответствует в заказе")

    with allure.step("3. Проверка процедуры ГТД"):
        check.equal(order_app["procedure_gtd"], "ИМ 40", "ФР: Процедура не ИМ 40")

    with allure.step("4. Без ТЕ не создаётся"):
        check.equal(order_app["order_te_not"], "Коносаментная партия должна содержать хотя бы один контейнер", "ФР: Нет окна или текст поменялся")

    with allure.step("5. Сравнение клиента"):
        check.equal(order_app["gtd_client"], order_app["order_dialog_client"], "❌ ФР: Не одинаковые данные")

    steps_to_check = [
        ("6. Экспедитор", ["gtd_forwarding"]),
        ("7. Отправитель", ["gtd_sender"]),
        ("8. План приход", ["gtd_plan_arrival"]),
        ("9. План судно", ["gtd_plan_ship"]),
        ("10. Получение документов", ["gtd_doc"]),
        ("11. Пост", ["gtd_post"]),
        ("12. СВХ", ["gtd_svh"]),
        ("13. Декларант", ["gtd_declarant"]),
        ("14. Подача", ["gtd_supply"]),
        ("15. Выпуск", ["gtd_release"]),
        ("16. Лички", ["gtd_pers"]),
        ("17. Декл. ТНВЭД", ["gtd_decl_te"]),
        ("18. Реал. ТНВЭД", ["gtd_real_te"]),
        ("21. Вес (брутто)", ["gtd_brutto"]),
        ("22. Вес (нетто)", ["gtd_netto"]),
        ("23. Цена подача", ["gtd_price_p"]),
        ("24. Цена выпуск", ["gtd_price_v"]),
        ("25. Платежи", ["gtd_payment"]),
        ("26. ТК", ["gtd_tk"]),
        ("27. КТС", ["gtd_kts"]),
        ("28. Обеспечение", ["gtd_guarantee"]),
        ("29. Пени", ["gtd_peny"]),
        ("30. Импортер", ["gtd_receiver"]),
        ("31. Контракт", ["gtd_contract"]),
        ("32. Сумма", ["gtd_sum"]),
        ("33. Примечание", ["gtd_note"]),
        ("34. Номер", ["gtd_forwarding"]),
        ("35. Список", ["gtd_sender"]),
        ("36. План прибытия", ["gtd_plan_arrival"]),
        ("37. Курс доллара", ["gtd_dol"]),
        ("38. Курс евро", ["gtd_evr"]),
        ("39. № ГТД", ["gtd_number"]),

    ]

    for step_name, fields in steps_to_check:
        with allure.step(step_name):
            for field in fields:
                value = order_app.get(field)
                check.is_false(value, f"❌ ФР: поле '{field}' должно быть пустым, но получено: {value}")

    # Проверка с гридом
    with allure.step("40. Сравнение Клиентов в гриде"):
        check.equal(order_app["gtd_client"], order_app["gtd_client_tab"], "ФР: Клиенты в гриде не одинаковые")

    with allure.step("40. Сравнение Декл. груз в гриде"):
        check.equal(order_app["gtd_decl_te_mod"], order_app["gtd_decl_tab"], "ФР: Декл. груз в гриде не одинаковые")

    with allure.step("40. Сравнение Приход груза в гриде"):
        compare_dates(order_app["gtd_plan_ship_mod"], order_app["gtd_arrival_tab"], "ФР: Приход груза в гриде не одинаковые")

    with allure.step("40. Сравнение Пост в гриде"):
        check.equal(order_app["gtd_post_mod"], order_app["gtd_post_tab"], "ФР: Пост в гриде не одинаковые")

    with allure.step("40. Сравнение Номер ТЕ в гриде"):
        check.equal(order_app["number_te"], order_app["gtd_container_tab"], "ФР: Номер ТЕ в гриде не одинаковые")

    with allure.step("40. Сравнение Вес (Брутто) в гриде"):
        check.is_true(order_app["gtd_brutto_mod"] in order_app["gtd_brutto_tab"], "ФР: Вес (Брутто) в гриде не одинаковые")

    with allure.step("40. Сравнение Подача ГТД в гриде"):
        compare_dates(order_app["gtd_supply_mod"], order_app["gtd_supply_tab"], "ФР: Подача ГТД в гриде не одинаковые")

    with allure.step("40. Сравнение Контракт в гриде"):
        check.equal(order_app["gtd_contract_mod"], order_app["gtd_contract_tab"], "ФР: Контракт в гриде не одинаковые")

    with allure.step("40. Сравнение Импортер в гриде"):
        check.is_true(order_app["gtd_receiver_mod"] in order_app["gtd_importer_tab"], "ФР: Импортер в гриде не одинаковые")

    with allure.step("40. Сравнение Выпуск ГТД в гриде"):
        compare_dates(order_app["gtd_release_mod"], order_app["gtd_release_tab"], "ФР: Выпуск ГТД в гриде не одинаковые")

    with allure.step("40. Сравнение № ГТД в гриде"):
        check.equal(order_app["gtd_number_mod"], order_app["gtd_number_tab"], "ФР: № ГТД в гриде не одинаковые")

    with allure.step("40. Сравнение Создан дата в гриде"):
        check.is_true(order_app["gtd_created_tab"], "ФР: Создан дата в гриде пустое")

    with allure.step("40. Сравнение Сумма инвойса в гриде"):
        check.is_true(order_app["gtd_sum_mod"] in order_app["gtd_sum_tab"], "ФР: Сумма инвойса в гриде не одинаковые")

    with allure.step("40. Сравнение Примечание в гриде"):
        check.equal(order_app["gtd_note_mod"], order_app["gtd_note_tab"], "ФР: Примечание в гриде не одинаковые")

    with allure.step("40. Сравнение Платежи в гриде"):
        check.is_true(order_app["gtd_payment_mod"] in order_app["gtd_payments_tab"], "ФР: Платежи в гриде не одинаковые")

    with allure.step("40. Сравнение № Лички в гриде"):
        check.equal(order_app["gtd_pers_mod"], order_app["gtd_personal_tab"], "ФР: № Лички в гриде не одинаковые")

    with allure.step("40. Сравнение Декларант в гриде"):
        check.equal(order_app["gtd_declarant_mod"], order_app["gtd_declarant_tab"], "ФР: Декларант в гриде не одинаковые")
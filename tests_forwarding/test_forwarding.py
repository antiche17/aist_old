from difflib import SequenceMatcher
from orders.forwarding import WinAISTApp
import pytest
import allure
import pytest_check as check
import locale
from datetime import datetime


MONTHS_RU_EN = {
    'января': 'January', 'февраля': 'February', 'марта': 'March',
    'апреля': 'April', 'мая': 'May', 'июня': 'June',
    'июля': 'July', 'августа': 'August', 'сентября': 'September',
    'октября': 'October', 'ноября': 'November', 'декабря': 'December'
}

def normalize_date(date_str):
    date_str = date_str.replace("г.", "").strip()
    # Преобразуем только если месяц на русском
    for ru, en in MONTHS_RU_EN.items():
        if ru in date_str:
            date_str = date_str.replace(ru, en)
            break
    # Устанавливаем английскую локаль временно
    locale.setlocale(locale.LC_TIME, 'C')
    formats = ["%d %B %Y", "%d.%m.%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Не удалось распознать формат даты: {date_str}")

def compare_dates(date1, date2, error_message):
    assert normalize_date(date1) == normalize_date(date2), error_message

@pytest.fixture(scope="module")
def order_app():
    print("[SETUP] Запуск фикстуры order_app")
    app = WinAISTApp()
    order_data = app.forwarding()
    yield order_data
    print("[TEARDOWN] Закрытие WinAISTApp")
    app.close()

def check_equal_dates(value1, value2, field_name):
    normalized1 = normalize_date(value1)
    normalized2 = normalize_date(value2)
    check.equal(normalized1, normalized2, f"❌ ФР: Не одинаковый {field_name}")

@allure.title("Проверка Таблицы Экспедирование 72 проверки")
@pytest.mark.order(1)
def test_forwarding(order_app):
    with allure.step("1. Портовое"):
        check.equal(order_app["forwarding_dialog_type"], "Портовое", "❌ ФР: Не Портовое тип")

    with allure.step("2. Клиент"):#потом
        check.equal(order_app["forwarding_dialog_type"], "Портовое", "❌ ФР: Клиенты не одинаковые")

    with allure.step("3. Номер заказа"):
        check.is_true(SequenceMatcher(None, order_app["forwarding_dialog_number"], order_app["forwarding_order_number"]).ratio() >= 0.3, "❌ Номер заказа не одинаковые на 30%")

    with allure.step("4. Ответственный"):
        check.equal(order_app["forwarding_dialog_otv"], order_app["forwarding_otv"], "❌ ФР: Ответственные не одинаковые")

    with allure.step("5. Портовое сравниваем"):
        check.equal(order_app["forwarding_dialog_type"], order_app["forwarding_type"], "❌ ФР: Портовое не одинаковые")

    with allure.step("6. Статус Черновик"):
        check.equal(order_app["forwarding_status"], "Черновик", "❌ ФР: Не Статус Черновик")

    with allure.step("7. Приоритет Средний"):
        check.equal(order_app["forwarding_priority"], "Средний", "❌ ФР: Не Средний Приоритет")

    with allure.step("8. Дата создания и Дата изменения сравниваем"):
        check.equal(order_app["forwarding_create_date"], order_app["forwarding_mode_date"], "❌ ФР: Дата создания и Дата изменения не одинаковые")

    with allure.step("9. Дата завершения"):
        check.equal(order_app["forwarding_finish_date"], "...", "❌ ФР: Дата завершения не ...")

    with allure.step("10. Вкладка Информация"):
        check.equal(order_app["tab_info"], "Информация", "❌ ФР: Нет Информация вкладки")

    with allure.step("11. Вкладка Экспедируемый груз"):
        check.equal(order_app["tab_forwarding"], "Экспедируемый груз", "❌ ФР: Нет Экспедируемый груз вкладки")

    with allure.step("12. Вкладка Услуги"):
        check.equal(order_app["tab_services"], "Услуги", "❌ ФР: Нет Услуги вкладки")

    with allure.step("13. Вкладка Файлы"):
        check.equal(order_app["tab_file"], "Файлы", "❌ ФР: Нет Файлы вкладки")

    with allure.step("14. Статус сравниваем"):
        check.is_false(order_app["forwarding_status"]== order_app["forwarding_status_mod"], "❌ ФР: Статус одинаковые")

    with allure.step("15. Приоритет сравниваем"):
        check.is_false(order_app["forwarding_priority"]== order_app["forwarding_priority_mod"], "❌ ФР: Приоритет одинаковые")

    with allure.step("16. Примечание сравниваем"):
        check.is_false(order_app["forwarding_note"]== order_app["forwarding_note_mod"], "❌ ФР: Примечание одинаковые")

    with allure.step("17. Ответсвтенный сравниваем"):
        check.is_false(order_app["forwarding_otv"]== order_app["forwarding_otv_mod"], "❌ ФР: Ответсвтенный одинаковые")

    with allure.step("18. Экспедитор сравниваем"):
        check.is_false(order_app["forwarding_dialog_type"]== order_app["forwarding_type_freight_mod"], "❌ ФР: Экспедитор одинаковые")

    with allure.step("19. Номинация эксп сравниваем"):
        check.is_false(order_app["forwarding_dialog_type"]== order_app["forwarding_class_freight_mod"], "❌ ФР: Номинация эксп одинаковые")

    with allure.step("20. Телекс-релиз сравниваем"):
        check.is_false(order_app["forwarding_dialog_type"]== order_app["forwarding_download_method_mod"], "❌ ФР: Телекс-релиз одинаковые")

    with allure.step("21. Получение докум сравниваем"):
        check.is_false(order_app["forwarding_dialog_type"]== order_app["forwarding_ref_freight_mod"], "❌ ФР: Получение докум одинаковые")

    with allure.step("22. ТЕ bulkership"):
        check.equal(order_app["order_dialog_te"], order_app["bul_type_form"], "❌ ФР: Не bulkership")

    with allure.step("23. Тип ТЕ"):
        check.equal(order_app["order_dialog_type"], order_app["bul_type_te_form"], "❌ ФР: Тип ТЕ не одинаковые")

    with allure.step("24 Количество ТЕ"):
        check.equal(order_app["order_dialog_quantity"], order_app["bul_quantity_form"], "❌ ФР: Количество ТЕ не одинаковые")

    with allure.step("25. Ед. измерения ТЕ"):
        check.equal(order_app["order_dialog_uom"], order_app["bul_uom_form"], "❌ ФР: Ед. измерения ТЕ не одинаковые")

    with allure.step("26. Номер ТЕ"):
        check.equal(order_app["order_dialog_number"], order_app["bul_te_number_form"], "❌ ФР: Номер ТЕ не одинаковые")

    with allure.step("27. ДО/ДО1"):
        check.is_not_none(order_app.get("bul_do_form"), "❌ ДО/ДО1 Поле пустое")

    with allure.step("28. bulkership Примечание"):
        check.is_not_none(order_app.get("bul_note_form"), "❌ Поле пустое bulkership Примечание")

    with allure.step("25. Тип заказа"):
        check.equal(order_app["order_type_form"], "Логистика", "❌ ФР: Не Логистика")

    with allure.step("26. Клиент заказа"):
        check.equal(order_app["forwarding_dialog_client"], order_app["order_client_form"], "❌ ФР: Клиенты заказа не одинаковые")

    with allure.step("27. Ответсвенный"):
        check.equal(order_app["forwarding_dialog_otv"], order_app["order_otv_form"], "❌ ФР: Ответсвенный не одинаковые")

    with allure.step("28. Тип Экспедирования в закзе"):
        check.equal(order_app["forwarding_dialog_type"], order_app["order_forwading_item"], "❌ ФР: Тип Экспедирования не одинаковые")

    with allure.step("30. Статус Экспедирования в заказе"):
        check.equal(order_app["forwarding_status_mod"], order_app["order_forwading_status"], "❌ ФР: Статус Экспедирования не одинаковые")

    with allure.step("31. Отвественный Экспедирования в заказе"):
        check.equal(order_app["forwarding_otv_mod"], order_app["order_forwading_otv"], "❌ ФР: Отвественный Экспедирования не одинаковые")

    with allure.step("32. Экспедитор Экспедирования в заказе"):
        check.equal(order_app["forwarding_type_freight_mod"], order_app["order_forwading_forward"], "❌ ФР: Экспедитор Экспедирования не одинаковые")

    with allure.step("33. Номер ТЕ Экспедирования в заказе"):
        check.equal(order_app["order_forwading_te"], "1", "❌ ФР: Номер ТЕ Экспедирования не одинаковые")

    with allure.step("34. Дата создания Экспедирования в заказе"):
        check.is_true(SequenceMatcher(None, order_app["forwarding_create_date"], order_app["order_forwading_data_create"]).ratio() >= 0.3,
                      "❌ ФР: Дата создания Экспедирования не одинаковые на 30%")

    with allure.step("35. Примечание Экспедирования в заказе"):
        check.equal(order_app["forwarding_note_mod"], order_app["order_forwading_note"], "❌ ФР: Примечание Экспедирования не одинаковые")

    with allure.step("36. Фид. коносамент в вкладке Экспедируемый груз"):
        check.equal(order_app["feeder_konos"], order_app["order_forwarding_fid_kons1"], "❌ ФР: Фид. коносамент не одинаковые")

    with allure.step("37. План. приб. в вкладке Экспедируемый груз"):
        check.equal(order_app["plan_arrival"], order_app["order_forwarding_plan_arrival1"], "❌ ФР: План. приб. не одинаковые")

    with allure.step("38. Факт. приб в вкладке Экспедируемый груз"):
        check.equal(order_app["fact_arrival"], order_app["order_forwarding_fact_arrival1"], "❌ ФР: Факт. приб не одинаковые")

    with allure.step("39. Фид. Линия в вкладке Экспедируемый груз"):
        check.equal(order_app["feeder_line"], order_app["order_forwarding_fid_line1"], "❌ ФР: Фид. Линия не одинаковые")

    with allure.step("40. Порт в вкладке Экспедируемый груз"):
        check.equal(order_app["port"], order_app["order_forwarding_port1"], "❌ ФР: Порт не одинаковые")

    with allure.step("41. Терминал в вкладке Экспедируемый груз"):
        check.equal(order_app["terminal"], order_app["order_forwarding_terminal1"], "❌ ФР: Терминал не одинаковые")

    with allure.step("42. ТЕ в вкладке Экспедируемый груз"):
        check.equal(order_app["order_dialog_te"], order_app["order_forwarding_te1"], "❌ ФР: ТЕ не одинаковые")

    with allure.step("43. Тип ТЕ в вкладке Экспедируемый груз"):
        check.equal(order_app["bul_type_te_form"], order_app["order_forwarding_te_type1"], "❌ ФР: Тип ТЕ не одинаковые")

    with allure.step("44. Номер ТЕ в вкладке Экспедируемый груз"):
        check.equal(order_app["order_dialog_number"], order_app["order_forwarding_te_number1"], "❌ ФР: Номер ТЕ не одинаковые")

    with allure.step("45. Релиз в вкладке Экспедируемый груз"):
        compare_dates(order_app["forwarding_download_method_mod"], order_app["order_forwarding_release1"], "❌ ФР: Релиз не одинаковые")

    with allure.step("46. Получение докум. в вкладке Экспедируемый груз"):
        compare_dates(order_app["forwarding_ref_freight_mod"], order_app["order_forwarding_doc1"], "❌ ФР: Получение докум не одинаковые")

    with allure.step("47. Номинация эксп. в вкладке Экспедируемый груз"):
        compare_dates(order_app["forwarding_class_freight_mod"], order_app["order_forwarding_nomination1"], "❌ ФР: Номинация эксп. не одинаковые")

    with allure.step("48. ДО/ДО1 в вкладке Экспедируемый груз"):
        compare_dates(order_app["bul_do_form"], order_app["order_forwarding_do_do1"], "❌ ФР: ДО/ДО1 не одинаковые")

    with allure.step("49. Примечание в вкладке Экспедируемый груз"):
        check.equal(order_app["forwarding_note_mod"], order_app["order_forwarding_note1"], "❌ ФР: Примечание не одинаковые")

    # В таблице Экспедиция
    with allure.step("50. Номер заказа в таблице"):
        check.equal(order_app["forwarding_dialog_number"], order_app["order_table1"], "❌ ФР: Номер заказа в таблице не одинаковые")

    with allure.step("51. Тип экспедирования в таблице"):
        check.equal(order_app["forwarding_dialog_type"], order_app["type_table1"], "❌ ФР: Тип экспедирования в таблице не одинаковые")

    with allure.step("52. Статус в таблице"):
        check.equal(order_app["forwarding_status_mod"], order_app["status_table1"], "❌ ФР: Статус в таблице не одинаковые")

    with allure.step("53. Приоритет в таблице"):
        check.equal(order_app["forwarding_priority_mod"], order_app["priority_table1"], "❌ ФР: Приоритет в таблице не одинаковые")

    with allure.step("54. Ответственный в таблице"):
        check.equal(order_app["forwarding_otv_mod"], order_app["responsible_table1"], "❌ ФР: Ответственный в таблице не одинаковые")

    with allure.step("55. Экспедитор в таблице"):
        check.equal(order_app["forwarding_type_freight_mod"], order_app["expeditor_table1"], "❌ ФР: Экспедитор в таблице не одинаковые")

    with allure.step("56. Телекс-релиз в таблице"):
        compare_dates(order_app["forwarding_download_method_mod"], order_app["telex_release_table1"], "❌ ФР: Телекс-релиз в таблице не одинаковые")

    with allure.step("57. Получение докум в таблице"):
        compare_dates(order_app["forwarding_ref_freight_mod"], order_app["receive_doc_table1"], "❌ ФР: Получение докум в таблице не одинаковые")

    with allure.step("58. Номинация эксп в таблице"):
        compare_dates(order_app["forwarding_class_freight_mod"], order_app["nomination_table1"], "❌ ФР: Номинация эксп в таблице не одинаковые")

    with allure.step("59. Примечание в таблице"):
        check.equal(order_app["forwarding_note_mod"], order_app["note_table1"], "❌ ФР: Примечание в таблице не одинаковые")

    with allure.step("60. Кем создан в таблице"):
        check.equal(order_app["forwarding_dialog_otv"], order_app["created_by_table1"], "❌ ФР: Кем создан в таблице не одинаковые")

    with allure.step("62. Дата создания в таблице"):
        check.is_true(SequenceMatcher(None, order_app["forwarding_create_date"], order_app["created_date_table1"]).ratio() >= 0.3,
                      "❌ ФР: Дата создания Экспедирования не одинаковые на 30%")

    with allure.step("63. Дата изменения в таблице"):
        check.is_true(SequenceMatcher(None, order_app["forwarding_mode_date"], order_app["updated_date_table1"]).ratio() >= 0.4,
            "❌ ФР: Дата изменения в таблице не одинаковые на 40%")

    with allure.step("64. Номер экспедирования в таблице"):
        check.is_true(SequenceMatcher(None, order_app["forwarding_number_header"], order_app["forwarding_order_number"]).ratio() >= 0.3, "❌ ФР: Номер экспедирования в таблице не одинаковые на 30%")

    with allure.step("65. Кол-во ТЕ в таблице"):
        check.equal(order_app["te_count_header"], "1", "65.❌ ФР: Кол-во ТЕ в экспедиции и таблице не одинаковые")


        steps_to_check = [
            ("66. Экспедитор", ["forwarding_type_freight"]),
            ("67. Номинация эксп.", ["forwarding_class_freight"]),
            ("68. Телекс-релиз", ["forwarding_download_method"]),
            ("69. Получение докум.", ["forwarding_ref_freight"]),
            ("70. Примечание", ["forwarding_note"]),
            ("71. Дата завершения в заказе", ["order_forwading_data_finish"]),
            ("72. Дата завершения в таблице Экспедиция", ["finished_date_table1"]),


        ]

        for step_name, fields in steps_to_check:
            with allure.step(step_name):
                for field in fields:
                    value = order_app.get(field)
                    check.is_false(value, f"❌ ФР: поле '{field}' должно быть пустым, но получено: {value}")
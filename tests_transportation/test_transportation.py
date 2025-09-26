import pytest
import allure
from orders.transport import WinAISTApp
import pytest_check as check
from difflib import SequenceMatcher
import locale
from datetime import datetime, date
import re



# Словарь для замены русских месяцев на английские
MONTHS_RU_EN = {
    'января': 'January', 'февраля': 'February', 'марта': 'March',
    'апреля': 'April', 'мая': 'May', 'июня': 'June',
    'июля': 'July', 'августа': 'August', 'сентября': 'September',
    'октября': 'October', 'ноября': 'November', 'декабря': 'December'
}

def normalize_date(date_val):
    """
    Преобразует дату в объект date, поддерживает форматы:
    - 23.09.2025
    - 23-09-2025 16:03 (автотест)
    - 1 сентября 2025
    """
    if isinstance(date_val, (datetime, date)):
        return date_val.date() if isinstance(date_val, datetime) else date_val

    date_str = str(date_val).replace("г.", "").strip()

    # Убираем всё, что в скобках
    date_str = re.sub(r"\(.*?\)", "", date_str).strip()

    # Переводим русские месяцы на английские
    for ru, en in MONTHS_RU_EN.items():
        if ru in date_str:
            date_str = date_str.replace(ru, en)
            break

    # Ставим безопасную локаль
    locale.setlocale(locale.LC_TIME, 'C')

    # Список форматов для распознавания
    formats = ["%d.%m.%Y", "%d-%m-%Y", "%d %B %Y", "%d-%m-%Y %H:%M"]

    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue

    raise ValueError(f"Не удалось распознать дату: {date_val}")

def compare_dates(date1, date2, error_message, tolerance_days=0):
    """
    Сравнивает две даты с допуском по дням.
    Если разница больше tolerance_days, выбрасывает AssertionError.
    """
    d1, d2 = normalize_date(date1), normalize_date(date2)
    delta_days = abs((d1 - d2).days)
    assert delta_days <= tolerance_days, f"{error_message}: {d1} != {d2}, разница {delta_days} дней"



@pytest.fixture(scope="module")
def order_app():
    print("[SETUP] Запуск фикстуры order_app")
    app = WinAISTApp()
    order_data = app.transport_auto()
    yield order_data
    print("[TEARDOWN] Закрытие WinAISTApp")
    app.close()

@allure.title("Проверка Таблицы Автоперевозка 104 проверки")
@pytest.mark.order(1)

def test_value_del(order_app):
    with allure.step("1. Тип перевозки"):
        check.equal(order_app["order_dialog_type"], "Автоперевозка", "❌ ФР: Не одинаковые")

    with allure.step("2. Поле Ответственный не пустое"):
        check.is_true(bool(order_app.get("order_dialog_otv")), "❌ ФР: поле Ответственный пустое")

    with allure.step("3. Номер заказа"):
        check.is_true(SequenceMatcher(None, order_app["order_dialog_number"], order_app["auto_order_number"]).ratio() >= 0.5, "❌ ФР: Не совпадает Имя маршрута Отгрузка на 50%")

    with allure.step("4. Сравнение Тип перевозки"):
        check.equal(order_app["order_dialog_type"], order_app["auto_type"], "❌ ФР: Не одинаковые Тип перевозки")

    with allure.step("5. Статус Черновик"):
        check.equal(order_app["auto_status"], "Черновик", "❌ ФР: Статус не Черновик")

    with allure.step("6. Приоритет Средний"):
        check.equal(order_app["auto_priority"], "Средний", "❌ ФР: Приоритет не Средний")

    with allure.step("7. Сравнение Ответственный"):
        check.equal(order_app["order_dialog_otv"], order_app["auto_otv"], "❌ ФР: Не одинаковые Ответственный")

    with allure.step("8. Сравнение Дат создания и изменение"):
        check.equal(order_app["auto_create_date"], order_app["auto_mode_date"], "❌ ФР: Не одинаковые Даты создания и изменение")

    with allure.step("9. Сравнение Дата завершения"):
        check.equal(order_app["auto_finish_date"], "...", "❌ ФР: Не одинаковые Дата завершения")

    with allure.step("10. Статусы неравны"):
        check.is_false(order_app["auto_status"] == order_app["auto_status_mod"], f"❌ ФР: Статусы равны")

    with allure.step("11. Приоритет неравны"):
        check.is_false(order_app["auto_priority"] == order_app["auto_priority_mod"], f"❌ ФР: Приоритет равны")

    with allure.step("12. Тип груза неравны"):
        check.is_false(order_app["auto_type_freight"] == order_app["auto_type_freight_mod"], f"❌ ФР: Тип груза равны")

    with allure.step("13. Класс груза неравны"):
        check.is_false(order_app["auto_class_freight"] == order_app["auto_class_freight_mod"], f"❌ ФР: Класс груза равны")

    with allure.step("14. Способ загрузки неравны"):
        check.is_false(order_app["auto_download_method"] == order_app["auto_download_method_mod"], f"❌ ФР: Способ загрузки равны")

    with allure.step("15. Референс груза неравны"):
        check.is_false(order_app["auto_ref_freight"] == order_app["auto_ref_freight_mod"], f"❌ ФР: Референс груза равны")

    with allure.step("16. Дата завершения неравны"):
        check.is_false(order_app["auto_finish_date"] == order_app["auto_finish_date_mod"], f"❌ ФР: Дата завершения равны")

    with allure.step("17. Номер CRM неравны"):
        check.is_false(order_app["auto_cmr"] == order_app["auto_cmr_mod"], f"❌ ФР: Номер CRM равны")

    with allure.step("18. Номер CRM порож неравны"):
        check.is_false(order_app["auto_cmr_por"] == order_app["auto_cmr_por_mod"], f"❌ ФР: Номер CRM порож равны")

    with allure.step("19. Примечание неравны"):
        check.is_false(order_app["auto_note"] == order_app["auto_note_mod"], f"❌ ФР: Примечание равны")


# Сравнение маршрутных данных
    with allure.step("20. Имя маршрута Отгрузка"):
        check.is_true(SequenceMatcher(None, order_app["shipment1"], order_app["shipment_name"]).ratio() >= 0.1, "❌ ФР: Не совпадает Имя маршрута Отгрузка на 130%")

    with allure.step("21. Адрес Отгрузка"):
        check.equal(order_app["address1"],order_app["shipment_address"], f"❌ ФР: Адрес Отгрузка")

    with allure.step("22. Водитель Отгрузка"):
        check.equal(order_app["driver1"],order_app["shipment_driver"], f"❌ ФР: Не совпадает Водитель Отгрузка")

    with allure.step("23. План. дата отгрузки Отгрузка"):
        compare_dates(order_app["plan_load1"],order_app["shipment_plan_data"], f"❌ ФР: Не совпадает План. дата отгрузки Отгрузка")

    with allure.step("24. Факт. дата отгрузки Отгрузка"):
        compare_dates(order_app["fact_load1"],order_app["shipment_fact_data"], f"❌ ФР: Не совпадает Факт. дата отгрузки Отгрузка")

    with allure.step("25. Автомобиль Отгрузка"):
        check.equal(order_app["car1"],order_app["shipment_auto"], f"❌ ФР: Не совпадает Автомобиль Отгрузка")

    with allure.step("26. Поменялся Адрес Отгрузка"):
        check.is_false(order_app["shipment_address"] == order_app["shipment_address_mod"], f"❌ ФР: ")

    with allure.step("27. Поменялся Водитель Отгрузка"):
        check.is_false(order_app["shipment_driver"] == order_app["shipment_driver_mod"], f"❌ ФР: ")

    with allure.step("28. Поменялся Автомобиль Отгрузка"):
        check.is_false(order_app["shipment_auto"] == order_app["shipment_auto_mod"], f"❌ ФР: ")

    with allure.step("29. Поменялся План. дата отгрузки Отгрузка"):
        check.is_false(order_app["shipment_plan_data"] == order_app["shipment_plan_data_mod"], f"❌ ФР: ")

    with allure.step("30. Поменялся Факт. дата отгрузки Отгрузка"):
        check.is_false(order_app["shipment_fact_data"] == order_app["shipment_fact_data_mod"], f"❌ ФР: ")

    with allure.step("31. Поменялся Примечание Отгрузка"):
        check.is_false(order_app["shipment_note"] == order_app["shipment_note_mod"], f"❌ ФР: НЕ поменялся Примечание Отгрузка")

    with allure.step("32. Адрес Прибытие"):
        check.equal(order_app["address2"],order_app["arrival_address"], f"❌ ФР: Не совпадает Адрес Прибытие")

    with allure.step("33. План. прибытия Прибытие"):
        compare_dates(order_app["plan_arrival2"],order_app["arrival_plan_data"], f"❌ ФР: Не совпадает План. прибытия Прибытие")

    with allure.step("34. Факт. прибытия Прибытие"):
        compare_dates(order_app["fact_arrival2"], order_app["arrival_fact_data"], f"❌ ФР: Не совпадает Факт. прибытия Прибытие")

    with allure.step("35. Поменялся Адрес Прибытие"):
        check.is_false(order_app["arrival_address"] == order_app["arrival_address_mod"], f"❌ ФР:Не поменялся Адрес Прибытие")

    with allure.step("36. Поменялся План. прибытия Прибытие"):
        check.is_false(order_app["arrival_plan_data"] == order_app["arrival_plan_data_mod"], f"❌ ФР:Не поменялся План. прибытия Прибытие ")

    with allure.step("37. Поменялся Факт. прибытия Прибытие"):
        check.is_false(order_app["arrival_fact_data"] == order_app["arrival_fact_data_mod"], f"❌ ФР:Не поменялся Факт. прибытия Прибытие ")

    with allure.step("38. Поменялся Примечание Прибытие"):
        check.is_false(order_app["arrival_note"] == order_app["arrival_note_mod"], f"❌ ФР:Не поменялся Примечание Прибытие ")

    with allure.step("39. Поменялся Адрес Cдача контейнера"):
        check.equal(order_app["address3"], order_app["drop_con_address"], f"❌ ФР:Не совпадает Адрес Cдача контейнера")

    with allure.step("40. План. прибытия Cдача контейнера"):
        compare_dates(order_app["plan_arrival3"],order_app["drop_con_plan_data"], f"❌ ФР: Не совпадает План. прибытия Cдача контейнера")

    with allure.step("41. Факт. прибытия Cдача контейнера"):
        compare_dates(order_app["fact_arrival3"],order_app["drop_con_fact_data"], f"❌ ФР: Не совпадает Факт. прибытия Cдача контейнера")

    with allure.step("42. Поменялся Адрес Cдача контейнера"):
        check.is_false(order_app["drop_con_address"] == order_app["drop_con_fact_data_mod"], f"❌ ФР:Не поменялся Примечание Прибытие ")

    with allure.step("43. Поменялся План. прибытия Cдача контейнера"):
        check.is_false(order_app["drop_con_plan_data"] == order_app["drop_con_fact_data_mod"], f"❌ ФР:Не поменялся Примечание Прибытие ")

    with allure.step("44. Поменялся Факт. прибытия Cдача контейнера"):
        check.is_false(order_app["drop_con_fact_data"] == order_app["drop_con_fact_data_mod"], f"❌ ФР:Не поменялся Примечание Прибытие ")

    with allure.step("45. Поменялся Примечание Cдача контейнера"):
        check.is_false(order_app["drop_con_note"] == order_app["arrival_note_mod"], f"❌ ФР:Не поменялся Примечание Прибытие ")

# Заказ
    with allure.step("46. Заказ таблица"):
        check.equal(order_app["order_table1"],order_app["order_dialog_number"], f"❌ ФР: Не совпадает Заказ")

    with allure.step("47. Статус таблица"):
        check.equal(order_app["status_table1"],order_app["auto_status_mod"], f"❌ ФР: Не совпадает Статус таблица")

    with allure.step("48. Приоритет таблица"):
        check.equal(order_app["priority_table1"],order_app["auto_priority_mod"], f"❌ ФР: Не совпадает Приоритет таблица")

    with allure.step("49. Ответственный таблица"):
        check.equal(order_app["responsible_table1"], order_app["auto_otv"], f"❌ ФР: Не совпадает Ответственный таблица")

    with allure.step("50. Перевозчик таблица"):
        check.equal(order_app["carrier_table1"], order_app["auto_carrier_mod"], f"❌ ФР: Не совпадает Перевозчик таблица Не чинили 29.08")

    with allure.step("51. Класс груза таблица"):
        check.equal(order_app["cargo_class_table1"], order_app["auto_class_freight_mod"], f"❌ ФР: Не совпадает Класс груза таблица")

    with allure.step("52. Способ загрузки таблица"):
        check.equal(order_app["loading_method_table1"], order_app["auto_download_method_mod"], f"❌ ФР: Не совпадает Способ загрузки таблица Не чинили 29.08")

    with allure.step("53. Номер CMR таблица"):
        check.equal(order_app["cmr_number_table1"], order_app["auto_cmr_mod"], f"❌ ФР: Не совпадает Номер CMR таблица")

    with allure.step("54. Примечание таблица"):
        check.equal(order_app["note_table1"], order_app["auto_note_mod"], f"❌ ФР: Не совпадает Примечание таблица")

    with allure.step("55. Кем создан таблица"):
        check.is_true(SequenceMatcher(None, order_app["created_by_table1"], order_app["auto_create_date"]).ratio() >= 0.3, "❌ ФР: Не совпадает Кем создан таблица на 30%")

    with allure.step("56. Дата создания таблица"):
        check.is_true(SequenceMatcher(None, order_app["creation_date_table1"], order_app["auto_create_date"]).ratio() >= 0.3, "❌ ФР: Не совпадает Дата создания таблица на 30%")

    with allure.step("57. Дата изменения таблица"):
        compare_dates(order_app["modification_date_table1"], order_app["auto_mode_date_mod"], f"❌ ФР: Не совпадает Дата изменения таблица")

    with allure.step("58. Дата завершения таблица"):
        compare_dates(order_app["completion_date_table1"], order_app["auto_finish_date_mod"], f"❌ ФР: Не совпадает Дата завершения таблица")

    with allure.step("59. Тип груза таблица"):
        check.equal(order_app["cargo_type_table1"], order_app["auto_type_freight_mod"], f"❌ ФР: Не совпадает Тип груза таблица")

    with allure.step("60. Номер заказа"):
        check.is_true(order_app["order_dialog_number"] in order_app["order_number"], "❌ ФР: Номер заказа не одинаковый")

    with allure.step("61. Тип заказа — Логистика"):
        check.equal(order_app["order_type"], "Логистика", "❌ ФР: Поле с другим значением, но должно быть Логистика")

    with allure.step("62. Статус заказа — Черновик"):
        check.equal(order_app["order_status"], "Черновик", "❌ ФР: Поле с другим значением, но должно быть Черновик")

    with allure.step("63. Приоритет заказа — Средний"):
        check.equal(order_app["order_priority"], "Средний", "❌ ФР: Поле с другим значением, но должно быть Средний")

    with allure.step("64. Указанный ответственный существует"):
        check.equal(order_app["order_dialog_otv"], order_app["order_otv"], "❌ ФР: Поля не одинаковые")


    with allure.step("65. Клиент заказа указан"):
        check.equal(order_app["order_dialog_client"], order_app["order_client"], "❌ ФР: Клиент не соответствует выбранному")

    with allure.step("66. Дата создания одинаковая с датой изменения"):
        check.is_true(SequenceMatcher(None, order_app["order_create_date"], order_app["order_create_mod"]).ratio() >= 0.9,
                  "❌ ФР: Поля не одинаковые Дата создания одинаковая с датой изменения на 90%")

    with allure.step("67. Дата завершения ..."):
        check.equal(order_app["order_completion_date"], "...", "❌ ФР: Не соответствует значению")


    steps_to_check = [
        ("68. Тип груза", ["auto_type_freight"]),
        ("69. Класс груза", ["auto_class_freight"]),
        ("70. Способ загрузки", ["auto_download_method"]),
        ("71. Референс груза", ["auto_ref_freight"]),
        ("72. Перевозчик", ["auto_carrier"]),
        ("73. Номер CRM", ["auto_cmr"]),
        ("74. Номер CRM порож", ["auto_cmr_por"]),
        ("75. Примечание перевозки", ["auto_note"]),
        ("76. Примечание Отгрузка", ["shipment_note"]),
        ("77. План. прибытия Отгрузка", ["plan_arrival1"]),
        ("78. Факт. прибытия Отгрузка", ["fact_arrival1"]),
        ("79. Водитель Прибытие", ["driver2"]),
        ("80. План. отгрузки Прибытие", ["plan_load2"]),
        ("81. Факт. отгрузки Прибытие", ["fact_load2"]),
        ("82. Автомобиль Прибытие", ["car2"]),
        ("83. Примечание Прибытие", ["arrival_note"]),
        ("84. Адрес Сдача контейнера", ["address3"]),
        ("85. Примечание Сдача контейнера", ["drop_con_note"]),
        ("86. Водитель Сдача контейнера", ["driver3"]),
        ("87. План. отгрузки Сдача контейнера", ["plan_load3"]),
        ("88. Факт. отгрузки Сдача контейнера", ["fact_load3"]),
        ("89. Автомобиль Сдача контейнера", ["car3"]),
        ("90. План. прибытия Отгрузка", ["plan_arrival1_mod"]),
        ("91. Факт. прибытия Отгрузка", ["fact_arrival1_mod"]),
        ("92. Водитель Прибытие", ["driver2_mod"]),
        ("93. План. отгрузки Прибытие", ["plan_load2_mod"]),
        ("94. Факт. отгрузки Прибытие", ["fact_load2_mod"]),
        ("95. Автомобиль Прибытие", ["car2_mod"]),
        ("96. Водитель Сдача контейнера", ["driver3_mod"]),
        ("97. План. отгрузки Сдача контейнера", ["plan_load3_mod"]),
        ("98. Факт. отгрузки Сдача контейнера", ["fact_load3_mod"]),
        ("99. Автомобиль Сдача контейнера", ["car3_mod"]),
        ("100. Отправители в заказе", ["order_senders"]),
        ("101. Получатель в заказе", ["order_recipient"]),
        ("102. Условия поставки в заказе", ["order_delivery"]),
        ("103. Референс клиента в заказе", ["order_reference"]),
        ("104. Примечание в заказе", ["order_note"]),
    ]

    for step_name, fields in steps_to_check:
        with    allure.step(step_name):
            for field in fields:
                value = order_app.get(field)
                check.is_false(value, f"❌ ФР: поле '{field}' должно быть пустым, но получено: {value}")

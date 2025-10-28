import pytest
import allure
from orders.services import WinAISTApp
import pytest_check as check
from locators.format_data import compare_dates


@pytest.fixture(scope="module")
def order_app():
    print("Создание в заказе, перевозках и экспедирование.\nРедактирование услуг.\nПривязка к ИС и ВС\nУдаление услуги \nПроверки выставление данных в таблицах.")
    app = WinAISTApp()
    try:
        order_data = app.services()
        yield order_data
    finally:
        print("[TEARDOWN] Закрытие WinAISTApp")
        app.close()


@allure.suite("ГТД в заказе" )
@allure.title("Проверка данных заказа и ГТД 38"
              " проверок")
@pytest.mark.order(1)
def test_full_order_validation(order_app):
    with allure.step("1. Проверка Название услуги в гриде"):
        check.is_true(order_app["service_type"] == order_app["service_type_mod"],
                      "❌ ФР: Одинаковые Название услуги в гриде")

    with allure.step("2. Проверка Ставка услуги в гриде"):
        check.is_false(order_app["service_rate"] == order_app["service_rate_mod"],
                      "❌ ФР: Одинаковые Ставка услуги в гриде")

    with allure.step("3. Проверка Валюта услуги в гриде"):
        check.is_false(order_app["service_currency"] == order_app["service_currency_mod"],
                      "❌ ФР: Одинаковые Валюта услуги в гриде")

    with allure.step("4. Проверка НДС услуги в гриде"):
        check.is_false(order_app["service_vat"] == order_app["service_vat_mod"], "❌ ФР: Одинаковые НДС услуги в гриде")

    with allure.step("5. Проверка Количество услуги в гриде"):
        check.equal(order_app["service_quantity"], "1,0000",
                      "❌ ФР: НЕ одинаковые Количество услуги в гриде")

    with allure.step("6. Проверка Количество услуги в гриде"):
        check.equal(order_app["service_quantity"], order_app["service_quantity_mod"],
                      "❌ ФР: НЕ одинаковые Количество услуги в гриде")

    with allure.step("7. Проверка Тип ТЕ услуги в гриде"):
        check.equal(order_app["service_te_type"], order_app["service_te_type_mod"],
                      "❌ ФР: Не одинаковые Тип ТЕ услуги в гриде")

    with allure.step("8. Проверка Номера ТЕ услуги в гриде"):
        check.equal(order_app["service_te_number"], order_app["service_te_number_mod"],
                       "❌ ФР: Не одинаковые Номера ТЕ услуги в гриде")

    with allure.step("9. Проверка Примечание услуги в гриде"):
        check.is_false(order_app["service_note"] == order_app["service_note_mod"],
                      "❌ ФР: Одинаковые Примечание услуги в гриде")

    with allure.step("10. Проверка Источник услуги в гриде"):
        check.equal(order_app["service_source"], order_app["service_source_mod"],
                      "❌ ФР: Не одинаковые Источник услуги в гриде")

    with allure.step("11. Проверка Счет услуги в гриде"):
        check.equal(order_app["service_account"], order_app["service_account_mod"],
                       "❌ ФР: Не одинаковые Счет услуги в гриде")

     #  Сравнение грида с формой
    with allure.step("12. Сравнение Название услуги в гриде и форме"):
        check.is_true(order_app["service_type_mod"] in order_app["service_name_form"], "❌ ФР: Не одинаковые Название услуги в гриде и форме")

    with allure.step("13. Сравнение Ставка услуги в гриде и форме"):
        check.equal(order_app["service_rate_mod"], order_app["service_rate_form"], "❌ ФР: Не одинаковые Ставка услуги в гриде и форме")

    with allure.step("14. Сравнение Валюта услуги в гриде и форме"):
        check.equal(order_app["service_currency_mod"], order_app["service_currency_form"], "❌ ФР: Не одинаковые Валюта услуги в гриде и форме")

    with allure.step("15. Сравнение НДС услуги в гриде и форме"):
        check.equal(order_app["service_vat_mod"], order_app["service_vat_form"], "❌ ФР: Не одинаковые НДС услуги в гриде и форме")

    with allure.step("16. Сравнение Количество услуги в гриде и форме"):
        check.equal(order_app["service_quantity_mod"], order_app["service_quantity_form"], "❌ ФР: Не одинаковые Количество услуги в гриде и форме")

    with allure.step("17. Сравнение Тип ТЕ услуги в гриде и форме"):
        check.equal(order_app["service_te_type"], order_app["service_te_type_form"], "❌ ФР: Не динаковые Тип ТЕ услуги в гриде и форме")

    with allure.step("18. Сравнение Номера ТЕ услуги в гриде и форме"):
        check.equal(order_app["service_te_number_mod"], order_app["service_te_number_form"], "❌ ФР: Не одинаковые Номера ТЕ услуги в гриде и форме")

    with allure.step("19. Сравнение Примечание услуги в гриде и форме"):
        check.equal(order_app["service_note_mod"], order_app["service_note_form"], "❌ ФР: Не одинаковые Примечание услуги в гриде и форме")

    with allure.step("20. Проверка Ед. изм. услуги в форме"):
        check.equal(order_app["service_uom_form"], "Шт.",
                    "❌ ФР: НЕ одинаковые Ед. изм. услуги в форме")

    #  Проверка отредактированной формы
    with allure.step("21. Отредактированная Ставка услуги в форме"):
        check.is_false(order_app["service_rate_form"] == order_app["service_rate_form_mod"], "❌ ФР: Одинаковые Ставка услуги в форме")

    with allure.step("22. Отредактированная Валюта услуги в форме"):
        check.is_false(order_app["service_currency_form"] == order_app["service_currency_form_mod"], "❌ ФР: Одинаковые Валюта услуги в форме")

    with allure.step("23. Отредактированная НДС услуги в форме"):
        check.is_false(order_app["service_vat_form"] == order_app["service_vat_form_mod"], "❌ ФР: Одинаковые НДС услуги в форме")

    with allure.step("24. Отредактированная Количество услуги в форме"):
        check.is_false(order_app["service_quantity_form"] == order_app["service_quantity_form_mod"], "❌ ФР: Одинаковые Количество услуги в форме")

    with allure.step("25. Отредактированная Тип ТЕ услуги в форме"):
        check.is_false(order_app["service_te_type_form"] == order_app["service_te_type_form_mod"], "❌ ФР: Одинаковые Тип ТЕ услуги в форме")

    with allure.step("26. Отредактированная Номера ТЕ услуги в форме"):
        check.is_false(order_app["service_te_number_form"] == order_app["service_te_number_form_mod"], "❌ ФР: Одинаковые Номера ТЕ услуги в форме")

    with allure.step("27. Отредактированная Примечание услуги в форме"):
        check.is_false(order_app["service_note_form"] == order_app["service_note_form_mod"], "❌ ФР: Одинаковые Примечание услуги в форме")

    with allure.step("28. Отредактированная Ед. изм. услуги в форме"):
        check.is_false(order_app["service_note_form"] == order_app["service_note_form_mod"],"❌ ФР: Одинаковые Ед. изм. услуги в форме")

#  Проверка отредактированной формы в гриде
    with allure.step("29. Отредактированная Ставка услуги в гриде"):
        check.equal(order_app["service_rate_form_mod"], order_app["service_rate_mod1"], "❌ ФР: Одинаковые Ставка услуги в гриде")

    with allure.step("30. Отредактированная Валюта услуги в гриде"):
        check.equal(order_app["service_currency_form_mod"], order_app["service_currency_mod1"], "❌ ФР: Одинаковые Валюта услуги в гриде")

    with allure.step("31. Отредактированная НДС услуги в гриде"):
        check.equal(order_app["service_vat_form_mod"], order_app["service_vat_mod1"], "❌ ФР: Одинаковые НДС услуги в гриде")

    with allure.step("32. Отредактированная Количество гриде"):
        check.equal(order_app["service_quantity_form_mod"], order_app["service_quantity_mod1"], "❌ ФР: Одинаковые Количество услуги в гриде")

    with allure.step("33. Отредактированная Тип ТЕ услуги в гриде"):
        check.equal(order_app["service_te_type_form_mod"], order_app["service_te_type_mod1"], "❌ ФР: Одинаковые Тип ТЕ услуги в гриде")

    with allure.step("34. Отредактированная Номера ТЕ услуги в гриде"):
        check.equal(order_app["service_te_number_form_mod"], order_app["service_te_number_mod1"], "❌ ФР: Одинаковые Номера ТЕ услуги в гриде")

    with allure.step("35. Отредактированная Примечание услуги в гриде"):
        check.equal(order_app["service_note_form_mod"], order_app["service_note_mod1"], "❌ ФР: Одинаковые Примечание услуги в гриде")

    #Проверка названий услуг и сравнение источника
    with allure.step("37. Номер морcкой перевозки в заказе"):
        check.equal(order_app["sea_service_source"], order_app["sea_number"],
                    "❌ ФР: Номер морcкой перевозки в заказе не совпадает с источником")

    with allure.step("39. Номер автоперевозки в заказе"):
        check.equal(order_app["auto_service_source"], order_app["auto_number"],
                    "❌ ФР: Номер автоперевозки в заказе не совпадает с источником")

    with allure.step("41. Номер ЖД перевозки в заказе"):
        check.equal(order_app["jd_service_source"], order_app["jd_number"],
                    "❌ ФР: Номер ЖД-перевозки в заказе не совпадает с источником")

    with allure.step("43. Номер авиаперевозки в заказе"):
        check.equal(order_app["avia_service_source"], order_app["avia_number"],
                    "❌ ФР: Номер авиаперевозки в заказе не совпадает с источником")

    with allure.step("45. Номер экспедировании в заказе"):
        check.equal(order_app["for_service_source"], order_app["for_number"],
                    "❌ ФР: Номер экспедировании в заказе не совпадает с источником")

    with allure.step("62. Текст окна при удалении услуги связанной с счетом в заказе"):
        check.equal(order_app["service_del_text"], "Нельзя удалить услугу, добавленную в счет. Сначала удалите услугу из счета и затем повторите попытку удаления услуги из заказа.", "❌ ФР: Тект не правильный при удалении услуги")

    tabs_to_check = {

        "sea_service_type": "36. Название  услуги в морской перевозке",
        "auto_service_type": "38. Название  услуги в автоперевозке",
        "jd_service_type": "40. Название  услуги в ЖД-перевозке",
        "avia_service_type": "42. Название  услуги в авиаперевозке",
        "for_service_type": "44. Название  услуги в экспедировании",

        "service_sea": "46. Название услуги из морской перевозки в заказе",
        "source_sea": "47. Источник услуги из морской перевозки в заказе",
        "service_auto": "48. Название услуги из автоперевозки в заказе",
        "source_auto": "49. Источник услуги из автоперевозки в заказе",
        "service_jd": "50. Название услуги из ЖД перевозки в заказе",
        "source_jd": "51. Источник услуги из ЖД перевозки в заказе",
        "service_avia": "52. Название услуги из авиаперевозки в заказе",
        "source_avia": "53. Источник услуги из авиаперевозки в заказе",
        "service_for": "54. Название услуги из экспедирования в заказе",
        "source_for": "55. Источник услуги из экспедирования в заказе",
        "service_is_1form": "56. Сравнение добавленной услуги 1 из заказа в ИС",
        "service_is_2form": "57. Сравнение добавленной услуги 2 из заказа в ИС",
        "service_is_3form": "58. Сравнение добавленной услуги 3 из заказа в ИС",
        "service_vs_1form": "59. Сравнение добавленной услуги 1 из заказа в ВС",
        "service_vs_2form": "60. Сравнение добавленной услуги 2 из заказа в ВС",
        "service_vs_3form": "61. Сравнение добавленной услуги 3 из заказа в ВС",
    }

    # Цикл по каждой вкладке
    for field_name, expected_value in tabs_to_check.items():
        with allure.step(f"Проверка {expected_value}'"):
            check.is_true(order_app.get(field_name), f"❌ ФР: Поле '{expected_value}' имеет неверное значение")

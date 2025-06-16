import pytest
import allure
from transportation.transportation import Transportation
from fuzzywuzzy import fuzz as f


@pytest.fixture(scope="module")
def order_app():
    print("[SETUP] Запуск фикстуры order_app")
    app = Transportation()
    order_data = app.create_transportation_sea()
    yield order_data
    print("[TEARDOWN] Закрытие WinAISTApp")
    app.close()


@allure.title("Морская перевозка")
@pytest.mark.order(1)
def test_value_del(order_app):
    with allure.step("Сравниваем тип заказа"):
        assert order_app["sea_type"] == order_app["sea_type_form"], "❌ Ожидалось: None, поля одинаковые"
        print("✅ Прошел тест! Тип Морская перевозка")

    with allure.step("Сравниваем Статус"):
        assert order_app["sea_status_form"] == "Черновик"
        print("✅ Прошел тест! Черновик")

    with allure.step("Сравниваем Приоритет"):
        assert order_app["sea_priority_form"] == "Средний"
        print("✅ Прошел тест! Средний")

    with allure.step("Сравниваем Ответственный"):
        assert order_app["sea_otv_form"] == order_app["sea_otv"], "❌ Ожидалось: Ответственные, поля должны быть одинаковые"
        print("✅ Прошел тест! Не пустое")

    with allure.step("Сравниваем Тип груза"):
        assert not order_app["sea_type_freight_form"], "❌ Ожидалось: None, но поле заполнено"
        print("✅ Прошел тест! Поле пустое")

    with allure.step("Сравниваем Класс груза"):
        assert not order_app["sea_class_freight_form"], "❌ Ожидалось: None, но поле заполнено"
        print("✅ Прошел тест! Поле пустое")

    with allure.step("Сравниваем Способ загрузки"):
        assert not order_app["sea_loading_form"], "❌ Ожидалось: None, но поле заполнено"
        print("✅ Прошел тест! Поле пустое")

    with allure.step("Сравниваем Референс груза"):
        assert not order_app["sea_reference_freight_form"], "❌ Ожидалось: None, но поле заполнено"
        print("✅ Прошел тест! Поле пустое")

    with allure.step("Сравниваем Дата создания"):
        assert order_app["sea_tab_create_date"] == order_app["sea_tab_mod_date"], "❌ Ожидалось: поля одинаковые"
        print("✅ Прошел тест! Одинаковые")

    with allure.step("Сравниваем Дата завершения"):
        assert order_app["sea_tab_finish"] == "...", "❌ Ожидалось: ... , но поле заполнено датой"
        print("✅ Прошел тест! Тип Морская перевозка")


    with allure.step("Сравниваем Тип груза"):
        assert not order_app["sea_type_freight_form"], "❌ Ожидалось: None, но поле заполнено"
        print("✅ Прошел тест! Поле пустое")

    with allure.step("Сравниваем Букинг референс"):
        assert not order_app["sea_tab_booking_ref"], "❌ Ожидалось: None, но поле заполнено"
        print("✅ Прошел тест! Поле пустое")

    with allure.step("Сравниваем Океанская линия"):
        assert order_app["sea_tab_ocean_line"] == "[нет данных]", "❌ Ожидалось: None, но поле заполнено"
        print("✅ Прошел тест! Поле пустое")

    with allure.step("Сравниваем Океан. коносамент"):
        assert not order_app["sea_tab_ocean_kon"], "❌ Ожидалось: None, но поле заполнено"
        print("✅ Прошел тест! Поле пустое")

    with allure.step("Сравниваем Фидерная линия"):
        assert order_app["sea_tab_feeder_line"] == "[нет данных]", "❌ Ожидалось: None, но поле заполнено"
        print("✅ Прошел тест! Поле пустое")

    with allure.step("Сравниваем Фидерн. коносамент"):
        assert not order_app["sea_tab_feeder_kon"], "❌ Ожидалось: None, но поле заполнено"
        print("✅ Прошел тест! Поле пустое")

    with allure.step("Сравниваем Примечание"):
        assert not order_app["sea_tab_note_sea"], "❌ Ожидалось: None, но поле заполнено"
        print("✅ Прошел тест! Поле пустое")




    with allure.step("Сравниваем Название"):
        assert f.ratio(order_app["sea_navigation"], order_app["sea_form_navigation"]), "❌ Ожидалось: поля одинаковые"
        print("✅ Прошел тест! Поле пустое")

    with allure.step("Сравниваем Порт"):
        assert order_app["sea_dialog_port"] == order_app["sea_form_port"], "❌ Ожидалось: None, но поле заполнено"
        print("✅ Прошел тест! Поле пустое")

    with allure.step("Сравниваем Терминал"):
        assert order_app["sea_dialog_terminal"] == order_app["sea_form_terminal"], "❌ Ожидалось: None, но поле заполнено"
        print("✅ Прошел тест! Поле пустое")

    with allure.step("Сравниваем Агент"):
        assert order_app["sea_dialog_agent"] == order_app["sea_form_agent"], "❌ Ожидалось: None, но поле заполнено"
        print("✅ Прошел тест! Поле пустое")

    with allure.step("Сравниваем Плановая дата"):
        assert order_app["sea_dialog_data"] == order_app["sea_form_data"], "❌ Ожидалось: None, но поле заполнено"
        print("✅ Прошел тест! Поле пустое")

    with allure.step("Сравниваем Примечание"):
        assert order_app["sea_fact_data"] == order_app["sea_form_fact_data"], "❌ Ожидалось: None, но поле заполнено"
        print("✅ Прошел тест! Поле пустое")

    with allure.step("Сравниваем Примечание"):
        assert order_app["sea_dialog_note"] == order_app["sea_form_note"], "❌ Ожидалось: None, но поле заполнено"
        print("✅ Прошел тест! Поле пустое")


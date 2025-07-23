from pywinauto import Application, keyboard
from locators.locators import LocOrders
from locators.function import Function
import time



class WinAISTApp:
    def __init__(self):
        self.app = Application(backend='uia').connect(path="WinAIST.exe")
        self.fun = Function()
        self.loc = LocOrders()

    def freight(self):
        # 1. Запуск приложения
        startup_window = self.fun.start_application()
        startup_window.set_focus()

        # 3. Переход в раздел Грузы
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(3)

        self.fun.click_element(main_window, self.loc.FREIGHT, timeout=3)
        time.sleep(8)

        # 4. Создать груз
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)

        self.fun.click_element(main_window, self.loc.CLIENT_COMBO, timeout=1)
        self.fun.click_element(main_window, self.loc.RECIPIENT_1, timeout=1)

        # 4. Создать заказа
        self.fun.click_element(main_window, self.loc.FREIGHT_ORDER_W, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_ORDER_CREATE, timeout=1)

        self.fun.click_element(main_window, self.loc.ORDER_TYPE_COMBO, timeout=1)
        self.fun.click_element(main_window, self.loc.LOGISTICS_ITEM, timeout=1)
        self.fun.click_element(main_window, self.loc.CUSTOMER_COMBO, timeout=1)
        self.fun.click_element(main_window, self.loc.RECIPIENT_1, timeout=1)

        time.sleep(1)

        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TE, timeout=2)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TE1, timeout=2)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TYPE, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TYPE1, timeout=1)
        self.fun.set_text_field(main_window, self.loc.FREIGHT_CREATE_QUANTITY, 1, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_UOM, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_UOM1, timeout=2)
        text = self.fun.get_element_value(main_window, self.loc.FREIGHT_ORDER_W, timeout=1)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

        # Фильтруем по номеру заказа
        self.fun.click_element(main_window, self.loc.FREIGHT_RESP_FOR_TABLE, timeout=1)
        keyboard.send_keys('{RIGHT}' * 27)
        keyboard.send_keys(text, with_spaces=True)
        keyboard.send_keys('{ENTER}')

        # Открываем заказ
        self.fun.click_element(main_window, self.loc.SEA_TAB_ORDER_NUMBER, timeout=1)

        # 12. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 12. Создаём груз
        # 6. Перейти во вкладку
        self.fun.click_element(main_window, self.loc.TAB_FREIGHT, timeout=2)

        # 5. Открыть груз bulkership
        self.fun.click_element_double(main_window, self.loc.FREIGHT_ITEM, timeout=5)

        # 5. Переключение на форму bulkership
        main_window = self.fun.get_freight_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.fun.app.window(**self.loc.FREIGHT_FROM)
        time.sleep(1)

        # 5. Проверка полей

        # 5 Редактирование формы bulkership
        self.fun.set_text_field(order_form, self.loc.FREIGHT_TE_NUMBER_FORM, "1234567", timeout=1)
        self.fun.click_element(order_form, self.loc.FREIGHT_TE_TYPE, timeout=1)
        self.fun.click_element(order_form, self.loc.FREIGHT_LINE_7, timeout=1)
        self.fun.set_text_field(order_form, self.loc.FREIGHT_TE_QUANTITY_FORM, "77", timeout=1)
        self.fun.click_element(order_form, self.loc.FREIGHT_TE_UOM, timeout=1)
        self.fun.click_element(order_form, self.loc.FREIGHT_LINE_3, timeout=1)

        self.fun.click_element(order_form, self.loc.UNLOADING, timeout=1)
        keyboard.send_keys('1')
        self.fun.set_text_field(order_form, self.loc.FREIGHT_NUMBER_SEAL_FORM, "12345678", timeout=1)
        self.fun.set_text_field(order_form, self.loc.FREIGHT_NUMBER_GTD_FORM, "23456789", timeout=2)
        self.fun.click_element(order_form, self.loc.FREIGHT_MODE_TO_FORM, timeout=1)
        self.fun.click_element(order_form, self.loc.DELIVERY_CONDITION_0, timeout=1)
        self.fun.click_element(order_form, self.loc.FORWARDING_RECEIVING_DO, timeout=1)
        keyboard.send_keys('2')
        self.fun.click_element(order_form, self.loc.FREIGHT_DATA_TO_FORM, timeout=1)
        keyboard.send_keys('3')
        self.fun.set_text_field(order_form, self.loc.NOTE_CONTAINER, "MSMU 2222222 + СААU 333333  2х20 ставка перевоза по 7 000р/щт", timeout=1)
        self.fun.click_element(order_form, self.loc.APPLY_BUTTON1, timeout=1)

        # Добавление товара bulkership
        self.fun.click_element(order_form, self.loc.TAB_FREIGHT_GOODS, timeout=1)

        self.fun.click_element(order_form, self.loc.CREATE_BUTTON, timeout=1)
        self.fun.set_text_field(order_form, self.loc.NAME_TOV_RU, "Суперпупер штука которая очень нужная", timeout=1)
        self.fun.set_text_field(order_form, self.loc.NAME_TOV_EN, "A super-duper thing that is very necessary" ,timeout=1)
        self.fun.set_text_field(order_form, self.loc.NAME_NOTE, "Быстро нужно привезти",timeout=1)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)

        # 5. Переключение на форму товара bulkership
        main_window = self.fun.get_product_form()
        main_window.set_focus()
        order_form = self.fun.app.window(**self.loc.PRODUCT_FORM)
        time.sleep(1)

        # 5. Добавление веса товара bulkership
        self.fun.set_text_field(order_form, self.loc.NET_WEIGHT, "1000", timeout=1)
        self.fun.set_text_field(order_form, self.loc.GROSS_WEIGHT, "2345", timeout=1)

        self.fun.click_element(order_form, self.loc.APPLY_BUTTON1, timeout=1)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)

        # 5. Переключение на форму bulkership
        main_window = self.fun.get_freight_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.fun.app.window(**self.loc.FREIGHT_FROM)
        time.sleep(1)

        # 5. Проверка полей

        # 5 Закрыть bulkership
        self.fun.click_element(order_form, self.loc.SAVE_BUTTON, timeout=1)
        time.sleep(1)



        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        order_form = self.fun.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)

        # 7 Создать Container
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TE, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TE2, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TYPE, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TYPE1, timeout=1)
        self.fun.set_text_field(main_window, self.loc.FREIGHT_CREATE_QUANTITY, 1, timeout=1)

        # 8 Взять данные
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)
        time.sleep(1)

        # Во вкладке Перевозки, таблица


        # 5. Открыть Container
        self.fun.click_element_double(main_window, self.loc.FREIGHT_ITEM2, timeout=5)

        # 5. Переключение на форму Container
        main_window = self.fun.get_freight_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.fun.app.window(**self.loc.FREIGHT_FROM)
        time.sleep(1)

        # 5. Проверка полей

        # 5 Редактирование формы Container
        self.fun.set_text_field(order_form, self.loc.FREIGHT_TE_NUMBER_FORM, "TARE 1234567", timeout=1)
        self.fun.click_element(order_form, self.loc.FREIGHT_TE_TYPE, timeout=1)
        self.fun.click_element(order_form, self.loc.FREIGHT_LINE_7, timeout=1)

        self.fun.click_element(order_form, self.loc.UNLOADING, timeout=1)
        keyboard.send_keys('1')
        self.fun.set_text_field(order_form, self.loc.FREIGHT_NUMBER_SEAL_FORM, "12345678", timeout=1)
        self.fun.set_text_field(order_form, self.loc.FREIGHT_NUMBER_GTD_FORM_CONTAINER, "23456789", timeout=1)
        self.fun.click_element(order_form, self.loc.FREIGHT_MODE_TO_FORM, timeout=1)
        self.fun.click_element(order_form, self.loc.DELIVERY_CONDITION_0, timeout=1)
        self.fun.click_element(order_form, self.loc.FORWARDING_RECEIVING_DO, timeout=1)
        keyboard.send_keys('2')
        self.fun.click_element(order_form, self.loc.FREIGHT_DATA_TO_FORM, timeout=1)
        keyboard.send_keys('3')
        self.fun.set_text_field(order_form, self.loc.NOTE_CONTAINER, "MSMU 2222222 + СААU 333333  2х20 ставка перевоза по 7 000р/щт", timeout=1)
        self.fun.click_element(order_form, self.loc.APPLY_BUTTON1, timeout=1)

        # Добавление товара Container
        self.fun.click_element(order_form, self.loc.TAB_FREIGHT_GOODS, timeout=1)

        self.fun.click_element(order_form, self.loc.CREATE_BUTTON, timeout=1)
        self.fun.set_text_field(order_form, self.loc.NAME_TOV_RU, "Суперпупер1 штука 1которая 1очень 1нужная", timeout=1)
        self.fun.set_text_field(order_form, self.loc.NAME_TOV_EN, "A super-duper1 thing 11that is 1very 1necessary", timeout=1)
        self.fun.set_text_field(order_form, self.loc.NAME_NOTE, "1Быстро 1нужно 1привезти", timeout=1)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)

        # 5. Переключение на форму товара Container
        main_window = self.fun.get_product_form()
        main_window.set_focus()
        order_form = self.fun.app.window(**self.loc.PRODUCT_FORM)
        time.sleep(1)

        # 5. Добавление веса товара bulkership
        self.fun.set_text_field(order_form, self.loc.NET_WEIGHT, "0007", timeout=1)
        self.fun.set_text_field(order_form, self.loc.GROSS_WEIGHT, "9876", timeout=1)

        self.fun.click_element(order_form, self.loc.APPLY_BUTTON1, timeout=1)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)

        # 5. Переключение на форму Container
        main_window = self.fun.get_freight_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.fun.app.window(**self.loc.FREIGHT_FROM)
        time.sleep(1)
        # 5. Проверка полей

        # 5 Закрыть Container
        self.fun.click_element(order_form, self.loc.SAVE_BUTTON, timeout=1)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        order_form = self.fun.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)



        # 7. Перейти во вкладку Перевозок
        self.fun.click_element(main_window, self.loc.TAB_TRANSPORTATION, timeout=5)

        # 8. Создать морскую перевозку
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.TYPE_TRANSPORTATION, timeout=3)
        self.fun.click_element(main_window, self.loc.SEA_TRANSPORTATION, timeout=3)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

        # 9. Переключится на форму морской перевозки
        main_window = self.fun.get_sea_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.fun.app.window(**self.loc.SEA_FORM)
        time.sleep(1)

        # 9. Добавить маршрут
        self.fun.click_element(main_window, self.loc.TAB_ROUTES, timeout=3)

        # 9. Предэкспедирование
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.ROUTES_WINDOWS, timeout=3)
        self.fun.click_element(main_window, self.loc.PREFORWARDING, timeout=3)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)

        # 9. Отгрузка
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.ROUTES_WINDOWS, timeout=3)
        self.fun.click_element(main_window, self.loc.SHIPMENT, timeout=3)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)

        # 9. Перевалка 1
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.ROUTES_WINDOWS, timeout=3)
        self.fun.click_element(main_window, self.loc.TRANSSHIPMENT1, timeout=3)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)

        # 9. Перевалка 2
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.ROUTES_WINDOWS, timeout=3)
        self.fun.click_element(main_window, self.loc.TRANSSHIPMENT2, timeout=3)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)

        # 9. Прибытие
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.ROUTES_WINDOWS, timeout=3)
        self.fun.click_element(main_window, self.loc.ARRIVAL, timeout=3)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)

        # 9. выставление данных в маршруты
        self.fun.click_element(order_form, self.loc.PORT1, timeout=1)
        self.fun.click_element(order_form, self.loc.ROUTES_WINDOWS, timeout=1)
        self.fun.click_element(order_form, self.loc.RECIPIENT_1, timeout=1)

        self.fun.click_element(order_form, self.loc.PORT2, timeout=1)
        self.fun.click_element(order_form, self.loc.ROUTES_WINDOWS, timeout=1)
        self.fun.click_element(order_form, self.loc.RECIPIENT_2, timeout=1)

        self.fun.click_element(order_form, self.loc.PORT3, timeout=1)
        self.fun.click_element(order_form, self.loc.ROUTES_WINDOWS, timeout=1)
        self.fun.click_element(order_form, self.loc.RECIPIENT_3, timeout=1)

        self.fun.click_element(order_form, self.loc.PORT4, timeout=1)
        self.fun.click_element(order_form, self.loc.ROUTES_WINDOWS, timeout=1)
        self.fun.click_element(order_form, self.loc.RECIPIENT_4, timeout=1)

        self.fun.click_element(order_form, self.loc.PORT5, timeout=1)
        self.fun.click_element(order_form, self.loc.ROUTES_WINDOWS, timeout=1)
        self.fun.click_element(order_form, self.loc.RECIPIENT_5, timeout=1)

        self.fun.click_element(order_form, self.loc.RECIPIENT_1, timeout=1)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)



        # 10. Добавление груза
        self.fun.click_element(main_window, self.loc.TAB_FREIGHT, timeout=3)
        self.fun.click_element(order_form, self.loc.CREATE_BUTTON, timeout=1)
        self.fun.click_element(order_form, self.loc.OPEN_BUTTON, timeout=1)
        self.fun.click_element(order_form, self.loc.DELIVERY_CONDITION_0, timeout=1)
        self.fun.click_element(order_form, self.loc.DELIVERY_CONDITION_1, timeout=1)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)



        # Закрываем морскую перевозку
        self.fun.click_element(order_form, self.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.fun.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)

        # Во вкладке Перевозки, таблица



        # Создаем автоперевозку
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.TYPE_TRANSPORTATION, timeout=3)
        self.fun.click_element(main_window, self.loc.AUTO_TRANSPORTATION, timeout=3)
        keyboard.send_keys('{ENTER}')  # нажать на ОК работает если есть фокус на кнопке, могут быть проблемы

        # 5. Переключится на форму автоперевозки
        main_window = self.fun.get_auto_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.fun.app.window(**self.loc.AUTO_FORM)
        time.sleep(1)

        # 5. Проверка полей

        # 10. Добавление груза
        self.fun.click_element(main_window, self.loc.TAB_FREIGHT, timeout=3)
        self.fun.click_element(order_form, self.loc.CREATE_BUTTON, timeout=1)
        self.fun.click_element(order_form, self.loc.OPEN_BUTTON, timeout=1)
        self.fun.click_element(order_form, self.loc.DELIVERY_CONDITION_0, timeout=1)
        self.fun.click_element(order_form, self.loc.DELIVERY_CONDITION_1, timeout=1)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)

        # Закрываем автоперевозку
        self.fun.click_element(order_form, self.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.fun.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)






        # 7. Перейти во вкладку Экспедирование
        self.fun.click_element(main_window, self.loc.TAB_FORWARDING, timeout=3)

        # 8. Создать Экспедирование
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

        # 9. Переключится на форму Экспедирования
        main_window = self.fun.get_forwarding_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.fun.app.window(**self.loc.FORWARDING_FROM)
        time.sleep(1)

        # 10. Проверка полей


        # 15. Редактирование Экспедирование
        self.fun.click_element(order_form, self.loc.STATUS_COMBO, timeout=1)
        self.fun.click_element(order_form, self.loc.STATUS_FINISH, timeout=1)
        self.fun.click_element(order_form, self.loc.PRIORITY_COMBO, timeout=1)
        self.fun.click_element(order_form, self.loc.PRIORITY_COMBO_LOW, timeout=1)

        self.fun.click_element(order_form, self.loc.FORWARDING_FORWARDER, timeout=1)
        self.fun.click_element(order_form, self.loc.RECIPIENT_1, timeout=1)

        self.fun.click_element(order_form, self.loc.FORWARDING_TELEX, timeout=1)
        time.sleep(1)
        keyboard.send_keys('1')
        self.fun.click_element(order_form, self.loc.FORWARDING_RECEIVING_DOC, timeout=1)
        time.sleep(1)
        keyboard.send_keys('2')
        self.fun.click_element(order_form, self.loc.FORWARDING_NOMINATION, timeout=1)
        time.sleep(1)
        keyboard.send_keys('3')
        self.fun.set_text_field(main_window, self.loc.NOTE, "CAAU 111111 \n"
                                                        "MSMU 2222222 + СААU 333333  2х20 ставка перевоза по 7 000р/щт\n"
                                                        "\n"
                                                        "Иван Иванов Иванович 30.12.1985\n"
                                                        "0000 111111 МВД по Республике Дагестан от 05.07.2021 Мира 1 кв1\n"
                                                        "89888333222 SCANIA А777УЕ05 прицеп УЕ1111 05\n"
                                                        "погрузка визит 13\05 1:40 - 4:50 ;\n"
                                                        "сдача на КТСП 13/05 ", timeout=1)


        # Перейти во вкладку грузы
        self.fun.click_element(order_form, self.loc.TAB_FORWARDING_FREIGHT, timeout=1)

        # Добавить груз
        self.fun.click_element(order_form, self.loc.CREATE_BUTTON, timeout=1)
        self.fun.click_element(order_form, self.loc.OPEN_BUTTON, timeout=1)
        self.fun.click_element(order_form, self.loc.DELIVERY_CONDITION_0, timeout=1)
        self.fun.click_element(order_form, self.loc.DELIVERY_CONDITION_1, timeout=1)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)

        self.fun.click_element(order_form, self.loc.APPLY_BUTTON1, timeout=1)

        # 16. Проверка введенных данных

        self.fun.click_element(order_form, self.loc.SAVE_BUTTON, timeout=1)

        # 17. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.fun.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)



        # 22. Во вкладке Перевозки, таблица



        return self.fun.order_data

    def close(self):
        """Завершение работы приложения"""
        self.app.kill(soft=True)
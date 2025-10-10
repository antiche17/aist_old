from pywinauto import Application, keyboard
from locators.locators import LocOrders
from locators.function import Function
import time
import subprocess
import psutil


class WinAISTApp:
    def __init__(self):
        self.fun = Function()
        self.loc = LocOrders()
        self.app = self.fun.app

    def freight(self):
        # 1. Запуск приложения
        self.fun.start_application()
        #startup_window.set_focus()

        # 2. Нажатие кнопки Запуск
        #self.fun.click_element(startup_window, self.loc.AIST_EF, timeout=1)
        #self.fun.click_element(startup_window, self.loc.START_BUTTON, timeout=1)
        time.sleep(2)

        # 3. Переход в раздел Грузы
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(2)

        self.fun.click_element(main_window, self.loc.FREIGHT, timeout=3)
        time.sleep(8)

        # 3. Добавление колонок
        self.fun.right_click_element(main_window, self.loc.OTV_TABLE, timeout=3)

        keyboard.send_keys('{DOWN}' * 7)
        keyboard.send_keys('{ENTER}')

        self.fun.click_element_double(main_window, self.loc.ADDRESS_TABLE, timeout=1)
        self.fun.click_element_double_sp(main_window, self.loc.AUTO_TABLE)
        self.fun.click_element_double_sp(main_window, self.loc.NET_WEIGHT_TABLE,)
        self.fun.click_element_double_sp(main_window, self.loc.DRIVER_TABLE,)
        self.fun.click_element_double_sp(main_window, self.loc.DATA_MOD_TABLE)
        self.fun.click_element_double_sp(main_window, self.loc.DATA_CREATE_TABLE)
        self.fun.click_element_double_sp(main_window, self.loc.MEAS_TABLE)
        self.fun.click_element_double_sp(main_window, self.loc.CHANGED_TABLE)
        self.fun.click_element_double_sp(main_window, self.loc.CREATED_TE_TABLE)
        self.fun.click_element_double_sp(main_window, self.loc.QUANTITY_TABLE)
        self.fun.click_element_double_sp(main_window, self.loc.NEW_TABLE)
        self.fun.click_element_double_sp(main_window, self.loc.NUMBER_GTD_TABLE)
        self.fun.click_element_double_sp(main_window, self.loc.OTV_AUTO_TABLE)
        self.fun.click_element_double_sp(main_window, self.loc.PLAN_TABLE)
        self.fun.click_element_double_sp(main_window, self.loc.NOTE_TABLE)

        # 4. Создать груз
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)

        self.fun.click_element_sp(main_window, self.loc.CLIENT_COMBO)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)

        # 4. Создать заказа
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_ORDER_W)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_ORDER_CREATE)

        self.fun.click_element_sp(main_window, self.loc.ORDER_TYPE_COMBO)
        self.fun.click_element_sp(main_window, self.loc.LOGISTICS_ITEM)
        self.fun.click_element_sp(main_window, self.loc.CUSTOMER_COMBO)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)


        time.sleep(1)

        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_CREATE_TE)
        time.sleep(2)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TE1, timeout=2)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_CREATE_TYPE)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_CREATE_TYPE1)
        self.fun.set_text_field(main_window, self.loc.FREIGHT_CREATE_QUANTITY, 1, timeout=1)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_CREATE_UOM)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_CREATE_UOM1)
        text = self.fun.get_element_value(main_window, self.loc.FREIGHT_ORDER_W, timeout=1)

        # Сбор выставленных данных
        self.fun.order_data = {
            'name_client': self.fun.get_element_property_sp(main_window, self.loc.CLIENT_COMBO, "Value"),
            'order_number': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_ORDER_W, "Value"),
            'bul_type_freight': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_CREATE_TE, "Value"),
            'bul_type_te': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_CREATE_TYPE, "Value"),
            'bul_quantity': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_CREATE_QUANTITY, "Value"),
            'bul_uom': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_CREATE_UOM, "Value"),
            'bul_te_number': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_CREATE_ORDER, "Value"),
        }

        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON)

        # Фильтруем по номеру заказа
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_RESP_FOR_TABLE)
        keyboard.send_keys('{RIGHT}' * 27)
        keyboard.send_keys(text, with_spaces=True)
        keyboard.send_keys('{ENTER}')

        # Проверка данных
        self.fun.order_data.update({
            'order_number_table': self.fun.get_element_property_sp(main_window, self.loc.SEA_TAB_ORDER_NUMBER, "Value"),
        })

        # Открываем заказ
        self.fun.click_element_sp(main_window, self.loc.SEA_TAB_ORDER_NUMBER)

        # 12. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # Добавить получателя
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.APPLY_BUTTON1)

        # Проверка данных
        self.fun.order_data.update({
            'name_client_order': self.fun.get_element_property_sp(main_window, self.loc.CLIENT_COMBO, "Value"),
            'order_status': self.fun.get_element_property_sp(main_window, self.loc.STATUS_COMBO, "Value"),
            'order_priority': self.fun.get_element_property_sp(main_window, self.loc.PRIORITY_COMBO, "Value"),
            'order_otv': self.fun.get_element_property_sp(main_window, self.loc.RESPONSIBLE_COMBO, "Value"),
            'order_recipient': self.fun.get_element_property_sp(main_window, self.loc.RECIPIENT, "Value"),

        })

        # 6. Перейти во вкладку
        self.fun.click_element_sp(main_window, self.loc.TAB_FREIGHT)
        
        # 5. Открыть груз bulkership
        self.fun.click_element_double_sp(main_window, self.loc.FREIGHT_ITEM)

        # 5. Переключение на форму bulkership
        main_window = self.fun.get_freight_form()
        main_window.set_focus()
        time.sleep(1)

        main_window = self.fun.app.window(**self.loc.FREIGHT_FROM)
        time.sleep(1)

        # 5. Проверка полей
        self.fun.order_data.update({
            'bul_type_freight_form': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_TYPE_TEXT, "Name"),
            'bul_type_te_form': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_CREATE_TYPE, "Value"),
            'bul_quantity_form': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_TE_QUANTITY_FORM, "Value"),
            'bul_uom_form': self.fun.get_element_property(main_window, self.loc.FREIGHT_TE_UOM, "Value"),
            'bul_te_number_form': self.fun.get_element_property(main_window, self.loc.FREIGHT_TE_NUMBER_FORM, "Value"),
        })

        # 5 Редактирование формы bulkership
        self.fun.set_text_field(main_window, self.loc.FREIGHT_TE_NUMBER_FORM, "1234567", timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_TE_TYPE, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_LINE_7, timeout=1)
        self.fun.set_text_field(main_window, self.loc.FREIGHT_TE_QUANTITY_FORM, "77", timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_TE_UOM, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_LINE_3, timeout=1)

        self.fun.click_element(main_window, self.loc.UNLOADING, timeout=1)
        keyboard.send_keys('1')
        self.fun.set_text_field(main_window, self.loc.FREIGHT_NUMBER_SEAL_FORM, "12345678", timeout=1)
        self.fun.set_text_field(main_window, self.loc.FREIGHT_NUMBER_GTD_FORM, "23456789", timeout=2)
        self.fun.click_element(main_window, self.loc.FREIGHT_MODE_TO_FORM, timeout=1)
        self.fun.click_element(main_window, self.loc.DELIVERY_CONDITION_0, timeout=1)
        self.fun.click_element(main_window, self.loc.FORWARDING_RECEIVING_DO, timeout=1)
        keyboard.send_keys('2')
        self.fun.click_element(main_window, self.loc.FREIGHT_DATA_TO_FORM, timeout=1)
        keyboard.send_keys('3')
        self.fun.set_text_field(main_window, self.loc.NOTE_CONTAINER, "MSMU2222222 + СААU 333333  2х20 ставка перевоза по 7 000р/щт", timeout=1)


        # Добавление товара bulkership
        self.fun.click_element(main_window, self.loc.TAB_FREIGHT_GOODS, timeout=1)

        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
        self.fun.set_text_field(main_window, self.loc.NAME_TOV_RU, "Суперпупер штука которая очень нужная", timeout=1)
        self.fun.set_text_field(main_window, self.loc.NAME_TOV_EN, "A super-duper thing that is very necessary" ,timeout=1)
        self.fun.set_text_field(main_window, self.loc.NAME_NOTE, "Быстро нужно привезти",timeout=1)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

        # 5. Переключение на форму товара bulkership
        main_window = self.fun.get_product_form()
        main_window.set_focus()


        # 5. Добавление вес товара bulkership
        self.fun.set_text_field(main_window, self.loc.NET_WEIGHT, "1000", timeout=1)
        self.fun.set_text_field(main_window, self.loc.GROSS_WEIGHT, "2345", timeout=1)

        self.fun.click_element(main_window, self.loc.APPLY_BUTTON1, timeout=1)

        # 5. Проверка полей
        self.fun.order_data.update({
            'bul_te_net': self.fun.get_element_property(main_window, self.loc.NET_WEIGHT, "Value"),
            'bul_te_gross': self.fun.get_element_property(main_window, self.loc.GROSS_WEIGHT, "Value"),
        })

        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

        # 5. Переключение на форму bulkership
        main_window = self.fun.get_freight_form()
        main_window.set_focus()
        time.sleep(1)

        self.fun.click_element(main_window, self.loc.APPLY_BUTTON1, timeout=1)
        self.fun.click_element(main_window, self.loc.TAB_INFO, timeout=1)

        # 5. Проверка полей bulkership
        self.fun.order_data.update({
            'bul_number_form_mod': self.fun.get_element_property(main_window, self.loc.FREIGHT_TE_NUMBER_FORM, "Value"),
            'bul_type_form_mod': self.fun.get_element_property(main_window, self.loc.FREIGHT_CREATE_TYPE, "Value"),
            'bul_te_number_mod': self.fun.get_element_property(main_window, self.loc.FREIGHT_TE_NUMBER_FORM, "Value"),
            'bul_unloading_mod': self.fun.get_element_property(main_window, self.loc.UNLOADING, "Value"),
            'bul_seal_num_form_mod': self.fun.get_element_property(main_window, self.loc.FREIGHT_NUMBER_SEAL_FORM, "Value"),
            'bul_do_form_mod': self.fun.get_element_property(main_window, self.loc.FORWARDING_RECEIVING_DO, "Value"),
            'bul_regime_to_form_mod': self.fun.get_element_property(main_window, self.loc.FREIGHT_MODE_TO_FORM, "Value"),
            'bul_data_to_form_mod': self.fun.get_element_property(main_window, self.loc.FREIGHT_DATA_TO_FORM, "Value"),
            'bul_note_form_mod': self.fun.get_element_property(main_window, self.loc.NOTE_CONTAINER, "Value"),
            'bul_gtd_form_mod': self.fun.get_element_property(main_window, self.loc.FREIGHT_NUMBER_GTD_FORM, "Value"),
            'bul_quantity_form_mod': self.fun.get_element_property(main_window, self.loc.FREIGHT_QUANTITY_APPLY, "Value"),
            'bul_uom_form_mod': self.fun.get_element_property(main_window, self.loc.FREIGHT_CREATE_UOM_SAVE, "Value"),
            'bul_create_form': self.fun.get_element_property(main_window, self.loc.FREIGHT_CREATE_FORM, "Name"),
        })

        # 5 Закрыть bulkership
        self.fun.click_element(main_window, self.loc.SAVE_BUTTON, timeout=1)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
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

        # 5. Открыть Container
        self.fun.click_element_double(main_window, self.loc.FREIGHT_ITEM2, timeout=5)

        # 5. Переключение на форму Container
        main_window = self.fun.get_freight_form()
        main_window.set_focus()
        time.sleep(1)

        # 5. Проверка полей

        # 5 Редактирование формы Container
        self.fun.set_text_field(main_window, self.loc.FREIGHT_TE_NUMBER_FORM, "TARE1234567", timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_TE_TYPE, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_LINE_7, timeout=1)

        self.fun.click_element(main_window, self.loc.UNLOADING, timeout=1)
        keyboard.send_keys('4')
        self.fun.set_text_field(main_window, self.loc.FREIGHT_NUMBER_SEAL_FORM, "12345678", timeout=1)
        self.fun.set_text_field(main_window, self.loc.FREIGHT_NUMBER_GTD_FORM_CONTAINER, "23456789", timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_MODE_TO_FORM, timeout=1)
        self.fun.click_element(main_window, self.loc.DELIVERY_CONDITION_0, timeout=1)
        self.fun.click_element(main_window, self.loc.FORWARDING_RECEIVING_DO, timeout=1)
        keyboard.send_keys('5')
        self.fun.click_element(main_window, self.loc.FREIGHT_DATA_TO_FORM, timeout=1)
        keyboard.send_keys('6')
        self.fun.set_text_field(main_window, self.loc.NOTE_CONTAINER, "MSMU2222222 + СААU 333333  2х20 ставка перевоза по 7 000р/щт", timeout=1)
        self.fun.click_element(main_window, self.loc.APPLY_BUTTON1, timeout=1)

        # Добавление товара Container
        self.fun.click_element(main_window, self.loc.TAB_FREIGHT_GOODS, timeout=1)

        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
        self.fun.set_text_field(main_window, self.loc.NAME_TOV_RU, "Суперпупер1 штука 1которая 1очень 1нужная", timeout=1)
        self.fun.set_text_field(main_window, self.loc.NAME_TOV_EN, "A super-duper1 thing 11that is 1very 1necessary", timeout=1)
        self.fun.set_text_field(main_window, self.loc.NAME_NOTE, "1Быстро 1нужно 1привезти", timeout=1)


        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

        # 5. Переключение на форму товара Container
        main_window = self.fun.get_product_form()
        main_window.set_focus()
        time.sleep(1)
        self.fun.order_data.update({


        })

        # 5. Добавление веса товара bulkership
        self.fun.set_text_field(main_window, self.loc.NET_WEIGHT, "0007", timeout=1)
        self.fun.set_text_field(main_window, self.loc.GROSS_WEIGHT, "9876", timeout=1)

        self.fun.click_element(main_window, self.loc.APPLY_BUTTON1, timeout=1)
        self.fun.order_data.update({
            'con_te_net': self.fun.get_element_property(main_window, self.loc.NET_WEIGHT, "Value"),
            'con_te_gross': self.fun.get_element_property(main_window, self.loc.GROSS_WEIGHT, "Value"),
        })
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

        # 5. Переключение на форму Container
        main_window = self.fun.get_freight_form()
        main_window.set_focus()
        time.sleep(1)

        self.fun.click_element(main_window, self.loc.APPLY_BUTTON1, timeout=1)
        self.fun.click_element(main_window, self.loc.TAB_INFO, timeout=1)

        # 5. Проверка полей bulkership
        self.fun.order_data.update({
            'con_number_form_mod': self.fun.get_element_property(main_window, self.loc.FREIGHT_TE_NUMBER_FORM, "Value"),
            'con_type_form_mod': self.fun.get_element_property(main_window, self.loc.FREIGHT_CREATE_TYPE, "Value"),
            'con_te_number_mod': self.fun.get_element_property(main_window, self.loc.FREIGHT_TE_NUMBER_FORM, "Value"),
            'con_unloading_mod': self.fun.get_element_property(main_window, self.loc.UNLOADING, "Value"),
            'con_seal_num_form_mod': self.fun.get_element_property(main_window, self.loc.FREIGHT_NUMBER_SEAL_FORM, "Value"),
            'con_do_form_mod': self.fun.get_element_property(main_window, self.loc.FORWARDING_RECEIVING_DO, "Value"),
            'con_regime_to_form_mod': self.fun.get_element_property(main_window, self.loc.FREIGHT_MODE_TO_FORM, "Value"),
            'con_data_to_form_mod': self.fun.get_element_property(main_window, self.loc.FREIGHT_DATA_TO_FORM, "Value"),
            'con_note_form_mod': self.fun.get_element_property(main_window, self.loc.NOTE_CONTAINER, "Value"),
            'con_gtd_form_mod': self.fun.get_element_property(main_window, self.loc.FREIGHT_NUMBER_GTD_FORM_CONTAINER, "Value"),
            'con_quantity_form_mod': self.fun.get_element_property(main_window, self.loc.FREIGHT_QUANTITY_APPLY, "Value"),
            'con_uom_form_mod': self.fun.get_element_property(main_window, self.loc.FREIGHT_CREATE_UOM_SAVE, "Value"),
            'con_create_form': self.fun.get_element_property(main_window, self.loc.FREIGHT_CREATE_FORM, "Name"),
        })

        # 5 Закрыть Container
        self.fun.click_element(main_window, self.loc.SAVE_BUTTON, timeout=1)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
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

        # 9. Изменить данные
        self.fun.click_element(main_window, self.loc.OCEAN_LINE, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TE1, timeout=1)
        self.fun.set_text_field(main_window, self.loc.OCEAN_KONOS, "Документы №1", timeout=1)
        self.fun.click_element(main_window, self.loc.FEEDER_LINE, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TE2, timeout=1)
        self.fun.set_text_field(main_window, self.loc.FEEDER_KONOS, "Документы №2", timeout=1)
        self.fun.click_element(main_window, self.loc.APPLY_BUTTON1, timeout=1)

        self.fun.order_data.update({
            'sea_ocean_line_form': self.fun.get_element_property(main_window, self.loc.OCEAN_LINE, "Value"),
            'sea_ocean_konos_form': self.fun.get_element_property(main_window, self.loc.OCEAN_KONOS, "Value"),
            'sea_feeder_line_form': self.fun.get_element_property(main_window, self.loc.FEEDER_LINE, "Value"),
            'sea_feeder_konos_form': self.fun.get_element_property(main_window, self.loc.FEEDER_KONOS, "Value"),
        })

        # 9. Добавить маршрут
        self.fun.click_element(main_window, self.loc.TAB_ROUTES, timeout=3)

        # 9. Отгрузка
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.ROUTES_WINDOWS, timeout=3)
        self.fun.click_element(main_window, self.loc.SHIPMENT, timeout=3)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

        # 9. Перевалка 1
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.ROUTES_WINDOWS, timeout=3)
        self.fun.click_element(main_window, self.loc.TRANSSHIPMENT1, timeout=3)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

        # 9. Прибытие
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.ROUTES_WINDOWS, timeout=3)
        self.fun.click_element(main_window, self.loc.ARRIVAL, timeout=3)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

        # 9. Порт выставление данных в маршруты
        self.fun.click_element(main_window, self.loc.PORT3, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(main_window, self.loc.PORT3, timeout=1)
        self.fun.click_element(main_window, self.loc.NAME_LINE3, timeout=1)

        # 9. Терминал выставление данных в маршруты
        self.fun.click_element(main_window, self.loc.TERMINAL_LINE3, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(main_window, self.loc.TERMINAL_LINE3, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TE3, timeout=1)

        # 9. Судно выставление данных в маршруты
        self.fun.click_element(main_window, self.loc.SHIP_LINE1, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(main_window, self.loc.SHIP_LINE1, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        self.fun.click_element(main_window, self.loc.SHIP_LINE2, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(main_window, self.loc.SHIP_LINE2, timeout=1)
        keyboard.send_keys('{DOWN}' *2)
        keyboard.send_keys('{ENTER}')

        # 10. Плановая дата прибытия
        self.fun.click_element(main_window, self.loc.PLAN_ARRIVAL3, timeout=3)
        keyboard.send_keys('7')

        # 10. Фактическая дата прибытия
        self.fun.click_element(main_window, self.loc.FACT_ARRIVAL3, timeout=3)
        keyboard.send_keys('8')

        self.fun.click_element(main_window, self.loc.APPLY_BUTTON1, timeout=1)

        self.fun.order_data.update({
            'sea_terminal_form': self.fun.get_element_property(main_window, self.loc.TERMINAL_LINE3, "Value"),
            'sea_port_form': self.fun.get_element_property(main_window, self.loc.PORT3, "Value"),
            'sea_plan_arrival_form': self.fun.get_element_property(main_window, self.loc.PLAN_ARRIVAL3, "Value"),
            'sea_fact_arrival_form': self.fun.get_element_property(main_window, self.loc.FACT_ARRIVAL3, "Value"),
            'sea_ship_shipment_form': self.fun.get_element_property(main_window, self.loc.SHIP_LINE1, "Value"),
            'sea_ship_trans1_form': self.fun.get_element_property(main_window, self.loc.SHIP_LINE2, "Value"),

        })

        # 10. Добавить груз
        self.fun.click_element(main_window, self.loc.TAB_FREIGHT, timeout=1)
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.loc.OPEN_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.loc.DELIVERY_CONDITION_0, timeout=1)
        self.fun.click_element(main_window, self.loc.DELIVERY_CONDITION_1, timeout=1)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

        # Закрываем морскую перевозку
        self.fun.click_element(main_window, self.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # Создаем автоперевозку
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.TYPE_TRANSPORTATION, timeout=3)
        self.fun.click_element(main_window, self.loc.AUTO_TRANSPORTATION, timeout=3)
        keyboard.send_keys('{ENTER}')  # нажать на ОК работает если есть фокус на кнопке, могут быть проблемы

        # 5. Переключится на форму автоперевозки
        main_window = self.fun.get_auto_form()
        main_window.set_focus()
        time.sleep(1)

        # Добавляем данные автоперевозки
        self.fun.click_element(main_window, self.loc.STATUS_COMBO, timeout=1)
        self.fun.click_element(main_window, self.loc.RESPONSIBLE_COMBO, timeout=1)
        self.fun.click_element(main_window, self.loc.APPLY_BUTTON1, timeout=1)

        self.fun.order_data.update({
            'auto_status': self.fun.get_element_property(main_window, self.loc.STATUS_COMBO, "Value"),
            'auto_otv': self.fun.get_element_property(main_window, self.loc.RESPONSIBLE_COMBO, "Value"),
        })

        # 9. Добавить маршрут
        self.fun.click_element(main_window, self.loc.TAB_ROUTES, timeout=3)

        # 9. Отгрузка
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.ROUTES_WINDOWS, timeout=3)
        self.fun.click_element(main_window, self.loc.SHIPMENT, timeout=3)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

        # 9. Прибытие
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.ROUTES_WINDOWS, timeout=3)
        self.fun.click_element(main_window, self.loc.ARRIVAL, timeout=3)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

        # 9. Адрес добавить
        self.fun.click_element(main_window, self.loc.ADDRESS2, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(main_window, self.loc.ADDRESS2, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TE2, timeout=1)

        # 9. Водитель добавить
        self.fun.click_element(main_window, self.loc.DRIVER, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(main_window, self.loc.DRIVER, timeout=1)
        self.fun.click_element(main_window, self.loc.NAME_LINE1, timeout=1)

        # 10. Автомобиль
        self.fun.click_element(main_window, self.loc.AUTO, timeout=1)
        keyboard.send_keys('х777хх 77 rus')
        keyboard.send_keys('{ENTER}')

        # 10. Плановая дата прибытия
        self.fun.click_element(main_window, self.loc.PLAN_ARRIVAL2, timeout=1)
        keyboard.send_keys('9')
        self.fun.click_element(main_window, self.loc.APPLY_BUTTON1, timeout=1)

        # 16. Проверка введенных данных
        self.fun.order_data.update({
            'auto_address': self.fun.get_element_property(main_window, self.loc.ADDRESS2, "Value"),
            'auto_plan_data': self.fun.get_element_property(main_window, self.loc.PLAN_ARRIVAL2, "Value"),
            'auto_driver': self.fun.get_element_property(main_window, self.loc.DRIVER, "Value"),
            'auto_number_auto': self.fun.get_element_property(main_window, self.loc.AUTO, "Value"),
        })

        # 10. Добавление груза
        self.fun.click_element(main_window, self.loc.TAB_FREIGHT, timeout=3)
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.loc.OPEN_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.loc.DELIVERY_CONDITION_0, timeout=1)
        self.fun.click_element(main_window, self.loc.DELIVERY_CONDITION_1, timeout=1)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

        # Закрываем автоперевозку
        self.fun.click_element(main_window, self.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        self.fun.order_data.update({
            'type_transport1': self.fun.get_element_property(main_window, self.loc.TRANSPORTATION_NUMBER1, "Value"),
            'type_transport2': self.fun.get_element_property(main_window, self.loc.TRANSPORTATION_NUMBER2, "Value"),

        })

        # 7. Перейти во вкладку Экспедирование
        self.fun.click_element(main_window, self.loc.TAB_FORWARDING, timeout=3)

        # 8. Создать Экспедирование
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

        # 9. Переключится на форму Экспедирования
        main_window = self.fun.get_forwarding_form()
        main_window.set_focus()
        time.sleep(1)

        # 15. Редактирование Экспедирование
        self.fun.click_element(main_window, self.loc.STATUS_COMBO, timeout=1)
        self.fun.click_element(main_window, self.loc.STATUS_FINISH, timeout=1)
        self.fun.click_element(main_window, self.loc.PRIORITY_COMBO, timeout=1)
        self.fun.click_element(main_window, self.loc.PRIORITY_COMBO_LOW, timeout=1)

        self.fun.click_element(main_window, self.loc.FORWARDING_FORWARDER, timeout=1)
        self.fun.click_element(main_window, self.loc.RECIPIENT_1, timeout=1)

        self.fun.click_element(main_window, self.loc.FORWARDING_TELEX, timeout=1)
        time.sleep(1)
        keyboard.send_keys('10')
        self.fun.click_element(main_window, self.loc.FORWARDING_RECEIVING_DOC, timeout=1)
        time.sleep(1)
        keyboard.send_keys('11')
        self.fun.click_element(main_window, self.loc.FORWARDING_NOMINATION, timeout=1)
        time.sleep(1)
        keyboard.send_keys('12')
        self.fun.set_text_field(main_window, self.loc.NOTE, "CAAU 111111 \n"
                                                        "MSMU 2222222 + СААU 333333  2х20 ставка перевоза по 7 000р/щт\n"
                                                        "\n"
                                                        "Иван Иванов Иванович 30.12.1985\n"
                                                        "0000 111111 МВД по Республике Дагестан от 05.07.2021 Мира 1 кв1\n"
                                                        "89888333222 SCANIA А777УЕ05 прицеп УЕ1111 05\n"
                                                        "погрузка визит 13\05 1:40 - 4:50 ;\n"
                                                        "сдача на КТСП 13/05 ", timeout=1)


        # Перейти во вкладку грузы
        self.fun.click_element(main_window, self.loc.TAB_FORWARDING_FREIGHT, timeout=1)

        # Добавить груз
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.loc.OPEN_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.loc.DELIVERY_CONDITION_0, timeout=1)
        self.fun.click_element(main_window, self.loc.DELIVERY_CONDITION_1, timeout=1)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

        self.fun.click_element(main_window, self.loc.APPLY_BUTTON1, timeout=1)

        # 16. Проверка введенных данных
        self.fun.order_data.update({
            'forwarding_otv': self.fun.get_element_property(main_window, self.loc.RESPONSIBLE_COMBO, "Value"),
            'forwarding_telex': self.fun.get_element_property(main_window, self.loc.FORWARDING_TELEX, "Value"),
            'forwarding_nomination': self.fun.get_element_property(main_window, self.loc.FORWARDING_NOMINATION, "Value"),
            'forwarding_receiving_doc': self.fun.get_element_property(main_window, self.loc.FORWARDING_RECEIVING_DOC, "Value"),

        })

        self.fun.click_element(main_window, self.loc.SAVE_BUTTON, timeout=1)

        # 17. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        self.fun.order_data.update({
            'forwarding_number': self.fun.get_element_property(main_window, self.loc.FORWARDING_NUMBER, "Value"),
        })

        self.fun.click_element(main_window, self.loc.SAVE_BUTTON, timeout=1)

        # 22. В таблицу грузы
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(1)

        self.fun.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=1)
        time.sleep(2)
        self.fun.click_element(main_window, self.loc.FREIGHT_ORDER_TABLE, timeout=1)
        time.sleep(1)

        # 5. Проверка середины полей в таблице до поля Заказ
        self.fun.order_data.update({
            'bul_data_to_table': self.fun.get_element_property(main_window, self.loc.DATA_TO_TABLE2, "Value"),
            'bul_ocean_line_table': self.fun.get_element_property(main_window, self.loc.OCEAN_LINE_TABLE2, "Value"),
            'bul_sea_ship_shipment_table': self.fun.get_element_property(main_window, self.loc.OCEAN_SHIP_TABLE2, "Value"),
            'bul_ocean_konos_table': self.fun.get_element_property(main_window, self.loc.OCEAN_KONOS_TABLE2, "Value"),
            'bul_feeder_line_table': self.fun.get_element_property(main_window, self.loc.FEEDER_LINE_TABLE2, "Value"),
            'bul_sea_ship_trans1_table': self.fun.get_element_property(main_window, self.loc.FEEDER_PORT_TABLE2, "Value"),
            'bul_feeder_konos_table': self.fun.get_element_property(main_window, self.loc.FEEDER_KONOS_TABLE2, "Value"),
            'bul_transport_table': self.fun.get_element_property(main_window, self.loc.TRANSPORT_TABLE2, "Value"),

            'con_data_to_table': self.fun.get_element_property(main_window, self.loc.DATA_TO_TABLE1, "Value"),
            'con_ocean_line_table': self.fun.get_element_property(main_window, self.loc.OCEAN_LINE_TABLE1, "Value"),
            'con_sea_ship_shipment_table': self.fun.get_element_property(main_window, self.loc.OCEAN_SHIP_TABLE1, "Value"),
            'con_ocean_konos_table': self.fun.get_element_property(main_window, self.loc.OCEAN_KONOS_TABLE1, "Value"),
            'con_feeder_line_table': self.fun.get_element_property(main_window, self.loc.FEEDER_LINE_TABLE1, "Value"),
            'con_sea_ship_trans1_table': self.fun.get_element_property(main_window, self.loc.FEEDER_PORT_TABLE1, "Value"),
            'con_feeder_konos_table': self.fun.get_element_property(main_window, self.loc.FEEDER_KONOS_TABLE1, "Value"),
            'con_transport_table': self.fun.get_element_property(main_window, self.loc.TRANSPORT_TABLE1, "Value"),
        })

        keyboard.send_keys('{RIGHT}' * 30)
        time.sleep(4)

        # 5. Проверка скрытых полей в таблице
        self.fun.order_data.update({
            'bul_note_table': self.fun.get_element_property(main_window, self.loc.NOTE_TE_TABLE2, "Value"),
            'bul_order_otv_table': self.fun.get_element_property(main_window, self.loc.RESPONSIBLE_ORDER_TABLE2, "Value"),
            'bul_forwarding_number_table': self.fun.get_element_property(main_window, self.loc.EXPEDITION_TABLE2, "Value"),
            'bul_net_table': self.fun.get_element_property(main_window, self.loc.WEIGHT_NETTO_TABLE2, "Value"),
            'bul_auto_number_auto_table': self.fun.get_element_property(main_window, self.loc.CAR_TABLE2, "Value"),
            'bul_auto_address_table': self.fun.get_element_property(main_window, self.loc.ADDRESS_TABLE2, "Value"),
            'bul_auto_driver_table': self.fun.get_element_property(main_window, self.loc.DRIVER_TABLE2, "Value"),
            'bul_auto_otv_table': self.fun.get_element_property(main_window, self.loc.OTV_AUTO_TABLE2, "Value"),
            'bul_auto_plan_data_table': self.fun.get_element_property(main_window, self.loc.DELIVERY_DATE_PLAN_TABLE2, "Value"),
            'bul_gtd_table': self.fun.get_element_property(main_window, self.loc.GTD_NUMBER_TABLE2, "Value"),
            'bul_quantity_table': self.fun.get_element_property(main_window, self.loc.QUANTITY_TABLE2, "Value"),
            'bul_uom_table': self.fun.get_element_property(main_window, self.loc.MEASUREMENT_UNIT_TABLE2, "Value"),
            'bul_otv_table': self.fun.get_element_property(main_window, self.loc.OTV_AUTO_TABLE2, "Value"),
            'bul_create_table': self.fun.get_element_property(main_window, self.loc.CREATED_TE_TABLE2, "Value"),

            'con_note_table': self.fun.get_element_property(main_window, self.loc.NOTE_TE_TABLE1, "Value"),
            'con_order_otv_table': self.fun.get_element_property(main_window, self.loc.RESPONSIBLE_ORDER_TABLE1, "Value"),
            'con_forwarding_number_table': self.fun.get_element_property(main_window, self.loc.EXPEDITION_TABLE1, "Value"),
            'con_net_table': self.fun.get_element_property(main_window, self.loc.WEIGHT_NETTO_TABLE1, "Value"),
            'con_auto_number_auto_table': self.fun.get_element_property(main_window, self.loc.CAR_TABLE1, "Value"),
            'con_auto_address_table': self.fun.get_element_property(main_window, self.loc.ADDRESS_TABLE1, "Value"),
            'con_auto_driver_table': self.fun.get_element_property(main_window, self.loc.DRIVER_TABLE1, "Value"),
            'con_auto_otv_table': self.fun.get_element_property(main_window, self.loc.OTV_AUTO_TABLE1, "Value"),
            'con_auto_plan_data_table': self.fun.get_element_property(main_window, self.loc.DELIVERY_DATE_PLAN_TABLE1, "Value"),
            'con_gtd_table': self.fun.get_element_property(main_window, self.loc.GTD_NUMBER_TABLE1, "Value"),
            'con_quantity_table': self.fun.get_element_property(main_window, self.loc.QUANTITY_TABLE1, "Value"),
            'con_uom_table': self.fun.get_element_property(main_window, self.loc.MEASUREMENT_UNIT_TABLE1, "Value"),
            'con_otv_table': self.fun.get_element_property(main_window, self.loc.OTV_AUTO_TABLE1, "Value"),
            'con_create_table': self.fun.get_element_property(main_window, self.loc.CREATED_TE_TABLE1, "Value"),
        })
        time.sleep(1)
        keyboard.send_keys('{LEFT}' * 47)
        time.sleep(2)

        # 5. Проверка открытых полей в таблице до Телекс-релиза
        self.fun.order_data.update({
            'bul_otv_table': self.fun.get_element_property(main_window, self.loc.OTV_FOR_TABLE2, "Value"),
            'bul_auto_status_table': self.fun.get_element_property(main_window, self.loc.STATUS_AUTO_TABLE2, "Value"),
            'bul_recipient_table': self.fun.get_element_property(main_window, self.loc.RECIPIENT_TABLE2, "Value"),
            'bul_client_table': self.fun.get_element_property(main_window, self.loc.CLIENT_FOR_TABLE2, "Value"),
            'bul_seal_num_table': self.fun.get_element_property(main_window, self.loc.SEAL_NUMBER_TABLE2, "Value"),
            'bul_te_table': self.fun.get_element_property(main_window, self.loc.TE_TABLE2, "Name"),
            'bul_type_table': self.fun.get_element_property(main_window, self.loc.TYPE_TE_TABLE2, "Value"),
            'bul_gross_table': self.fun.get_element_property(main_window, self.loc.FREIGHT_GROSS_TABLE2, "Value"),
            'bul_number_table': self.fun.get_element_property(main_window, self.loc.NUM_TE_TABLE2, "Value"),
            'bul_sea_terminal_table': self.fun.get_element_property(main_window, self.loc.TERMINAL_TABLE2, "Value"),
            'bul_port_table': self.fun.get_element_property(main_window, self.loc.PORT_TABLE2, "Value"),
            'bul_plan_arrival_table': self.fun.get_element_property(main_window, self.loc.PLAN_ARRIVAL_TABLE1, "Value"),
            'bul_fact_arrival_table': self.fun.get_element_property(main_window, self.loc.FACT_ARRIVAL_TABLE2, "Value"),
            'bul_unloading_table': self.fun.get_element_property(main_window, self.loc.FACT_UNLOADING_TABLE2, "Value"),
            'bul_do_table': self.fun.get_element_property(main_window, self.loc.DO_TABLE2, "Value"),
            'bul_forwarding_doc_table': self.fun.get_element_property(main_window, self.loc.DOC_TABLE2, "Value"),
            'bul_nomination_table': self.fun.get_element_property(main_window, self.loc.NOMINATION_TABLE2, "Value"),
            'bul_regime_to_table': self.fun.get_element_property(main_window, self.loc.REGIMEN_TABLE2, "Value"),
            'bul_telex_table': self.fun.get_element_property(main_window, self.loc.TELEX_TABLE2, "Value"),

            'con_otv_table': self.fun.get_element_property(main_window, self.loc.OTV_FOR_TABLE1, "Value"),
            'con_auto_status_table': self.fun.get_element_property(main_window, self.loc.STATUS_AUTO_TABLE1, "Value"),
            'con_recipient_table': self.fun.get_element_property(main_window, self.loc.RECIPIENT_TABLE1, "Value"),
            'con_client_table': self.fun.get_element_property(main_window, self.loc.CLIENT_FOR_TABLE1, "Value"),
            'con_seal_num_table': self.fun.get_element_property(main_window, self.loc.SEAL_NUMBER_TABLE1, "Value"),
            'con_te_table': self.fun.get_element_property(main_window, self.loc.TE_TABLE1, "Name"),
            'con_type_table': self.fun.get_element_property(main_window, self.loc.TYPE_TE_TABLE1, "Value"),
            'con_gross_table': self.fun.get_element_property(main_window, self.loc.FREIGHT_GROSS_TABLE1, "Value"),
            'con_number_table': self.fun.get_element_property(main_window, self.loc.NUM_TE_TABLE1, "Value"),
            'con_sea_terminal_table': self.fun.get_element_property(main_window, self.loc.TERMINAL_TABLE1, "Value"),
            'con_port_table': self.fun.get_element_property(main_window, self.loc.PORT_TABLE1, "Value"),
            'con_plan_arrival_table': self.fun.get_element_property(main_window, self.loc.PLAN_ARRIVAL_TABLE1, "Value"),
            'con_fact_arrival_table': self.fun.get_element_property(main_window, self.loc.FACT_ARRIVAL_TABLE1, "Value"),
            'con_unloading_table': self.fun.get_element_property(main_window, self.loc.FACT_UNLOADING_TABLE1, "Value"),
            'con_do_table': self.fun.get_element_property(main_window, self.loc.DO_TABLE1, "Value"),
            'con_forwarding_doc_table': self.fun.get_element_property(main_window, self.loc.DOC_TABLE1, "Value"),
            'con_nomination_table': self.fun.get_element_property(main_window, self.loc.NOMINATION_TABLE1, "Value"),
            'con_regime_to_table': self.fun.get_element_property(main_window, self.loc.REGIMEN_TABLE1, "Value"),
            'con_telex_table': self.fun.get_element_property(main_window, self.loc.TELEX_TABLE1, "Value"),

        })

        # Изменяем данные в таблице
        self.fun.click_element(main_window, self.loc.OTV_FOR_TABLE2, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(main_window, self.loc.OTV_FOR_TABLE2, timeout=1)
        self.fun.click_element(main_window, self.loc.CUSTOMER_ITEM, timeout=1)

        self.fun.click_element(main_window, self.loc.STATUS_AUTO_TABLE2, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(main_window, self.loc.STATUS_AUTO_TABLE2, timeout=1)
        self.fun.click_element(main_window, self.loc.STATUS_COMBO_FINISH, timeout=1)

        self.fun.click_element(main_window, self.loc.SEAL_NUMBER_TABLE1, timeout=1)
        keyboard.send_keys("Номер пломбы №1")
        self.fun.click_element(main_window, self.loc.SEAL_NUMBER_TABLE2, timeout=1)
        keyboard.send_keys("2Номер пломбы №2")

        self.fun.click_element(main_window, self.loc.TERMINAL_TABLE2, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(main_window, self.loc.TERMINAL_TABLE2, timeout=1)
        self.fun.click_element(main_window, self.loc.CUSTOMER_ITEM, timeout=1)

        self.fun.click_element(main_window, self.loc.PORT_TABLE2, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(main_window, self.loc.PORT_TABLE2, timeout=1)
        self.fun.click_element(main_window, self.loc.NAME_LINE1, timeout=1)

        self.fun.click_element(main_window, self.loc.PLAN_ARRIVAL_TABLE1, timeout=1)
        keyboard.send_keys('20')

        self.fun.click_element(main_window, self.loc.FACT_ARRIVAL_TABLE2, timeout=1)
        keyboard.send_keys('21')

        self.fun.click_element(main_window, self.loc.FACT_UNLOADING_TABLE1, timeout=1)
        keyboard.send_keys('22')

        self.fun.click_element(main_window, self.loc.FACT_UNLOADING_TABLE2, timeout=1)
        keyboard.send_keys('23')

        self.fun.click_element(main_window, self.loc.DO_TABLE1, timeout=1)
        keyboard.send_keys('24')

        self.fun.click_element(main_window, self.loc.DO_TABLE2, timeout=1)
        keyboard.send_keys('25')

        self.fun.click_element(main_window, self.loc.DOC_TABLE2, timeout=1)
        keyboard.send_keys('26')

        self.fun.click_element(main_window, self.loc.REGIMEN_TABLE1, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(main_window, self.loc.REGIMEN_TABLE1, timeout=1)
        self.fun.click_element(main_window, self.loc.DELIVERY_CONDITION_1, timeout=1)

        self.fun.click_element(main_window, self.loc.REGIMEN_TABLE2, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(main_window, self.loc.REGIMEN_TABLE2, timeout=1)
        self.fun.click_element(main_window, self.loc.DELIVERY_CONDITION_2, timeout=1)

        self.fun.click_element(main_window, self.loc.TELEX_TABLE2, timeout=1)
        keyboard.send_keys('27')
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=1)
        time.sleep(2)

        self.fun.order_data.update({
            'otv_table': self.fun.get_element_property(main_window, self.loc.OTV_FOR_TABLE2, "Value"),
            'status_table': self.fun.get_element_property(main_window, self.loc.STATUS_AUTO_TABLE2, "Value"),
            'seal_number_table_con': self.fun.get_element_property(main_window, self.loc.SEAL_NUMBER_TABLE1, "Value"),
            'seal_number_table_bul': self.fun.get_element_property(main_window, self.loc.SEAL_NUMBER_TABLE2, "Value"),
            'terminal_table': self.fun.get_element_property(main_window, self.loc.TERMINAL_TABLE2, "Value"),
            'port_table': self.fun.get_element_property(main_window, self.loc.PORT_TABLE2, "Value"),
            'plan_arrival_table': self.fun.get_element_property(main_window, self.loc.PLAN_ARRIVAL_TABLE1, "Value"),

            'fact_arrival_table': self.fun.get_element_property(main_window, self.loc.FACT_ARRIVAL_TABLE2, "Value"),
            'unloading_table_con': self.fun.get_element_property(main_window, self.loc.FACT_UNLOADING_TABLE1, "Value"),
            'unloading_table_bul': self.fun.get_element_property(main_window, self.loc.FACT_UNLOADING_TABLE2, "Value"),
            'do_table_con': self.fun.get_element_property(main_window, self.loc.DO_TABLE1, "Value"),

            'do_table_bul': self.fun.get_element_property(main_window, self.loc.DO_TABLE2, "Value"),
            'doc_table': self.fun.get_element_property(main_window, self.loc.DOC_TABLE2, "Value"),
            'regimen_table_con': self.fun.get_element_property(main_window, self.loc.REGIMEN_TABLE1, "Value"),
            'regimen_table_bul': self.fun.get_element_property(main_window, self.loc.REGIMEN_TABLE2, "Value"),

            'telex_table': self.fun.get_element_property(main_window, self.loc.TELEX_TABLE2, "Value"),

        })
        self.fun.click_element(main_window, self.loc.TELEX_TABLE2, timeout=1)
        keyboard.send_keys('{RIGHT}' * 19)
        time.sleep(2)

        self.fun.click_element(main_window, self.loc.DATA_TO_TABLE1)
        keyboard.send_keys('28')

        self.fun.click_element(main_window, self.loc.DATA_TO_TABLE2, timeout=1)
        keyboard.send_keys('29')

        self.fun.click_element(main_window, self.loc.CAR_TABLE2,timeout=1)
        keyboard.send_keys("о111оо 78rus")

        self.fun.click_element(main_window, self.loc.ADDRESS_TABLE2, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(main_window, self.loc.ADDRESS_TABLE2, timeout=1)
        self.fun.click_element(main_window, self.loc.CUSTOMER_ITEM, timeout=1)

        self.fun.click_element(main_window, self.loc.DRIVER_TABLE2, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(main_window, self.loc.DRIVER_TABLE2, timeout=1)
        self.fun.click_element(main_window, self.loc.NAME_LINE2, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=1)

        time.sleep(2)

        self.fun.order_data.update({
            'data_to_table_con': self.fun.get_element_property(main_window, self.loc.DATA_TO_TABLE1, "Value"),
            'data_to_table_bul': self.fun.get_element_property(main_window, self.loc.DATA_TO_TABLE2, "Value"),
            'car_table': self.fun.get_element_property(main_window, self.loc.CAR_TABLE2, "Value"),
            'address_table': self.fun.get_element_property(main_window, self.loc.ADDRESS_TABLE2, "Value"),
            'driver_table': self.fun.get_element_property(main_window, self.loc.DRIVER_TABLE2, "Value"),
        })

        self.fun.click_element(main_window, self.loc.DRIVER_TABLE2, timeout=1)
        keyboard.send_keys('{RIGHT}' * 11)
        time.sleep(2)

        self.fun.click_element(main_window, self.loc.DELIVERY_DATE_PLAN_TABLE2, timeout=1)
        keyboard.send_keys('30')
        self.fun.click_element(main_window, self.loc.GTD_NUMBER_TABLE1, timeout=1)
        keyboard.send_keys('112233')
        self.fun.click_element(main_window, self.loc.GTD_NUMBER_TABLE2, timeout=1)
        keyboard.send_keys('4455666')
        self.fun.click_element(main_window, self.loc.NOTE_TE_TABLE1, timeout=1)
        keyboard.send_keys('Всё привезли')
        self.fun.click_element(main_window, self.loc.NOTE_TE_TABLE2,  timeout=1)
        keyboard.send_keys('НЕ всё привезли')
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=1)
        time.sleep(2)

        self.fun.order_data.update({
            'delivery_data_plan_table': self.fun.get_element_property(main_window, self.loc.DELIVERY_DATE_PLAN_TABLE2, "Value"),
            'gtd_number_table_con': self.fun.get_element_property(main_window, self.loc.GTD_NUMBER_TABLE1, "Value"),
            'gtd_number_table_bul': self.fun.get_element_property(main_window, self.loc.GTD_NUMBER_TABLE2, "Value"),
            'note_table_con': self.fun.get_element_property(main_window, self.loc.NOTE_TE_TABLE1, "Value"),
            'note_table_bul': self.fun.get_element_property(main_window, self.loc.NOTE_TE_TABLE2, "Value"),
        })

        # Открываем заказ
        self.fun.click_element_sp(main_window, self.loc.SEA_TAB_ORDER_NUMBER)

        # 12. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 6. Перейти во вкладку
        self.fun.click_element(main_window, self.loc.TAB_FREIGHT, timeout=2)

        # 5. Открыть груз bulkership
        self.fun.click_element_double(main_window, self.loc.FREIGHT_ITEM, timeout=5)

        # 5. Переключение на форму bulkership
        main_window = self.fun.get_freight_form()
        main_window.set_focus()
        time.sleep(1)

        # 5. Проверка полей bulkership
        self.fun.order_data.update({
            'bul_unloading_mod2': self.fun.get_element_property(main_window, self.loc.UNLOADING, "Value"),
            'bul_seal_num_mod2': self.fun.get_element_property(main_window, self.loc.FREIGHT_NUMBER_SEAL_FORM, "Value"),
            'bul_do_mod2': self.fun.get_element_property(main_window, self.loc.FORWARDING_RECEIVING_DO, "Value"),
            'bul_regime_to_mod2': self.fun.get_element_property(main_window, self.loc.FREIGHT_MODE_TO_FORM, "Value"),
            'bul_data_to_mod2': self.fun.get_element_property(main_window, self.loc.FREIGHT_DATA_TO_FORM, "Value"),
            'bul_note_mod2': self.fun.get_element_property(main_window, self.loc.NOTE_CONTAINER, "Value"),
            'bul_gtd_mod2': self.fun.get_element_property(main_window, self.loc.FREIGHT_NUMBER_GTD_FORM, "Value"),
        })

        # 5 Закрыть bulkership
        self.fun.click_element(main_window, self.loc.SAVE_BUTTON, timeout=1)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 5. Открыть Container
        self.fun.click_element_double_sp(main_window, self.loc.FREIGHT_ITEM2)

        # 5. Переключение на форму Container
        main_window = self.fun.get_freight_form()
        main_window.set_focus()
        time.sleep(2)

        # 5. Проверка полей Container
        self.fun.order_data.update({
            'con_unloading_mod2': self.fun.get_element_property_sp(main_window, self.loc.UNLOADING, "Value"),
            'con_seal_num_mod2': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_NUMBER_SEAL_FORM, "Value"),
            'con_do_mod2': self.fun.get_element_property_sp(main_window, self.loc.FORWARDING_RECEIVING_DO, "Value"),
            'con_regime_to_mod2': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_MODE_TO_FORM, "Value"),
            'con_data_to_mod2': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_DATA_TO_FORM, "Value"),
            'con_note_mod2': self.fun.get_element_property_sp(main_window, self.loc.NOTE_CONTAINER, "Value"),
            'con_gtd_mod2': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_NUMBER_GTD_FORM_CONTAINER, "Value"),
        })

        # 5 Закрыть Container
        self.fun.click_element(main_window, self.loc.SAVE_BUTTON, timeout=1)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        order_form = self.fun.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)

        # 7. Перейти во вкладку Перевозок
        self.fun.click_element(main_window, self.loc.TAB_TRANSPORTATION, timeout=5)

        # 8. Открыть морскую перевозку
        self.fun.click_element_double_sp(main_window, self.loc.TRANSPORTATION_ITEM)

        # 9. Переключится на форму морской перевозки
        main_window = self.fun.get_sea_form()
        main_window.set_focus()
        time.sleep(1)

        self.fun.click_element(main_window, self.loc.TAB_ROUTES, timeout=1)
        self.fun.order_data.update({
            'sea_terminal_mod2': self.fun.get_element_property_sp(main_window, self.loc.TERMINAL_LINE3, "Value"),
            'sea_port_mod2': self.fun.get_element_property_sp(main_window, self.loc.PORT3, "Value"),
            'sea_plan_arrival_mod2': self.fun.get_element_property_sp(main_window, self.loc.PLAN_ARRIVAL3, "Value"),
            'sea_fact_arrival_mod2': self.fun.get_element_property_sp(main_window, self.loc.FACT_ARRIVAL3, "Value"),
        })

        # Закрываем морскую перевозку
        self.fun.click_element(main_window, self.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 8. Открыть автоперевозку
        self.fun.click_element_double_sp(main_window, self.loc.TRANSPORTATION_ITEM2)

        # 5. Переключится на форму автоперевозки
        main_window = self.fun.get_auto_form()
        main_window.set_focus()
        time.sleep(1)

        self.fun.click_element(main_window, self.loc.TAB_ROUTES, timeout=1)

        # 16. Проверка введенных данных
        self.fun.order_data.update({
            'auto_status_mod2': self.fun.get_element_property_sp(main_window, self.loc.STATUS_COMBO, "Value"),
            'auto_address_mod2': self.fun.get_element_property_sp(main_window, self.loc.ADDRESS2, "Value"),
            'auto_plan_data_mod2': self.fun.get_element_property_sp(main_window, self.loc.PLAN_ARRIVAL2, "Value"),
            'auto_driver_mod2': self.fun.get_element_property_sp(main_window, self.loc.DRIVER, "Value"),
            'auto_number_auto_mod2': self.fun.get_element_property_sp(main_window, self.loc.AUTO, "Value"),
        })

        # Закрываем автоперевозку
        self.fun.click_element(main_window, self.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 7. Перейти во вкладку Экспедирование
        self.fun.click_element(main_window, self.loc.TAB_FORWARDING, timeout=3)

        # 8. Открыть Экспедирование
        self.fun.click_element_double_sp(main_window, self.loc.RECIPIENT_1)

        # 9. Переключится на форму Экспедирования
        main_window = self.fun.get_forwarding_form()
        main_window.set_focus()
        time.sleep(1)

        # 16. Проверка введенных данных
        self.fun.order_data.update({
            'forwarding_otv_mod2': self.fun.get_element_property(main_window, self.loc.RESPONSIBLE_COMBO, "Value"),
            'forwarding_telex_mod2': self.fun.get_element_property(main_window, self.loc.FORWARDING_TELEX, "Value"),
            'forwarding_receiving_doc_mod2': self.fun.get_element_property(main_window, self.loc.FORWARDING_RECEIVING_DOC, "Value"),

        })

        return self.fun.order_data

    def close(self):
        """Завершение работы приложения"""
        self.app.kill(soft=True)
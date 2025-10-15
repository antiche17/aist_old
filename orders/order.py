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

    def create_order(self):
        # 1. Запуск приложения
        self.fun.start_application()
        # startup_window.set_focus()

        # 2. Нажатие кнопки Запуск
        # self.fun.fun.click_element(startup_window, self.fun.loc.AIST_EF, timeout=1)
        # self.fun.fun.click_element(startup_window, self.fun.loc.START_BUTTON, timeout=1)
        time.sleep(2)

        # 3. Переход в раздел Заказы
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(4)

        self.fun.click_element(main_window, self.fun.loc.ORDERS_TAB, timeout=3)
        time.sleep(5)

        # 4. Создание нового заказа
        self.fun.click_element_sp(main_window, self.fun.loc.ADD_BUTTON)
        time.sleep(1)

        # 5. Заполнение формы заказа
        self.fun.click_element_sp(main_window, self.fun.loc.ORDER_TYPE_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.LOGISTICS_ITEM)
        self.fun.click_element_sp(main_window, self.fun.loc.CUSTOMER_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.CUSTOMER_ITEM)
        time.sleep(1)

        # 6. Взять значения для проверок
        self.fun.order_data = {
            'order_dialog_type': self.fun.get_element_property_sp(main_window, self.fun.loc.ORDER_TYPE_COMBO, "Value"),
            'order_dialog_client': self.fun.get_element_property_sp(main_window, self.fun.loc.CUSTOMER_COMBO, "Value"),
            'order_dialog_otv': self.fun.get_element_property_sp(main_window, self.fun.loc.RESPONSIBLE_COMBO, "Value"),
        }
        self.fun.click_element_sp(main_window, self.fun.loc.OK_BUTTON)
        time.sleep(3)

        # 7. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 8. Получение данных из формы заказа
        self.fun.order_data.update({
            'order_number': self.fun.get_element_property(main_window, self.fun.loc.ORDER_NUMBER, "Value"),
            'order_type': self.fun.get_element_property(main_window, self.fun.loc.ORDER_TYPE_TEXT, "Name"),
            'order_status': self.fun.get_element_property(main_window, self.fun.loc.STATUS_COMBO, "Value"),
            'order_priority': self.fun.get_element_property(main_window, self.fun.loc.PRIORITY_COMBO, "Value"),
            'order_otv': self.fun.get_element_property(main_window, self.fun.loc.RESPONSIBLE_COMBO, "Value"),

            'order_client': self.fun.get_element_property(main_window, self.fun.loc.CLIENT_COMBO, "Value"),
            'order_senders': self.fun.get_element_property(main_window, self.fun.loc.SENDERS_1, "Value"),
            'order_recipient': self.fun.get_element_property(main_window, self.fun.loc.RECIPIENT, "Value"),
            'order_delivery': self.fun.get_element_property(main_window, self.fun.loc.DELIVERY_CONDITION, "Value"),

            'order_create_mod': self.fun.get_element_property(main_window, self.fun.loc.MOD_DATE, "Name"),
            'order_create_date': self.fun.get_element_property(main_window, self.fun.loc.CREATE_DATE, "Name"),
            'order_completion_date': self.fun.get_element_property(main_window, self.fun.loc.COMPLETION_DATE, "Name"),
            'order_reference': self.fun.get_element_property(main_window, self.fun.loc.REFERENCE, "Value"),
            'order_note': self.fun.get_element_property(main_window, self.fun.loc.NOTE, "Value"),

            'order_tab_freight': self.fun.get_element_property(main_window, self.fun.loc.TAB_FREIGHT, "Name"),
            'order_tab_transportation': self.fun.get_element_property(main_window, self.fun.loc.TAB_TRANSPORTATION, "Name"),
            'order_tab_forwarding': self.fun.get_element_property(main_window, self.fun.loc.TAB_FORWARDING, "Name"),
            'order_tab_gtd': self.fun.get_element_property(main_window, self.fun.loc.TAB_GTD, "Name"),
            'order_tab_check': self.fun.get_element_property(main_window, self.fun.loc.TAB_CHECK, "Name"),
            'order_tab_file': self.fun.get_element_property(main_window, self.fun.loc.TAB_FILE, "Name"),
            'order_tab_services': self.fun.get_element_property(main_window, self.fun.loc.TAB_SERVICES, "Name"),
            'order_tab_tracking': self.fun.get_element_property(main_window, self.fun.loc.TAB_TRACKING, "Name"),
        })

        # 9. Сохранение заказа
        self.fun.click_element_sp(main_window, self.fun.loc.SAVE_BUTTON)
        time.sleep(1)

        # 10. Обновляем таблицу
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        self.fun.click_element_sp(main_window, self.fun.loc.REFRESH_BUTTON)

        # 110. Проверка данных в таблице
        self.fun.order_data.update({
            'table_order': self.fun.get_element_property(main_window, self.fun.loc.TABLE_ORDER_NUMBER, "Value"),
            'table_type': self.fun.get_element_property(main_window, self.fun.loc.TABLE_ORDER_TYPE, "Value"),
            'table_status': self.fun.get_element_property(main_window, self.fun.loc.TABLE_STATUS, "Value"),
            'table_priority': self.fun.get_element_property(main_window, self.fun.loc.TABLE_PRIORITY, "Value"),
            'table_creator': self.fun.get_element_property(main_window, self.fun.loc.TABLE_CREATOR, "Value"),
            'table_client': self.fun.get_element_property(main_window, self.fun.loc.TABLE_CLIENT, "Value")
        })

        # 12. Открыть заказ заказа
        self.fun.click_element_double(main_window, self.fun.loc.TABLE_ORDER_NUMBER, timeout=5)
        time.sleep(1)

        # 13. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 14. Меняем данные
        self.fun.click_element_sp(main_window, self.fun.loc.STATUS_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.STATUS_COMBO_CANCEL)
        self.fun.click_element_sp(main_window, self.fun.loc.PRIORITY_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.PRIORITY_COMBO_KRIT)

        self.fun.click_element_sp(main_window, self.fun.loc.CLIENT_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.CLIENT_COMBO_3)
        self.fun.click_element(main_window, self.fun.loc.SENDERS_1, timeout=3)
        self.fun.type_keys(main_window, self.fun.loc.SENDERS_1, timeout=3)
        self.fun.click_element(main_window, self.fun.loc.RECIPIENT, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.RECIPIENT_1, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.DELIVERY_CONDITION, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.DELIVERY_CONDITION_0, timeout=1)

        self.fun.set_text_field(main_window, self.fun.loc.REFERENCE, "Привет, мир!", timeout=1)
        self.fun.set_text_field(main_window, self.fun.loc.NOTE, "Привет, наш огромный дивный мир! 666 ", timeout=1)

        # 15. Получение данных из формы заказа
        self.fun.order_data.update({
            'order_status_up': self.fun.get_element_property_sp(main_window, self.fun.loc.STATUS_COMBO, "Value"),
            'order_priority_up': self.fun.get_element_property_sp(main_window, self.fun.loc.PRIORITY_COMBO, "Value"),

            'order_client_up': self.fun.get_element_property_sp(main_window, self.fun.loc.CLIENT_COMBO, "Value"),
            'order_senders_up': self.fun.get_element_property_sp(main_window, self.fun.loc.SENDERS_1, "Value"),
            'order_recipient_up': self.fun.get_element_property_sp(main_window, self.fun.loc.RECIPIENT, "Value"),
            'order_delivery_up': self.fun.get_element_property_sp(main_window, self.fun.loc.DELIVERY_CONDITION, "Value"),

            'order_reference_up': self.fun.get_element_property_sp(main_window, self.fun.loc.REFERENCE, "Value"),
            'order_note_up': self.fun.get_element_property_sp(main_window, self.fun.loc.NOTE, "Value"),
            'order_mod_date_up': self.fun.get_element_property_sp(main_window, self.fun.loc.MOD_DATE, "Name")
        })

        # 16. Сохранение заказа
        self.fun.click_element_sp(main_window, self.fun.loc.SAVE_BUTTON)
        time.sleep(1)

        # 17. Переход в раздел Заказы
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(4)

        # 18. Обновляем таблицу
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element(main_window, self.fun.loc.REFRESH_BUTTON, timeout=2)

        self.fun.order_data.update({
            'table_type_up': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_ORDER_TYPE, "Value"),
            'table_status_up': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_STATUS, "Value"),
            'table_priority_up': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_PRIORITY, "Value"),
            'table_client_up': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_CLIENT, "Value"),
            'table_recipient_up': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_RECIPIENT, "Value"),
            #'table_delivery_up': self.fun.get_element_property(main_window, self.fun.loc.TABLE_DELIVERY, "Value"),
            'table_note_up': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_NOTE, "Value")
        })

        # 19. Открыть заказ
        self.fun.click_element_double(main_window, self.fun.loc.TABLE_ORDER_NUMBER, timeout=5)
        time.sleep(1)

        # 20. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(3)

        # 21. Проверка сохранённых данных
        self.fun.order_data.update({
            'repeat_status': self.fun.get_element_property_sp(main_window, self.fun.loc.STATUS_COMBO, "Value"),
            'repeat_priority': self.fun.get_element_property_sp(main_window, self.fun.loc.PRIORITY_COMBO, "Value"),
            'repeat_client': self.fun.get_element_property_sp(main_window, self.fun.loc.CLIENT_COMBO, "Value"),
            'repeat_senders': self.fun.get_element_property_sp(main_window, self.fun.loc.SENDERS_1, "Value"),
            'repeat_recipient': self.fun.get_element_property_sp(main_window, self.fun.loc.RECIPIENT, "Value"),
            'repeat_delivery': self.fun.get_element_property_sp(main_window, self.fun.loc.DELIVERY_CONDITION, "Value"),
            'repeat_reference': self.fun.get_element_property_sp(main_window, self.fun.loc.REFERENCE, "Value"),
            'repeat_note': self.fun.get_element_property_sp(main_window, self.fun.loc.NOTE, "Value"),
            'repeat_order_mod_date': self.fun.get_element_property_sp(main_window, self.fun.loc.MOD_DATE, "Name")
        })

        # 16. Сохранение заказа
        self.fun.click_element(main_window, self.fun.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)

        # 17. Переход в раздел Заказы
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(4)

        # 22. Создание нового заказа Другие услуги
        self.fun.click_element_sp(main_window, self.fun.loc.ADD_BUTTON)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.fun.loc.ORDER_TYPE_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.LOGISTICS_ITEM_DR)
        self.fun.click_element_sp(main_window, self.fun.loc.CUSTOMER_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.CUSTOMER_ITEM)
        time.sleep(1)
        self.fun.order_data.update({
            'order_dialog_type_dr': self.fun.get_element_property(main_window, self.fun.loc.ORDER_TYPE_COMBO, "Value"),
            'order_dialog_client_dr': self.fun.get_element_property(main_window, self.fun.loc.CUSTOMER_COMBO, "Value"),
            'order_dialog_otv_dr': self.fun.get_element_property(main_window, self.fun.loc.RESPONSIBLE_COMBO, "Value"),
        })
        self.fun.click_element(main_window, self.fun.loc.OK_BUTTON, timeout=1)
        time.sleep(1)

        # 23. Форма заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        self.fun.order_data.update({
            'order_number_dr': self.fun.get_element_property_sp(main_window, self.fun.loc.ORDER_NUMBER, "Value"),
            'order_type_dr': self.fun.get_element_property_sp(main_window, self.fun.loc.ORDER_TYPE_TEXT, "Name"),
            'order_status_dr': self.fun.get_element_property_sp(main_window, self.fun.loc.STATUS_COMBO, "Value"),
            'order_priority_dr': self.fun.get_element_property_sp(main_window, self.fun.loc.PRIORITY_COMBO, "Value"),
            'order_otv_dr': self.fun.get_element_property_sp(main_window, self.fun.loc.RESPONSIBLE_COMBO, "Value"),
            'order_client_dr': self.fun.get_element_property_sp(main_window, self.fun.loc.CLIENT_COMBO, "Value"),
            'order_create_mod_dr': self.fun.get_element_property_sp(main_window, self.fun.loc.MOD_DATE, "Name"),
            'order_create_date_dr': self.fun.get_element_property_sp(main_window, self.fun.loc.CREATE_DATE, "Name"),
            'order_completion_date_dr': self.fun.get_element_property_sp(main_window, self.fun.loc.COMPLETION_DATE, "Name"),
            'order_reference_dr': self.fun.get_element_property_sp(main_window, self.fun.loc.REFERENCE, "Value"),
            'order_tab_check_dr': self.fun.get_element_property_sp(main_window, self.fun.loc.TAB_CHECK, "Name"),
            'order_tab_file_dr': self.fun.get_element_property_sp(main_window, self.fun.loc.TAB_FILE, "Name"),
            'order_tab_services_dr': self.fun.get_element_property_sp(main_window, self.fun.loc.TAB_SERVICES, "Name"),
            'order_note_dr': self.fun.get_element_property_sp(main_window, self.fun.loc.NOTE, "Value"),
        })

        self.fun.click_element(main_window, self.fun.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)

        # 24. Получение данных из таблицы
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(1)

        self.fun.click_element(main_window, self.fun.loc.REFRESH_BUTTON, timeout=2)
        self.fun.order_data.update({
            'table_order_dr': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_ORDER_NUMBER, "Value"),
            'table_type_dr': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_ORDER_TYPE, "Value"),
            'table_status_dr': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_STATUS, "Value"),
            'table_priority_dr': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_PRIORITY, "Value"),
            'table_creator_dr': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_CREATOR, "Value"),
            'table_date_dr': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_DATE, "Value"),
            'table_client_dr': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_CLIENT, "Value")
        })

        return self.fun.order_data

    def transportation(self):
        # 1. Запуск приложения
        self.fun.start_application()

        # 3. Переход в раздел Заказы
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(4)

        self.fun.click_element(main_window, self.fun.loc.ORDERS_TAB, timeout=3)
        time.sleep(5)

        # 4. Создание нового заказа
        self.fun.click_element(main_window, self.fun.loc.ADD_BUTTON, timeout=5)
        time.sleep(1)

        # 5. Заполнение формы заказа
        self.fun.click_element(main_window, self.fun.loc.ORDER_TYPE_COMBO, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.LOGISTICS_ITEM, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.CUSTOMER_COMBO, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.CUSTOMER_ITEM, timeout=1)
        time.sleep(1)
        self.fun.order_data = {
            'order_dialog_otv': self.fun.get_element_property(main_window, self.fun.loc.RESPONSIBLE_COMBO, "Value")
        }
        self.fun.click_element(main_window, self.fun.loc.OK_BUTTON, timeout=1)
        time.sleep(1)

        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 6. Взять номер заказа
        self.fun.order_data.update({
            'order_number': self.fun.get_element_property(main_window, self.fun.loc.ORDER_NUMBER, "Name")
        })

        # 7. Перейти во вкладку
        self.fun.click_element(main_window, self.fun.loc.TAB_TRANSPORTATION, timeout=5)

        # 8. Создать морскую перевозку
        self.fun.click_element(main_window, self.fun.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.fun.loc.TYPE_TRANSPORTATION, timeout=3)
        self.fun.click_element(main_window, self.fun.loc.SEA_TRANSPORTATION, timeout=3)
        self.fun.click_element(main_window, self.fun.loc.OK_BUTTON, timeout=1)

        # 9. Переключится на форму морской перевозки
        main_window = self.fun.get_sea_form()
        main_window.set_focus()
        time.sleep(1)

        # 10. Проверка полей
        self.fun.order_data.update({
            'sea_order_number': self.fun.get_element_property(main_window, self.fun.loc.ORDER_NUMBER, "Name"),
            'sea_type': self.fun.get_element_property(main_window, self.fun.loc.SEA_TYPE_TEXT, "Name"),
            'sea_status': self.fun.get_element_property(main_window, self.fun.loc.STATUS_COMBO, "Value"),
            'sea_priority': self.fun.get_element_property(main_window, self.fun.loc.PRIORITY_COMBO, "Value"),
            'sea_otv': self.fun.get_element_property(main_window, self.fun.loc.RESPONSIBLE_COMBO, "Value"),

            'sea_type_freight': self.fun.get_element_property(main_window, self.fun.loc.TYPE_FREIGHT, "Value"),
            'sea_class_freight': self.fun.get_element_property(main_window, self.fun.loc.CLASS_FREIGHT, "Value"),
            'sea_download_method': self.fun.get_element_property(main_window, self.fun.loc.DOWNLOAD_METHOD, "Value"),
            'sea_ref_freight': self.fun.get_element_property(main_window, self.fun.loc.REFERENCE_FREIGHT, "Value"),

            'sea_create_date': self.fun.get_element_property(main_window, self.fun.loc.CREATE_DATE, "Value"),
            'sea_mode_date': self.fun.get_element_property(main_window, self.fun.loc.MOD_DATE, "Value"),

            'sea_booking_reference': self.fun.get_element_property(main_window, self.fun.loc.BOOKING_REFERENCE, "Value"),
            'sea_ocean_line': self.fun.get_element_property(main_window, self.fun.loc.OCEAN_LINE, "Value"),
            'sea_ocean_konos': self.fun.get_element_property(main_window, self.fun.loc.OCEAN_KONOS, "Value"),
            'sea_feeder_line': self.fun.get_element_property(main_window, self.fun.loc.FEEDER_LINE, "Value"),
            'sea_feeder_konos': self.fun.get_element_property(main_window, self.fun.loc.FEEDER_KONOS, "Value"),
        })

        # Закрываем морскую перевозку
        self.fun.click_element(main_window, self.fun.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # Во вкладке Перевозки, таблица
        self.fun.order_data.update({
            'sea_order_table': self.fun.get_element_property(main_window, self.fun.loc.TRANSPORTATION_ITEM, "Value")
        })

        # Удаляем морскую перевозку
        self.fun.click_element(main_window, self.fun.loc.LINE_TRANSPORTATION, timeout=2)
        self.fun.click_element(main_window, self.fun.loc.DEL_BUTTON, timeout=2)
        self.fun.click_element(main_window, self.fun.loc.YES_BUTTON, timeout=2)
        self.fun.click_element(main_window, self.fun.loc.REFRESH_BUTTON_ORDER, timeout=2)
        self.fun.order_data.update({
            'del_sea': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # Создаем автоперевозку
        self.fun.click_element(main_window, self.fun.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.fun.loc.TYPE_TRANSPORTATION, timeout=3)
        self.fun.click_element(main_window, self.fun.loc.AUTO_TRANSPORTATION, timeout=3)
        keyboard.send_keys('{ENTER}')  # нажать на ОК работает если есть фокус на кнопке, могут быть проблемы

        # 5. Переключится на форму автоперевозки
        main_window = self.fun.get_auto_form()
        main_window.set_focus()
        time.sleep(1)

        # 5. Проверка полей
        self.fun.order_data.update({
            'auto_order_number': self.fun.get_element_property(main_window, self.fun.loc.AUTO_NAME_TRANSPORTATION, "Name"),
            'auto_type': self.fun.get_element_property(main_window, self.fun.loc.AUTO_TYPE_TEXT, "Name"),
            'auto_status': self.fun.get_element_property(main_window, self.fun.loc.STATUS_COMBO, "Value"),
            'auto_priority': self.fun.get_element_property(main_window, self.fun.loc.PRIORITY_COMBO, "Value"),
            'auto_otv': self.fun.get_element_property(main_window, self.fun.loc.RESPONSIBLE_COMBO, "Value"),

            'auto_create_date': self.fun.get_element_property(main_window, self.fun.loc.CREATE_DATE, "Value"),
            'auto_mode_date': self.fun.get_element_property(main_window, self.fun.loc.MOD_DATE, "Value"),

            'auto_type_freight': self.fun.get_element_property(main_window, self.fun.loc.TYPE_FREIGHT, "Value"),
            'auto_class_freight': self.fun.get_element_property(main_window, self.fun.loc.CLASS_FREIGHT_AUTO, "Value"),
            'auto_download_method': self.fun.get_element_property(main_window, self.fun.loc.DOWNLOAD_METHOD_AUTO, "Value"),
            'auto_ref_freight': self.fun.get_element_property(main_window, self.fun.loc.REFERENCE_FREIGHT, "Value"),

            'auto_carrier': self.fun.get_element_property(main_window, self.fun.loc.AUTO_CARRIER, "Value"),
            'auto_cmr': self.fun.get_element_property(main_window, self.fun.loc.AUTO_CMR, "Value"),
            'auto_cmr_por': self.fun.get_element_property(main_window, self.fun.loc.AUTO_CMR_POR, "Value"),
        })

        # Закрываем морскую перевозку
        self.fun.click_element(main_window, self.fun.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # Во вкладке Перевозки, таблица
        self.fun.order_data.update({
            'auto_order_table': self.fun.get_element_property(main_window, self.fun.loc.TRANSPORTATION_ITEM, "Value")
        })
        # Удаляем автоперевозку
        self.fun.click_element(main_window, self.fun.loc.LINE_TRANSPORTATION, timeout=2)
        self.fun.click_element(main_window, self.fun.loc.DEL_BUTTON, timeout=2)
        self.fun.click_element(main_window, self.fun.loc.YES_BUTTON, timeout=2)
        self.fun.click_element(main_window, self.fun.loc.REFRESH_BUTTON_ORDER, timeout=2)
        self.fun.order_data.update({
            'del_auto': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })
        return self.fun.order_data

    def freight_bulkership(self):
        # 1. Запуск приложения
        self.fun.start_application()
        # startup_window.set_focus()

        # 2. Нажатие кнопки Запуск
        # self.fun.fun.click_element(startup_window, self.fun.loc.AIST_EF, timeout=1)
        # self.fun.fun.click_element(startup_window, self.fun.loc.START_BUTTON, timeout=1)
        time.sleep(2)

        # 3. Переход в раздел Заказы
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(4)
        self.fun.click_element(main_window, self.fun.loc.ORDERS_TAB, timeout=3)
        time.sleep(5)

        # 4. Создание нового заказа
        self.fun.click_element(main_window, self.fun.loc.ADD_BUTTON, timeout=5)
        time.sleep(1)

        # 5. Заполнение формы заказа
        self.fun.click_element(main_window, self.fun.loc.ORDER_TYPE_COMBO, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.LOGISTICS_ITEM, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.CUSTOMER_COMBO, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.CUSTOMER_ITEM, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.OK_BUTTON, timeout=1)
        time.sleep(1)

        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 6. Перейти во вкладку
        self.fun.click_element(main_window, self.fun.loc.TAB_FREIGHT, timeout=2)

        # 7 Создать Bulkership
        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_CREATE_TE)
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_CREATE_TE1)
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_CREATE_TYPE)
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_CREATE_TYPE1)
        self.fun.set_text_field(main_window, self.fun.loc.FREIGHT_CREATE_QUANTITY, 1, timeout=1)
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_CREATE_UOM)
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_CREATE_UOM1)
        time.sleep(1)
        # 8 Взять данные
        self.fun.order_data = {
            'order_dialog_te': self.fun.get_element_property_sp(main_window, self.fun.loc.FREIGHT_CREATE_TE, "Value"),
            'order_dialog_type': self.fun.get_element_property_sp(main_window, self.fun.loc.FREIGHT_CREATE_TYPE, "Value"),
            'order_dialog_quantity': self.fun.get_element_property_sp(main_window, self.fun.loc.FREIGHT_CREATE_QUANTITY, "Value"),
            'order_dialog_uom': self.fun.get_element_property_sp(main_window, self.fun.loc.FREIGHT_CREATE_UOM, "Value"),
            'order_dialog_number': self.fun.get_element_property_sp(main_window, self.fun.loc.FREIGHT_CREATE_ORDER, "Value"),
        }
        self.fun.click_element_sp(main_window, self.fun.loc.OK_BUTTON)
        time.sleep(1)

        # Во вкладке Перевозки, таблица
        self.fun.order_data.update({
            'order_table_te': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_ITEM, "Value"),
            'order_table_type': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TABLE_TYPE_TE, "Value"),
            'order_table_number': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TABLE_NUMBER_TE, "Value")
        })

        # 5. Открыть груз заказа
        self.fun.click_element_double(main_window, self.fun.loc.FREIGHT_ITEM, timeout=5)

        # 5. Переключение на форму груза
        main_window = self.fun.get_freight_form()
        main_window.set_focus()
        time.sleep(1)

        # 5. Проверка полей
        self.fun.order_data.update({
            'freight_te': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TYPE_FORM, "Name"),
            'freight_number': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TE_NUMBER_FORM, "Value"),
            'freight_te_type': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TE_TYPE, "Value"),
            'freight_quantity': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TE_QUANTITY_FORM, "Value"),
            'freight_oum': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TE_UOM, "Value"),
            'freight_net': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_NET_WEIGHT_FORM, "Name"),
            'freight_gross': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_GROSS_WEIGHT_FORM, "Name"),

            'freight_unloading': self.fun.get_element_property(main_window, self.fun.loc.UNLOADING, "Value"),
            'freight_seal_number': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_NUMBER_SEAL_FORM, "Value"),
            'freight_number_gtd': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_NUMBER_GTD_FORM, "Value"),
            'freight_mode_to': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_MODE_TO_FORM, "Value"),
            'freight_do': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_RECEIVING_DO, "Value"),
            'freight_data_to': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_DATA_TO_FORM, "Value"),

            'freight_tab_info': self.fun.get_element_property(main_window, self.fun.loc.TAB_INFO, "Name"),
            'freight_tab_goods': self.fun.get_element_property(main_window, self.fun.loc.TAB_FREIGHT_GOODS, "Name"),
            'freight_tab_file': self.fun.get_element_property(main_window, self.fun.loc.TAB_FILE, "Name"),
            'freight_tab_tracking': self.fun.get_element_property(main_window, self.fun.loc.TAB_TRACKING, "Name"),

            'freight_data_create': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_CREATE_FORM, "Value"),
            'freight_data_mod': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_MOD_FORM, "Value"),
            'freight_note': self.fun.get_element_property(main_window, self.fun.loc.NOTE_CONTAINER, "Value")
        })

        # 5 Редактирование формы груза
        self.fun.set_text_field(main_window, self.fun.loc.FREIGHT_TE_NUMBER_FORM, "1234567", timeout=1)
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_TE_TYPE)
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_LINE_7)
        self.fun.set_text_field(main_window, self.fun.loc.FREIGHT_TE_QUANTITY_FORM, "77", timeout=1)
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_TE_UOM)
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_LINE_3)

        self.fun.click_element_sp(main_window, self.fun.loc.UNLOADING)
        keyboard.send_keys('1')
        self.fun.set_text_field(main_window, self.fun.loc.FREIGHT_NUMBER_SEAL_FORM, "12345678", timeout=1)
        self.fun.set_text_field(main_window, self.fun.loc.FREIGHT_NUMBER_GTD_FORM, "23456789", timeout=1)
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_MODE_TO_FORM)
        self.fun.click_element_sp(main_window, self.fun.loc.DELIVERY_CONDITION_0)
        self.fun.click_element_sp(main_window, self.fun.loc.FORWARDING_RECEIVING_DO)
        keyboard.send_keys('2')
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_DATA_TO_FORM)
        keyboard.send_keys('3')
        self.fun.set_text_field(main_window, self.fun.loc.NOTE_CONTAINER, "MSMU 2222222 + СААU 333333  2х20 ставка перевоза по 7 000р/щт", timeout=1)

        # 5. Проверка полей
        self.fun.order_data.update({
            'freight_number_up': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TE_NUMBER_FORM, "Value"),
            'freight_te_type_up': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TE_TYPE, "Value"),
            'freight_quantity_up': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TE_QUANTITY_FORM, "Value"),
            'freight_oum_up': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TE_UOM, "Value"),

            'freight_unloading_up': self.fun.get_element_property(main_window, self.fun.loc.UNLOADING, "Value"),
            'freight_seal_number_up': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_NUMBER_SEAL_FORM, "Value"),
            'freight_number_gtd_up': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_NUMBER_GTD_FORM, "Value"),
            'freight_mode_to_up': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_MODE_TO_FORM, "Value"),
            'freight_do_up': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_RECEIVING_DO, "Value"),
            'freight_data_to_up': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_DATA_TO_FORM, "Value"),

            'freight_note_up': self.fun.get_element_property(main_window, self.fun.loc.NOTE_CONTAINER, "Value")
        })

        # 5 Закрыть груз
        self.fun.click_element(main_window, self.fun.loc.SAVE_BUTTON, timeout=1)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 5. Открыть груз заказа
        self.fun.click_element_double(main_window, self.fun.loc.FREIGHT_ITEM, timeout=5)

        # 5. Переключение на форму груза
        main_window = self.fun.get_freight_form()
        main_window.set_focus()
        time.sleep(1)

        # 5. Проверка полей
        self.fun.order_data.update({
            'freight_number_save': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TE_NUMBER_FORM, "Value"),
            'freight_te_type_save': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TE_TYPE, "Value"),
            'freight_quantity_save': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TE_QUANTITY_FORM, "Value"),
            'freight_oum_save': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TE_UOM, "Value"),

            'freight_unloading_save': self.fun.get_element_property(main_window, self.fun.loc.UNLOADING, "Value"),
            'freight_seal_number_save': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_NUMBER_SEAL_FORM, "Value"),
            'freight_number_gtd_save': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_NUMBER_GTD_FORM, "Value"),
            'freight_mode_to_save': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_MODE_TO_FORM, "Value"),
            'freight_do_save': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_RECEIVING_DO, "Value"),
            'freight_data_to_save': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_DATA_TO_FORM, "Value"),

            'freight_data_create_save': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_CREATE_FORM, "Value"),
            'freight_data_mod_save': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_MOD_FORM, "Value"),
            'freight_note_save': self.fun.get_element_property(main_window, self.fun.loc.NOTE_CONTAINER, "Value")
        })

        # 5 Закрыть груз
        self.fun.click_element(main_window, self.fun.loc.SAVE_BUTTON, timeout=1)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()


        # 5. Удалить Bulkership
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_ITEM)
        self.fun.click_element_sp(main_window, self.fun.loc.DEL_BUTTON)
        self.fun.click_element_sp(main_window, self.fun.loc.YES_BUTTON)
        self.fun.click_element_sp(main_window, self.fun.loc.REFRESH_BUTTON_ORDER)

        self.fun.order_data.update({
            'freight_del_table': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TOTAL_RECORDS, "Value")
        })

        return self.fun.order_data

    def freight_container(self):
        # 1. Запуск приложения
        self.fun.start_application()
        # startup_window.set_focus()

        # 2. Нажатие кнопки Запуск
        # self.fun.fun.click_element(startup_window, self.fun.loc.AIST_EF, timeout=1)
        # self.fun.fun.click_element(startup_window, self.fun.loc.START_BUTTON, timeout=1)
        time.sleep(2)

        # 3. Переход в раздел Заказы
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(4)
        self.fun.click_element(main_window, self.fun.loc.ORDERS_TAB, timeout=3)
        time.sleep(5)

        # 4. Создание нового заказа
        self.fun.click_element(main_window, self.fun.loc.ADD_BUTTON, timeout=5)
        time.sleep(1)

        # 5. Заполнение формы заказа
        self.fun.click_element(main_window, self.fun.loc.ORDER_TYPE_COMBO, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.LOGISTICS_ITEM, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.CUSTOMER_COMBO, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.CUSTOMER_ITEM, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.OK_BUTTON, timeout=1)
        time.sleep(1)

        main_window = self.fun.get_main_form()
        main_window.set_focus()

        # 6. Перейти во вкладку
        self.fun.click_element(main_window, self.fun.loc.TAB_FREIGHT, timeout=1)

        # 7 Создать Container
        self.fun.click_element(main_window, self.fun.loc.CREATE_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.FREIGHT_CREATE_TE, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.FREIGHT_CREATE_TE2, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.FREIGHT_CREATE_TYPE, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.FREIGHT_CREATE_TYPE1, timeout=1)
        self.fun.set_text_field(main_window, self.fun.loc.FREIGHT_CREATE_QUANTITY, 1, timeout=1)
        self.fun.click_element_sp(main_window, self.fun.loc.APPLY_BUTTON1)
        time.sleep(1)

        # 8 Взять данные
        self.fun.order_data = {
            'order_dialog_te': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_CREATE_TE, "Value"),
            'order_dialog_type': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_CREATE_TYPE, "Value"),
            'order_dialog_quantity': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_CREATE_QUANTITY, "Value"),
            'order_dialog_number': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_CREATE_ORDER, "Value"),
        }
        self.fun.click_element(main_window, self.fun.loc.OK_BUTTON, timeout=1)
        time.sleep(1)

        # Во вкладке Перевозки, таблица
        self.fun.order_data.update({
            'order_table_te': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_ITEM, "Value"),
            'order_table_type': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TABLE_TYPE_TE, "Value"),
            'order_table_number': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TABLE_NUMBER_TE, "Value")
        })

        # 5. Открыть груз заказа
        self.fun.click_element_double(main_window, self.fun.loc.FREIGHT_ITEM, timeout=5)

        # 5. Переключение на форму груза
        main_window = self.fun.get_freight_form()
        main_window.set_focus()
        time.sleep(1)

        # 5. Проверка полей
        self.fun.order_data.update({
            'freight_te': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TYPE_FORM, "Name"),
            'freight_number': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TE_NUMBER_FORM, "Value"),
            'freight_te_type': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TE_TYPE, "Value"),
            'freight_net': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_NET_WEIGHT_FORM, "Name"),
            'freight_gross': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_GROSS_WEIGHT_FORM, "Name"),

            'freight_unloading': self.fun.get_element_property(main_window, self.fun.loc.UNLOADING, "Value"),
            'freight_seal_number': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_NUMBER_SEAL_FORM, "Value"),
            'freight_number_gtd': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_NUMBER_GTD_FORM_CONTAINER, "Value"),
            'freight_mode_to': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_MODE_TO_FORM, "Value"),
            'freight_do': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_RECEIVING_DO, "Value"),
            'freight_data_to': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_DATA_TO_FORM, "Value"),

            'freight_tab_info': self.fun.get_element_property(main_window, self.fun.loc.TAB_INFO, "Name"),
            'freight_tab_goods': self.fun.get_element_property(main_window, self.fun.loc.TAB_FREIGHT_GOODS, "Name"),
            'freight_tab_file': self.fun.get_element_property(main_window, self.fun.loc.TAB_FILE, "Name"),
            'freight_tab_tracking': self.fun.get_element_property(main_window, self.fun.loc.TAB_TRACKING, "Name"),

            'freight_data_create': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_CREATE_FORM, "Value"),
            'freight_data_mod': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_MOD_FORM, "Value"),
            'freight_note': self.fun.get_element_property(main_window, self.fun.loc.NOTE_CONTAINER, "Value")
        })

        # 5 Редактирование формы груза
        self.fun.set_text_field(main_window, self.fun.loc.FREIGHT_TE_NUMBER_FORM, "TARE1234567", timeout=1)
        self.fun.click_element(main_window, self.fun.loc.FREIGHT_TE_TYPE, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.FREIGHT_LINE_7, timeout=1)

        self.fun.click_element(main_window, self.fun.loc.UNLOADING, timeout=1)
        keyboard.send_keys('1')
        self.fun.set_text_field(main_window, self.fun.loc.FREIGHT_NUMBER_SEAL_FORM, "12345678", timeout=1)
        self.fun.set_text_field(main_window, self.fun.loc.FREIGHT_NUMBER_GTD_FORM_CONTAINER, "23456789", timeout=1)
        self.fun.click_element(main_window, self.fun.loc.FREIGHT_MODE_TO_FORM, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.DELIVERY_CONDITION_0, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.FORWARDING_RECEIVING_DO, timeout=1)
        keyboard.send_keys('2')
        self.fun.click_element(main_window, self.fun.loc.FREIGHT_DATA_TO_FORM, timeout=1)
        keyboard.send_keys('3')
        self.fun.set_text_field(main_window, self.fun.loc.NOTE_CONTAINER, "MSMU 2222222 + СААU 333333  2х20 ставка перевоза по 7 000р/щт", timeout=1)
        self.fun.click_element_sp(main_window, self.fun.loc.APPLY_BUTTON1)
        time.sleep(1)
        # 5. Проверка полей
        self.fun.order_data.update({
            'freight_number_up': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TE_NUMBER_FORM, "Value"),
            'freight_te_type_up': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TE_TYPE, "Value"),

            'freight_unloading_up': self.fun.get_element_property(main_window, self.fun.loc.UNLOADING, "Value"),
            'freight_seal_number_up': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_NUMBER_SEAL_FORM, "Value"),
            'freight_number_gtd_up': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_NUMBER_GTD_FORM_CONTAINER, "Value"),
            'freight_mode_to_up': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_MODE_TO_FORM, "Value"),
            'freight_do_up': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_RECEIVING_DO, "Value"),
            'freight_data_to_up': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_DATA_TO_FORM, "Value"),

            'freight_note_up': self.fun.get_element_property(main_window, self.fun.loc.NOTE_CONTAINER, "Value")
        })

        # 5 Закрыть груз
        self.fun.click_element(main_window, self.fun.loc.SAVE_BUTTON, timeout=1)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 5. Открыть груз заказа
        self.fun.click_element_double(main_window, self.fun.loc.FREIGHT_ITEM, timeout=5)

        # 5. Переключение на форму груза
        main_window = self.fun.get_freight_form()
        main_window.set_focus()
        time.sleep(1)

        # 5. Проверка полей
        self.fun.order_data.update({
            'freight_number_save': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TE_NUMBER_FORM, "Value"),
            'freight_te_type_save': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TE_TYPE, "Value"),

            'freight_unloading_save': self.fun.get_element_property(main_window, self.fun.loc.UNLOADING, "Value"),
            'freight_seal_number_save': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_NUMBER_SEAL_FORM, "Value"),
            'freight_number_gtd_save': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_NUMBER_GTD_FORM_CONTAINER, "Value"),
            'freight_mode_to_save': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_MODE_TO_FORM, "Value"),
            'freight_do_save': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_RECEIVING_DO, "Value"),
            'freight_data_to_save': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_DATA_TO_FORM, "Value"),

            'freight_data_create_save': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_CREATE_FORM, "Value"),
            'freight_data_mod_save': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_MOD_FORM, "Value"),
            'freight_note_save': self.fun.get_element_property(main_window, self.fun.loc.NOTE_CONTAINER, "Value")
        })

        # 5 Закрыть груз
        self.fun.click_element(main_window, self.fun.loc.SAVE_BUTTON, timeout=1)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()

        # 5. Удалить Container
        self.fun.click_element(main_window, self.fun.loc.LINE_TRANSPORTATION, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.DEL_BUTTON, timeout=2)
        self.fun.click_element(main_window, self.fun.loc.YES_BUTTON, timeout=2)
        self.fun.click_element(main_window, self.fun.loc.REFRESH_BUTTON_ORDER, timeout=2)

        self.fun.order_data.update({
            'freight_del_table': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TOTAL_RECORDS, "Value")
        })

        return self.fun.order_data

    def forwarding(self):
        # 1. Запуск приложения
        self.fun.start_application()
        # startup_window.set_focus()

        # 2. Нажатие кнопки Запуск
        # self.fun.fun.click_element(startup_window, self.fun.loc.AIST_EF, timeout=1)
        # self.fun.fun.click_element(startup_window, self.fun.loc.START_BUTTON, timeout=1)
        time.sleep(2)

        # 3. Переход в раздел Заказы
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(4)

        self.fun.click_element(main_window, self.fun.loc.ORDERS_TAB, timeout=3)
        time.sleep(5)

        # 5. Создание нового заказа
        self.fun.click_element(main_window, self.fun.loc.ADD_BUTTON, timeout=5)
        time.sleep(1)

        # 6. Заполнение формы заказа
        self.fun.click_element(main_window, self.fun.loc.ORDER_TYPE_COMBO, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.LOGISTICS_ITEM, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.CUSTOMER_COMBO, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.CUSTOMER_ITEM, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.OK_BUTTON, timeout=1)
        time.sleep(2)

        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 6. Взять номер заказа
        self.fun.order_data = {
            'order_number': self.fun.get_element_property(main_window, self.fun.loc.ORDER_NUMBER, "Name")
        }

        # 7. Перейти во вкладку
        self.fun.click_element(main_window, self.fun.loc.TAB_FORWARDING, timeout=3)

        # 8. Создать Экспедирование
        self.fun.click_element(main_window, self.fun.loc.CREATE_BUTTON, timeout=1)
        self.fun.order_data.update({
            'forwarding_dialog_type': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_TYPE_DIALOG, "Value"),
            'forwarding_dialog_otv': self.fun.get_element_property(main_window, self.fun.loc.RESPONSIBLE_COMBO, "Value"),
        })

        self.fun.click_element(main_window, self.fun.loc.OK_BUTTON, timeout=1)

        # 9. Переключится на форму Экспедирования
        main_window = self.fun.get_forwarding_form()
        main_window.set_focus()
        time.sleep(1)


        # 10. Проверка полей
        self.fun.order_data.update({
            'forwarding_order_number': self.fun.get_element_property(main_window, self.fun.loc.ORDER_NUMBER, "Name"),
            'forwarding_type': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_TYPE_TEXT, "Name"),
            'forwarding_status': self.fun.get_element_property(main_window, self.fun.loc.STATUS_COMBO, "Value"),
            'forwarding_priority': self.fun.get_element_property(main_window, self.fun.loc.PRIORITY_COMBO, "Value"),
            'forwarding_otv': self.fun.get_element_property(main_window, self.fun.loc.RESPONSIBLE_COMBO, "Value"),

            'forwarding_forwarder': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_FORWARDER, "Value"),
            'forwarding_create_date': self.fun.get_element_property(main_window, self.fun.loc.CREATE_DATE, "Value"),
            'forwarding_mode_date': self.fun.get_element_property(main_window, self.fun.loc.MOD_DATE, "Value"),
            'forwarding_completion_data': self.fun.get_element_property(main_window, self.fun.loc.COMPLETION_DATE, "Value"),
            'forwarding_telex': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_TELEX, "Value"),
            'forwarding_receiving_doc': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_RECEIVING_DOC,"Value"),
            'forwarding_nomination': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_NOMINATION, "Value"),
            'forwarding_note': self.fun.get_element_property(main_window, self.fun.loc.NOTE, "Value"),

            'tab_info': self.fun.get_element_property(main_window, self.fun.loc.TAB_INFO, "Name"),
            'tab_forwarding_freight': self.fun.get_element_property(main_window, self.fun.loc.TAB_FORWARDING_FREIGHT, "Name"),
            'tab_services': self.fun.get_element_property(main_window, self.fun.loc.TAB_SERVICES, "Name"),
            'tab_file': self.fun.get_element_property(main_window, self.fun.loc.TAB_FILE, "Name"),
        })

        # 11. Закрываем морскую перевозку
        self.fun.click_element(main_window, self.fun.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)

        # 12. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 13. Открыть Экспедирование
        self.fun.click_element_double(main_window, self.fun.loc.LINE_TRANSPORTATION, timeout=1)

        # 14. Переключится на форму Экспедирование
        main_window = self.fun.get_forwarding_form()
        main_window.set_focus()
        time.sleep(1)

        # 15. Редактирование Экспедирование
        self.fun.click_element(main_window, self.fun.loc.STATUS_COMBO, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.STATUS_FINISH, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.PRIORITY_COMBO, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.PRIORITY_COMBO_LOW, timeout=1)

        self.fun.click_element(main_window, self.fun.loc.FORWARDING_FORWARDER, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.RECIPIENT_1, timeout=1)

        self.fun.click_element(main_window, self.fun.loc.FORWARDING_TELEX, timeout=1)
        time.sleep(1)
        keyboard.send_keys('1')
        self.fun.click_element(main_window, self.fun.loc.FORWARDING_RECEIVING_DOC, timeout=1)
        time.sleep(1)
        keyboard.send_keys('2')
        self.fun.click_element(main_window, self.fun.loc.FORWARDING_NOMINATION, timeout=1)
        time.sleep(1)
        keyboard.send_keys('3')
        self.fun.set_text_field(main_window, self.fun.loc.NOTE, "CAAU 111111 \n"
                                                        "MSMU 2222222 + СААU 333333  2х20 ставка перевоза по 7 000р/щт\n"
                                                        "\n"
                                                        "Иван Иванов Иванович 30.12.1985\n"
                                                        "0000 111111 МВД по Республике Дагестан от 05.07.2021 Мира 1 кв1\n"
                                                        "89888333222 SCANIA А777УЕ05 прицеп УЕ1111 05\n"
                                                        "погрузка визит 13\05 1:40 - 4:50 ;\n"
                                                        "сдача на КТСП 13/05 ", timeout=1)
        self.fun.click_element_sp(main_window, self.fun.loc.APPLY_BUTTON1)
        time.sleep(1)

        # 16. Проверка введенных данных
        self.fun.order_data.update({
            'forwarding_status_up': self.fun.get_element_property(main_window, self.fun.loc.STATUS_COMBO, "Value"),
            'forwarding_priority_up': self.fun.get_element_property(main_window, self.fun.loc.PRIORITY_COMBO, "Value"),
            'forwarding_forwarder_up': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_FORWARDER, "Value"),

            'forwarding_telex_up': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_TELEX, "Value"),
            'forwarding_receiving_doc_up': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_RECEIVING_DOC,"Value"),
            'forwarding_nomination_up': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_NOMINATION, "Value"),
            'forwarding_note_up': self.fun.get_element_property(main_window, self.fun.loc.NOTE, "Value"),
        })

        self.fun.click_element(main_window, self.fun.loc.SAVE_BUTTON, timeout=1)

        # 17. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 18. Открыть Экспедирование
        self.fun.click_element_double(main_window, self.fun.loc.LINE_TRANSPORTATION, timeout=1)

        # 14. Переключится на форму морской перевозки
        main_window = self.fun.get_forwarding_form()
        main_window.set_focus()
        time.sleep(1)

        # 19. Проверка сохраненных данных
        self.fun.order_data.update({
            'forwarding_status_save': self.fun.get_element_property(main_window, self.fun.loc.STATUS_COMBO, "Value"),
            'forwarding_priority_save': self.fun.get_element_property(main_window, self.fun.loc.PRIORITY_COMBO, "Value"),
            'forwarding_forwarder_save': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_FORWARDER, "Value"),
            'forwarding_telex_save': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_TELEX, "Value"),
            'forwarding_receiving_doc_save': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_RECEIVING_DOC,"Value"),
            'forwarding_nomination_save': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_NOMINATION,"Value"),
            'forwarding_note_save': self.fun.get_element_property(main_window, self.fun.loc.NOTE, "Value"),
        })

        # 20. Переключится на форму морской перевозки
        main_window = self.fun.get_forwarding_form()
        main_window.set_focus()
        time.sleep(1)

        self.fun.click_element(main_window, self.fun.loc.SAVE_BUTTON, timeout=1)

        # 21. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 22. Во вкладке Перевозки, таблица
        self.fun.order_data.update({
            'forwarding_type_table': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_ITEM, "Value"),
            'forwarding_order_table': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_NUMBER, "Value"),
            'forwarding_status_table': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_STATUS, "Value"),
            'forwarding_otv_table': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_OTV, "Value"),
            'forwarding_forward_table': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_FORWARD, "Value"),
            'forwarding_te_table': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_TE, "Value"),
            'forwarding_create_table': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_DATA_CREATE, "Value"),
            'forwarding_mod_table': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_DATA_FINISH, "Value"),
            'forwarding_note_table': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_NOTE, "Value")
        })

        # 23. Удаляем морскую перевозку
        self.fun.click_element(main_window, self.fun.loc.LINE_TRANSPORTATION, timeout=2)
        self.fun.click_element(main_window, self.fun.loc.DEL_BUTTON, timeout=2)
        self.fun.click_element(main_window, self.fun.loc.YES_BUTTON, timeout=2)
        self.fun.click_element(main_window, self.fun.loc.REFRESH_BUTTON_ORDER, timeout=2)

        # 23. Проверка удаление морской перевозки
        self.fun.order_data.update({
            'forwarding_panel': self.fun.get_element_property(main_window, self.fun.loc.DATA_PANEL, "Value"),
        })

        return self.fun.order_data

    def gtd(self):
        # 1. Запуск приложения
        self.fun.start_application()

        # 2. Переход в раздел Заказы
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(4)

        self.fun.click_element(main_window, self.fun.loc.ORDERS_TAB, timeout=3)
        time.sleep(5)

        # 4. Создание нового заказа
        self.fun.click_element_sp(main_window, self.fun.loc.ADD_BUTTON)
        time.sleep(1)

        # 5. Заполнение формы заказа
        self.fun.click_element_sp(main_window, self.fun.loc.ORDER_TYPE_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.LOGISTICS_ITEM)
        self.fun.click_element_sp(main_window, self.fun.loc.CUSTOMER_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.CUSTOMER_ITEM)
        time.sleep(1)

        # 6. Взять значения для проверок
        self.fun.order_data = {
            'order_dialog_client': self.fun.get_element_property_sp(main_window, self.fun.loc.CUSTOMER_COMBO, "Value"),
        }
        self.fun.click_element_sp(main_window, self.fun.loc.OK_BUTTON)
        time.sleep(3)

        # 4. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 5. Взять номер заказа
        self.fun.order_data.update({
            'order_number': self.fun.get_element_property(main_window, self.fun.loc.ORDER_NUMBER, "Name")
        })
        # 7. Перейти во вкладку

        self.fun.click_element(main_window, self.fun.loc.TAB_TRANSPORTATION, timeout=5)

        # 8. Создать морскую перевозку
        self.fun.click_element(main_window, self.fun.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.fun.loc.TYPE_TRANSPORTATION, timeout=3)
        self.fun.click_element(main_window, self.fun.loc.SEA_TRANSPORTATION, timeout=3)
        self.fun.click_element(main_window, self.fun.loc.OK_BUTTON, timeout=1)

        # 9. Переключится на форму морской перевозки
        main_window = self.fun.get_sea_form()
        main_window.set_focus()
        time.sleep(1)

        # 10. Проверка полей
        self.fun.order_data.update({
            'sea_order_number': self.fun.get_element_property(main_window, self.fun.loc.ORDER_NUMBER, "Name"),

        })

        # 10. Создать ТЕ
        self.fun.click_element_sp(main_window, self.fun.loc.TAB_FREIGHT)
        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.fun.loc.ADD_TE)
        self.fun.click_element_sp(main_window, self.fun.loc.OPEN_BUTTON)
        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.fun.loc.OK_BUTTON)

        # 8 Создать Bulkership
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_CREATE_TE, )
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_CREATE_TE1)
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_CREATE_TYPE)
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_CREATE_TYPE1)
        self.fun.set_text_field(main_window, self.fun.loc.FREIGHT_CREATE_QUANTITY, 1, timeout=1)
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_CREATE_UOM)
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_CREATE_UOM1)
        time.sleep(1)

        keyboard.send_keys('{ENTER}')
        main_window = self.fun.get_sea_form()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.fun.loc.SAVE_BUTTON)
        keyboard.send_keys('{ENTER}')


        # Закрываем морскую перевозку
        self.fun.click_element_sp(main_window, self.fun.loc.SAVE_BUTTON)
        time.sleep(1)

        # 4. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 10. Создать ГТД в заказе
        self.fun.click_element_sp(main_window, self.fun.loc.TAB_GTD)
        self.fun.click_element_sp(main_window, self.fun.loc.ADD_BUTTON)

        main_window = self.fun.get_gtd_form()
        main_window.set_focus()
        time.sleep(1)

        # 11. Проверка полей
        self.fun.order_data.update({
            'gtd_client': self.fun.get_element_property(main_window, self.fun.loc.GTD_CLIENT, "Value"),
            'gtd_order_number': self.fun.get_element_property(main_window, self.fun.loc.GTD_ORDER, "Value"),
            'gtd_number': self.fun.get_element_property(main_window, self.fun.loc.GTD_NUMBER, "Value"),
            'procedure_gtd': self.fun.get_element_property(main_window, self.fun.loc.GTD_PROCEDURE, "Value"),
            'gtd_manager': self.fun.get_element_property(main_window, self.fun.loc.GTD_MANAGER, "Value"),

            'gtd_forwarding': self.fun.get_element_property(main_window, self.fun.loc.GTD_FORWARDING, "Value"),
            'gtd_sender': self.fun.get_element_property(main_window, self.fun.loc.GTD_SENDER, "Value"),
            'gtd_plan_arrival': self.fun.get_element_property(main_window, self.fun.loc.GTD_PLAN_ARRIVAL, "Value"),
            'gtd_plan_ship': self.fun.get_element_property(main_window, self.fun.loc.GTD_PLAN_SHIP, "Value"),
            'gtd_doc': self.fun.get_element_property(main_window, self.fun.loc.GTD_DOC, "Value"),
            'gtd_post': self.fun.get_element_property(main_window, self.fun.loc.GTD_POST, "Value"),
            'gtd_svh': self.fun.get_element_property(main_window, self.fun.loc.GTD_SVH, "Value"),
            'gtd_declarant': self.fun.get_element_property(main_window, self.fun.loc.GTD_DEC, "Value"),

            'gtd_supply': self.fun.get_element_property(main_window, self.fun.loc.GTD_SUPPLY, "Value"),
            'gtd_release': self.fun.get_element_property(main_window, self.fun.loc.GTD_RELEASE, "Value"),
            'gtd_pers': self.fun.get_element_property(main_window, self.fun.loc.GTD_PERSONALS, "Value"),

            'gtd_decl_te': self.fun.get_element_property(main_window, self.fun.loc.GTD_DECl_TE, "Value"),
            'gtd_real_te': self.fun.get_element_property(main_window, self.fun.loc.GTD_REAL_TE, "Value"),
            'gtd_decl_tnved': self.fun.get_element_property(main_window, self.fun.loc.GTD_DECl_TNVED, "Value"),
            'gtd_real_tnved': self.fun.get_element_property(main_window, self.fun.loc.GTD_REAL_TNVED, "Value"),
            'gtd_brutto': self.fun.get_element_property(main_window, self.fun.loc.GTD_BRUTTO, "Value"),
            'gtd_netto': self.fun.get_element_property(main_window, self.fun.loc.GTD_NETTO, "Value"),
            'gtd_price_p': self.fun.get_element_property(main_window, self.fun.loc.GTD_PRICE_P, "Value"),
            'gtd_price_v': self.fun.get_element_property(main_window, self.fun.loc.GTD_PRICE_V, "Value"),

            'gtd_payment': self.fun.get_element_property(main_window, self.fun.loc.GTD_PAYMENT, "Value"),
            'gtd_tk': self.fun.get_element_property(main_window, self.fun.loc.GTD_TK, "Value"),
            'gtd_kts': self.fun.get_element_property(main_window, self.fun.loc.GTD_KTS, "Value"),
            'gtd_guarantee': self.fun.get_element_property(main_window, self.fun.loc.GTD_GUARANTEE, "Value"),
            'gtd_peny': self.fun.get_element_property(main_window, self.fun.loc.GTD_PENY, "Value"),

            'gtd_receiver': self.fun.get_element_property(main_window, self.fun.loc.GTD_RECEIVER, "Value"),
            'gtd_contract': self.fun.get_element_property(main_window, self.fun.loc.GTD_CONTRACT, "Value"),
            'gtd_sum': self.fun.get_element_property(main_window, self.fun.loc.GTD_SUM, "Value"),
            'gtd_note': self.fun.get_element_property(main_window, self.fun.loc.GTD_NOTE, "Value"),

            'gtd_dol': self.fun.get_element_property(main_window, self.fun.loc.GTD_DOL, "Value"),
            'gtd_evr': self.fun.get_element_property(main_window, self.fun.loc.GTD_EVR, "Value"),

        })

        # 11. Проверка, что ГТД не сохраняется без ТЕ
        self.fun.click_element_sp(main_window, self.fun.loc.OK_BUTTON1)
        self.fun.order_data.update({
            'order_te_not': self.fun.get_element_property(main_window, self.fun.loc.GTD_TE_NOT, "Name"),
        })
        self.fun.click_element_sp(main_window, self.fun.loc.OK_BUTTON)

        # 12. Создать ТЕ из ГТД
        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.fun.loc.ADD_TE)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')
        time.sleep(1)
        self.fun.order_data.update({
            'number_te': self.fun.get_element_property(main_window, self.fun.loc.GTD_TE, "Value")
        })

        # 12. Взять из К/С партии
        #self.fun.click_element_sp(main_window, self.fun.loc.GTD_KS)
        #self.fun.click_element_sp(main_window, self.fun.loc.ADD_TE)

        # 12. Редактирование формы(не все поля)
        # 12. Редактирование формы(не все поля)
        self.fun.click_element_sp(main_window, self.fun.loc.GTD_PLAN_SHIP)
        keyboard.send_keys('1')
        self.fun.click_element_sp(main_window, self.fun.loc.GTD_DEC)
        self.fun.click_element_sp(main_window, self.fun.loc.RECIPIENT_1)
        keyboard.send_keys('1')
        self.fun.click_element_sp(main_window, self.fun.loc.GTD_POST)
        time.sleep(1)
        self.fun.set_text_field(main_window, self.fun.loc.SEARCH_BOX, "В", timeout=1)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.fun.loc.RECIPIENT_1)
        time.sleep(1)


        self.fun.click_element_sp(main_window, self.fun.loc.GTD_SUPPLY)
        keyboard.send_keys('2')
        self.fun.click_element_sp(main_window, self.fun.loc.GTD_RELEASE)
        keyboard.send_keys('3')
        self.fun.click_element_sp(main_window, self.fun.loc.GTD_PERSONALS)
        keyboard.send_keys('4')

        self.fun.click_element_sp(main_window, self.fun.loc.GTD_DECl_TE)
        keyboard.send_keys('1')
        self.fun.click_element_sp(main_window, self.fun.loc.GTD_BRUTTO)
        keyboard.send_keys('100')
        self.fun.click_element_sp(main_window, self.fun.loc.GTD_PAYMENT)
        keyboard.send_keys('5')
        self.fun.click_element_sp(main_window, self.fun.loc.GTD_RECEIVER)
        self.fun.click_element_sp(main_window, self.fun.loc.RECIPIENT_1)

        self.fun.click_element_sp(main_window, self.fun.loc.GTD_CONTRACT)
        self.fun.click_element_sp(main_window, self.fun.loc.GTD_ELLIPSIS)
        self.fun.click_element_sp(main_window, self.fun.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.fun.loc.OK_BUTTON1)
        self.fun.click_element_sp(main_window, self.fun.loc.GTD_SUM)
        keyboard.send_keys('6')

        self.fun.set_text_field(main_window, self.loc.GTD_NOTE, "Примечание ГТД", timeout=1)
        self.fun.click_element_sp(main_window, self.fun.loc.APPLY_BUTTON)
        self.fun.click_element_sp(main_window, self.fun.loc.YES_BUTTON)
        time.sleep(1)
        # 11. Проверка полей
        self.fun.order_data.update({
            'gtd_number_mod': self.fun.get_element_property(main_window, self.fun.loc.GTD_NUMBER, "Value"),
            'gtd_plan_ship_mod': self.fun.get_element_property(main_window, self.fun.loc.GTD_PLAN_SHIP, "Value"),
            'gtd_post_mod': self.fun.get_element_property(main_window, self.fun.loc.GTD_POST, "Value"),
            'gtd_declarant_mod': self.fun.get_element_property(main_window, self.fun.loc.GTD_DEC, "Value"),
            'gtd_supply_mod': self.fun.get_element_property(main_window, self.fun.loc.GTD_SUPPLY, "Value"),
            'gtd_release_mod': self.fun.get_element_property(main_window, self.fun.loc.GTD_RELEASE, "Value"),
            'gtd_pers_mod': self.fun.get_element_property(main_window, self.fun.loc.GTD_PERSONALS, "Value"),
            'gtd_decl_te_mod': self.fun.get_element_property(main_window, self.fun.loc.GTD_DECl_TE, "Value"),
            'gtd_brutto_mod': self.fun.get_element_property(main_window, self.fun.loc.GTD_BRUTTO, "Value"),

            'gtd_payment_mod': self.fun.get_element_property(main_window, self.fun.loc.GTD_PAYMENT, "Value"),
            'gtd_receiver_mod': self.fun.get_element_property(main_window, self.fun.loc.GTD_RECEIVER, "Value"),
            'gtd_contract_mod': self.fun.get_element_property(main_window, self.fun.loc.GTD_CONTRACT, "Value"),
            'gtd_sum_mod': self.fun.get_element_property(main_window, self.fun.loc.GTD_SUM, "Value"),
            'gtd_note_mod': self.fun.get_element_property(main_window, self.fun.loc.GTD_NOTE, "Value"),

            'gtd_dol_mod': self.fun.get_element_property(main_window, self.fun.loc.GTD_DOL, "Value"),
            'gtd_evr_mod': self.fun.get_element_property(main_window, self.fun.loc.GTD_EVR, "Value"),

        })
        self.fun.click_element_sp(main_window, self.fun.loc.OK_BUTTON1)

        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        self.fun.click_element_sp(main_window, self.fun.loc.REFRESH_BUTTON)
        self.fun.click_element_sp(main_window, self.fun.loc.MAX_FORM)

        self.fun.order_data.update({
            'gtd_client_tab': self.fun.get_element_property(main_window, self.fun.loc.TABLE_CLIENT, "Value"),
            'gtd_decl_tab': self.fun.get_element_property(main_window, self.fun.loc.TABLE_DECL, "Value"),
            'gtd_arrival_tab': self.fun.get_element_property(main_window, self.fun.loc.TABLE_ARRIVAL, "Value"),
            'gtd_post_tab': self.fun.get_element_property(main_window, self.fun.loc.TABLE_POST, "Value"),
            'gtd_container_tab': self.fun.get_element_property(main_window, self.fun.loc.TABLE_CONTAINER, "Value"),
            'gtd_brutto_tab': self.fun.get_element_property(main_window, self.fun.loc.TABLE_BRUTTO, "Value"),
            'gtd_supply_tab': self.fun.get_element_property(main_window, self.fun.loc.TABLE_SUPPLY, "Value"),
            'gtd_contract_tab': self.fun.get_element_property(main_window, self.fun.loc.TABLE_CONTRACT, "Value"),
            'gtd_importer_tab': self.fun.get_element_property(main_window, self.fun.loc.TABLE_IMPORTER, "Value"),
            'gtd_release_tab': self.fun.get_element_property(main_window, self.fun.loc.TABLE_RELEASE_GTD, "Value"),
            'gtd_number_tab': self.fun.get_element_property(main_window, self.fun.loc.TABLE_GTD_NUMBER, "Value"),
            'gtd_created_tab': self.fun.get_element_property(main_window, self.fun.loc.TABLE_CREATED, "Value"),
            'gtd_sum_tab': self.fun.get_element_property(main_window, self.fun.loc.TABLE_INVOICE_SUM, "Value"),
            'gtd_note_tab': self.fun.get_element_property(main_window, self.fun.loc.TABLE_NOTE, "Value"),
            'gtd_payments_tab': self.fun.get_element_property(main_window, self.fun.loc.TABLE_PAYMENTS, "Value"),
            'gtd_personal_tab': self.fun.get_element_property(main_window, self.fun.loc.TABLE_PERSONAL, "Value"),
            'gtd_declarant_tab': self.fun.get_element_property(main_window, self.fun.loc.TABLE_DECLARANT, "Value")
        })

        self.fun.click_element_sp(main_window, self.fun.loc.TABLE_DELETE)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element_sp(main_window, self.fun.loc.REFRESH_BUTTON)

        self.fun.order_data.update({
            'all_status': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TOTAL_RECORDS, "Value")
        })
        time.sleep(1)

        return self.fun.order_data

    def finance(self):
        # 1. Запуск приложения
        self.fun.start_application()
        # startup_window.set_focus()

        # 2. Нажатие кнопки Запуск
        # self.fun.fun.click_element(startup_window, self.fun.loc.AIST_EF, timeout=1)
        # self.fun.fun.click_element(startup_window, self.fun.loc.START_BUTTON, timeout=1)
        time.sleep(2)

        # 3. Переход в раздел Заказы
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(3)
        self.fun.click_element(main_window, self.fun.loc.ORDERS_TAB, timeout=3)
        time.sleep(4)

        # 4. Создание нового заказа
        self.fun.click_element(main_window, self.fun.loc.ADD_BUTTON, timeout=5)
        time.sleep(1)

        # 5. Заполнение формы заказа
        self.fun.click_element(main_window, self.fun.loc.ORDER_TYPE_COMBO, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.LOGISTICS_ITEM, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.CUSTOMER_COMBO, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.CUSTOMER_ITEM, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.OK_BUTTON, timeout=1)
        time.sleep(1)

        main_window = self.fun.get_main_form()
        main_window.set_focus()

        # 6. Перейти во вкладку
        self.fun.click_element_sp(main_window, self.fun.loc.TAB_CHECK)

        self.fun.order_data.update({
            'order_client': self.fun.get_element_property(main_window, self.fun.loc.CLIENT_COMBO, "Value"),
        })

        # 7 Создать Исходящий счет и выставить покупателя
        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)
        time.sleep(1)
        self.fun.order_data.update({
            'is_create_order': self.fun.get_element_property_sp(main_window, self.fun.loc.IS_CREATE_ORDER, "Name"),
        })
        self.fun.click_element(main_window, self.fun.loc.CREATE_BUTTON, timeout=1)

        # 8. Переключение на форму ИС
        main_window = self.fun.get_check_form()
        main_window.set_focus()
        main_window = self.fun.app.window(**self.fun.loc.CHECK_FROM)
        time.sleep(1)

        # 9. Редактирование
        self.fun.click_element(main_window, self.fun.loc.IS_SUPPLIER, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.RECIPIENT_1, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.IS_LIST, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.IS_FREIGHT, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.APPLY_BUTTON, timeout=1)

        # 10. Проверка полей
        self.fun.order_data.update({
            #'is_name_form': self.fun.get_element_property(main_window, self.fun.loc.IS_NAME_FORM, "Value"),
            'is_number': self.fun.get_element_property(main_window, self.fun.loc.IS_NUMBER, "Value"),
            'is_date': self.fun.get_element_property(main_window, self.fun.loc.IS_DATE, "Value"),
            'is_list': self.fun.get_element_property(main_window, self.fun.loc.IS_LIST, "Value"),
            'is_suppler': self.fun.get_element_property(main_window, self.fun.loc.IS_SUPPLIER, "Value"),
            'is_order': self.fun.get_element_property(main_window, self.fun.loc.IS_ORDER, "Value"),
            'is_client': self.fun.get_element_property(main_window, self.fun.loc.GTD_CLIENT, "Value"),
            'is_buyer': self.fun.get_element_property(main_window, self.fun.loc.IS_BUYER, "Value"),
        })

        self.fun.click_element(main_window, self.fun.loc.OK_BUTTON1, timeout=1)

        # 11. Переключить на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()

        self.fun.click_element(main_window, self.fun.loc.REFRESH_BUTTON_ORDER, timeout=1)

        # 12. Поля в таблице
        self.fun.order_data.update({
            'is_type_table': self.fun.get_element_property(main_window, self.fun.loc.IS_TYPE_CHECK, "Value"),
            'is_number_table': self.fun.get_element_property(main_window, self.fun.loc.IS_NUMBER_TABLE, "Value"),
            'is_date_table': self.fun.get_element_property(main_window, self.fun.loc.IS_DATE_TABLE, "Value"),
            'is_suppler_table': self.fun.get_element_property(main_window, self.fun.loc.IS_SUPPLIER_TABLE, "Value"),
            'is_buyer_table': self.fun.get_element_property(main_window, self.fun.loc.IS_BUYER_TABLE, "Value"),
            'is_currency_table': self.fun.get_element_property(main_window, self.fun.loc.IS_CURRENCY, "Value"),
            'is_sum_table': self.fun.get_element_property(main_window, self.fun.loc.IS_SUM_TABLE, "Value"),
            'is_closed_table': self.fun.get_element_property(main_window, self.fun.loc.IS_CLOSED_TABLE, "Value"),
            'is_nclosed_table': self.fun.get_element_property(main_window, self.fun.loc.IS_NCLOSED_TABLE, "Value"),
            'is_nincluded_table': self.fun.get_element_property(main_window, self.fun.loc.IS_NINCLUDED_TABLE, "Value"),
            'is_appointment_table': self.fun.get_element_property(main_window, self.fun.loc.IS_APPOINTMENT_TABLE, "Value"),
        })

        # 13. Удалить
        self.fun.click_element(main_window, self.fun.loc.RECIPIENT_1, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.DEL_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.YES_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.REFRESH_BUTTON_ORDER, timeout=1)

        self.fun.order_data.update({
            'freight_del_table_is': self.fun.get_element_property_sp(main_window, self.fun.loc.FREIGHT_TOTAL_RECORDS, "Value")
        })

        # 7 Создать Входящий счет и выставить покупателя
        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)
        time.sleep(1)
        self.fun.click_element_double_sp(main_window, self.fun.loc.VS_CREATE_ORDER)
        time.sleep(1)
        self.fun.order_data.update({
            'vs_create_order': self.fun.get_element_property_sp(main_window, self.fun.loc.VS_CREATE_ORDER, "Name"),
        })
        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)

        # 7 Переключение на форму ИС
        main_window = self.fun.get_check_vs_form()
        main_window.set_focus()
        main_window = self.fun.app.window(**self.fun.loc.CHECK_FROM_VS)
        time.sleep(1)

        # 7 Редактирование
        self.fun.click_element(main_window, self.fun.loc.IS_LIST, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.IS_FREIGHT1, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.IS_SUPPLIER, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.RECIPIENT_1, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.IS_BUYER, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.RECIPIENT_1, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.VS_CONTRACTOR, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.RECIPIENT_1, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.APPLY_BUTTON, timeout=1)

        # 7 Проверка полей
        self.fun.order_data.update({
            # 'is_name_form': self.fun.get_element_property(main_window, self.fun.loc.IS_NAME_FORM, "Value"),
            'vs_number': self.fun.get_element_property(main_window, self.fun.loc.IS_NUMBER, "Value"),
            'vs_date': self.fun.get_element_property(main_window, self.fun.loc.IS_DATE, "Value"),
            'vs_list': self.fun.get_element_property(main_window, self.fun.loc.IS_LIST, "Value"),
            'vs_suppler': self.fun.get_element_property(main_window, self.fun.loc.IS_SUPPLIER, "Value"),
            'vs_order': self.fun.get_element_property(main_window, self.fun.loc.VS_ORDER, "Value"),
            'vs_contractor': self.fun.get_element_property(main_window, self.fun.loc.VS_CONTRACTOR, "Value"),
            'vs_buyer': self.fun.get_element_property(main_window, self.fun.loc.IS_BUYER, "Value"),
        })

        self.fun.click_element(main_window, self.fun.loc.OK_BUTTON1, timeout=1)

        # Переключить на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()

        self.fun.click_element(main_window, self.fun.loc.REFRESH_BUTTON_ORDER, timeout=1)

        # 7 Поля в таблице
        self.fun.order_data.update({
            'vs_type_table': self.fun.get_element_property(main_window, self.fun.loc.IS_TYPE_CHECK, "Value"),
            'vs_number_table': self.fun.get_element_property(main_window, self.fun.loc.IS_NUMBER_TABLE, "Value"),
            'vs_date_table': self.fun.get_element_property(main_window, self.fun.loc.IS_DATE_TABLE, "Value"),
            'vs_suppler_table': self.fun.get_element_property(main_window, self.fun.loc.IS_SUPPLIER_TABLE, "Value"),
            'vs_buyer_table': self.fun.get_element_property(main_window, self.fun.loc.IS_BUYER_TABLE, "Value"),
            'vs_currency_table': self.fun.get_element_property(main_window, self.fun.loc.IS_CURRENCY, "Value"),
            'vs_sum_table': self.fun.get_element_property(main_window, self.fun.loc.IS_SUM_TABLE, "Value"),
            'vs_closed_table': self.fun.get_element_property(main_window, self.fun.loc.IS_CLOSED_TABLE, "Value"),
            'vs_nclosed_table': self.fun.get_element_property(main_window, self.fun.loc.IS_NCLOSED_TABLE, "Value"),
            'vs_nincluded_table': self.fun.get_element_property(main_window, self.fun.loc.IS_NINCLUDED_TABLE, "Value"),
            'vs_appointment_table': self.fun.get_element_property(main_window, self.fun.loc.IS_APPOINTMENT_TABLE, "Value"),
        })

        # 7 Удалить
        self.fun.click_element(main_window, self.fun.loc.RECIPIENT_1, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.DEL_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.YES_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.REFRESH_BUTTON_ORDER, timeout=1)

        self.fun.order_data.update({
            'freight_del_table_vs': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TOTAL_RECORDS, "Value")
        })

        # 7 Создать Входящий счет и выставить покупателя
        self.fun.click_element(main_window, self.fun.loc.CREATE_BUTTON, timeout=1)
        time.sleep(1)
        self.fun.click_element_double(main_window, self.fun.loc.IP_CREATE_ORDER, timeout=1)
        self.fun.order_data.update({
            'ip_create_order': self.fun.get_element_property(main_window, self.fun.loc.IP_CREATE_ORDER, "Name"),
        })
        self.fun.click_element(main_window, self.fun.loc.CREATE_BUTTON, timeout=1)

        # 7 Переключение на форму ИС
        main_window = self.fun.get_check_ip_form()
        main_window.set_focus()
        main_window = self.fun.app.window(**self.fun.loc.CHECK_FROM_IP)
        time.sleep(1)

        # 7 Редактирование
        self.fun.click_element(main_window, self.fun.loc.IS_LIST, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.IS_FREIGHT3, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.IS_SUPPLIER, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.RECIPIENT_1, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.IS_BUYER, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.RECIPIENT_1, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.APPLY_BUTTON, timeout=1)

        # 7 Проверка полей
        self.fun.order_data.update({
            # 'is_name_form': self.fun.get_element_property(main_window, self.fun.loc.IS_NAME_FORM, "Value"),
            'ip_number': self.fun.get_element_property(main_window, self.fun.loc.VP_NUMBER, "Value"),
            'ip_date': self.fun.get_element_property(main_window, self.fun.loc.IS_DATE, "Value"),
            'ip_list': self.fun.get_element_property(main_window, self.fun.loc.IS_LIST, "Value"),
            'ip_suppler': self.fun.get_element_property(main_window, self.fun.loc.IS_SUPPLIER, "Value"),
            'ip_order': self.fun.get_element_property(main_window, self.fun.loc.VP_ORDER, "Value"),
            'ip_buyer': self.fun.get_element_property(main_window, self.fun.loc.IS_BUYER, "Value"),
        })

        self.fun.click_element(main_window, self.fun.loc.OK_BUTTON1, timeout=1)

        # Переключить на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()

        self.fun.click_element(main_window, self.fun.loc.REFRESH_BUTTON_ORDER, timeout=1)

        # 7 Поля в таблице
        self.fun.order_data.update({
            'ip_type_table': self.fun.get_element_property(main_window, self.fun.loc.IS_TYPE_CHECK, "Value"),
            'ip_number_table': self.fun.get_element_property(main_window, self.fun.loc.IS_NUMBER_TABLE, "Value"),
            'ip_date_table': self.fun.get_element_property(main_window, self.fun.loc.IS_DATE_TABLE, "Value"),
            'ip_suppler_table': self.fun.get_element_property(main_window, self.fun.loc.IS_SUPPLIER_TABLE, "Value"),
            'ip_buyer_table': self.fun.get_element_property(main_window, self.fun.loc.IS_BUYER_TABLE, "Value"),
            'ip_currency_table': self.fun.get_element_property(main_window, self.fun.loc.IS_CURRENCY, "Value"),
            'ip_sum_table': self.fun.get_element_property(main_window, self.fun.loc.IS_SUM_TABLE, "Value"),
            'ip_closed_table': self.fun.get_element_property(main_window, self.fun.loc.IS_CLOSED_TABLE, "Value"),
            'ip_nclosed_table': self.fun.get_element_property(main_window, self.fun.loc.IS_NCLOSED_TABLE, "Value"),
            'ip_nincluded_table': self.fun.get_element_property(main_window, self.fun.loc.IS_NINCLUDED_TABLE, "Value"),
            'ip_appointment_table': self.fun.get_element_property(main_window, self.fun.loc.IS_APPOINTMENT_TABLE, "Value"),
        })

        # 7 Удалить
        self.fun.click_element(main_window, self.fun.loc.RECIPIENT_1, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.DEL_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.YES_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.REFRESH_BUTTON_ORDER, timeout=1)

        self.fun.order_data.update({
            'freight_del_table_ip': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TOTAL_RECORDS, "Value")
        })

        # 7 Создать Входящий счет и выставить покупателя
        self.fun.click_element(main_window, self.fun.loc.CREATE_BUTTON, timeout=1)
        time.sleep(1)
        self.fun.click_element_double(main_window, self.fun.loc.VP_CREATE_ORDER, timeout=1)
        self.fun.order_data.update({
            'vp_create_order': self.fun.get_element_property(main_window, self.fun.loc.VP_CREATE_ORDER, "Name"),
        })
        self.fun.click_element(main_window, self.fun.loc.CREATE_BUTTON, timeout=1)

        # 7 Переключение на форму ИС
        main_window = self.fun.get_check_vp_form()
        main_window.set_focus()
        main_window = self.fun.app.window(**self.fun.loc.CHECK_FROM_VP)
        time.sleep(1)

        # 7 Редактирование
        self.fun.click_element(main_window, self.fun.loc.IS_LIST, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.IS_FREIGHT2, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.IS_SUPPLIER, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.RECIPIENT_1, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.IS_BUYER, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.RECIPIENT_1, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.APPLY_BUTTON, timeout=1)

        # 7 Проверка полей
        self.fun.order_data.update({
            # 'is_name_form': self.fun.get_element_property(main_window, self.fun.loc.IS_NAME_FORM, "Value"),
            'vp_number': self.fun.get_element_property(main_window, self.fun.loc.VP_NUMBER, "Value"),
            'vp_date': self.fun.get_element_property(main_window, self.fun.loc.IS_DATE, "Value"),
            'vp_list': self.fun.get_element_property(main_window, self.fun.loc.IS_LIST, "Value"),
            'vp_suppler': self.fun.get_element_property(main_window, self.fun.loc.IS_SUPPLIER, "Value"),
            'vp_order': self.fun.get_element_property(main_window, self.fun.loc.VP_ORDER, "Value"),
            'vp_client': self.fun.get_element_property(main_window, self.fun.loc.GTD_CLIENT, "Value"),
            'vp_buyer': self.fun.get_element_property(main_window, self.fun.loc.IS_BUYER, "Value"),
        })

        self.fun.click_element(main_window, self.fun.loc.OK_BUTTON1, timeout=1)

        # Переключить на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()

        self.fun.click_element(main_window, self.fun.loc.REFRESH_BUTTON_ORDER, timeout=1)
        # 7 Поля в таблице
        self.fun.order_data.update({
            'vp_type_table': self.fun.get_element_property(main_window, self.fun.loc.IS_TYPE_CHECK, "Value"),
            'vp_number_table': self.fun.get_element_property(main_window, self.fun.loc.IS_NUMBER_TABLE, "Value"),
            'vp_date_table': self.fun.get_element_property(main_window, self.fun.loc.IS_DATE_TABLE, "Value"),
            'vp_suppler_table': self.fun.get_element_property(main_window, self.fun.loc.IS_SUPPLIER_TABLE, "Value"),
            'vp_buyer_table': self.fun.get_element_property(main_window, self.fun.loc.IS_BUYER_TABLE, "Value"),
            'vp_currency_table': self.fun.get_element_property(main_window, self.fun.loc.IS_CURRENCY, "Value"),
            'vp_sum_table': self.fun.get_element_property(main_window, self.fun.loc.IS_SUM_TABLE, "Value"),
            'vp_closed_table': self.fun.get_element_property(main_window, self.fun.loc.IS_CLOSED_TABLE, "Value"),
            'vp_nclosed_table': self.fun.get_element_property(main_window, self.fun.loc.IS_NCLOSED_TABLE, "Value"),
            'vp_nincluded_table': self.fun.get_element_property(main_window, self.fun.loc.IS_NINCLUDED_TABLE, "Value"),
            'vp_appointment_table': self.fun.get_element_property(main_window, self.fun.loc.IS_APPOINTMENT_TABLE, "Value"),
        })

        # 7 Удалить
        self.fun.click_element(main_window, self.fun.loc.RECIPIENT_1, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.DEL_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.YES_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.REFRESH_BUTTON_ORDER, timeout=1)

        self.fun.order_data.update({
            'freight_del_table_vp': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TOTAL_RECORDS, "Value")
        })
        return self.fun.order_data

    def close(self):
        """Завершение работы приложения"""
        self.fun.app.kill(soft=True)
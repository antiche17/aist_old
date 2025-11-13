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

    def transport_auto(self):
        # 1. Запуск приложения
        self.fun.start_application()
        time.sleep(3)

        # 3.
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(1)

        self.fun.click_element_sp(main_window, self.loc.AUTO_TRANSPORTATION1)
        time.sleep(3)
        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)
        time.sleep(1)

        # 4. Заполнение формы заказа
        self.fun.click_element(main_window, self.fun.loc.CLIENT_COMBO, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.CLIENT_COMBO_3, timeout=1)
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_ORDER_W)
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_ORDER_CREATE)
        time.sleep(1)
        text = self.fun.get_element_value(main_window, self.loc.FREIGHT_ORDER_W, timeout=1)
        self.fun.order_data = {
            'order_dialog_type': self.fun.get_element_property_sp(main_window, self.fun.loc.TYPE_TRANSPORTATION, "Value"),
            'order_dialog_client': self.fun.get_element_property_sp(main_window, self.fun.loc.CLIENT_COMBO, "Value"),
            'order_dialog_number': self.fun.get_element_property_sp(main_window, self.fun.loc.FREIGHT_ORDER_W, "Value"),
            'order_dialog_otv': self.fun.get_element_property_sp(main_window, self.fun.loc.RESPONSIBLE_COMBO, "Value"),
        }
        self.fun.click_element_sp(main_window, self.fun.loc.OK_BUTTON)
        time.sleep(2)
        main_window = self.fun.get_auto_form()
        main_window.set_focus()
        time.sleep(1)

        # 5. Проверка полей
        self.fun.order_data.update({
            'auto_order_number': self.fun.get_element_property_sp(main_window, self.fun.loc.AUTO_NAME_TRANSPORTATION, "Value"),
            'auto_type': self.fun.get_element_property_sp(main_window, self.fun.loc.AUTO_TYPE_TEXT, "Name"),
            'auto_status': self.fun.get_element_property_sp(main_window, self.fun.loc.STATUS_COMBO, "Value"),
            'auto_priority': self.fun.get_element_property_sp(main_window, self.fun.loc.PRIORITY_COMBO, "Value"),
            'auto_otv': self.fun.get_element_property_sp(main_window, self.fun.loc.RESPONSIBLE_COMBO, "Value"),

            'auto_create_date': self.fun.get_element_property_sp(main_window, self.fun.loc.CREATE_DATE, "Name"),
            'auto_mode_date': self.fun.get_element_property_sp(main_window, self.fun.loc.MOD_DATE, "Name"),
            'auto_finish_date': self.fun.get_element_property_sp(main_window, self.fun.loc.COMPLETION_DATE, "Name"),

            'auto_type_freight': self.fun.get_element_property_sp(main_window, self.fun.loc.TYPE_FREIGHT, "Value"),
            'auto_class_freight': self.fun.get_element_property_sp(main_window, self.fun.loc.CLASS_FREIGHT_AUTO, "Value"),
            'auto_download_method': self.fun.get_element_property_sp(main_window, self.fun.loc.DOWNLOAD_METHOD_AUTO, "Value"),
            'auto_ref_freight': self.fun.get_element_property_sp(main_window, self.fun.loc.REFERENCE_FREIGHT, "Value"),

            'auto_carrier': self.fun.get_element_property_sp(main_window, self.fun.loc.AUTO_CARRIER, "Value"),
            'auto_cmr': self.fun.get_element_property_sp(main_window, self.fun.loc.AUTO_CMR, "Value"),
            'auto_cmr_por': self.fun.get_element_property_sp(main_window, self.fun.loc.AUTO_CMR_POR, "Value"),

            'auto_note': self.fun.get_element_property_sp(main_window, self.fun.loc.NOTE, "Value"),
        })
        time.sleep(1)

        # 6. Редактирование полей
        self.fun.click_element_sp(main_window, self.fun.loc.STATUS_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.STATUS_COMBO_CANCEL2)
        self.fun.click_element_sp(main_window, self.fun.loc.PRIORITY_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.PRIORITY_COMBO_HIGH)
        self.fun.click_element_sp(main_window, self.fun.loc.RESPONSIBLE_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.RECIPIENT_1)

        self.fun.click_element_sp(main_window, self.fun.loc.TYPE_FREIGHT)
        self.fun.click_element_sp(main_window, self.fun.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.fun.loc.CLASS_FREIGHT_AUTO)
        self.fun.click_element_sp(main_window, self.fun.loc.CLASS_FREIGHT2)
        self.fun.click_element_sp(main_window, self.fun.loc.DOWNLOAD_METHOD_AUTO)
        self.fun.click_element_sp(main_window, self.fun.loc.DOWNLOAD_METHOD3)
        self.fun.set_text_field(main_window, self.fun.loc.REFERENCE_FREIGHT, "123456789Фы", timeout=1)

        self.fun.click_element_sp(main_window, self.fun.loc.AUTO_CARRIER)
        self.fun.click_element_sp(main_window, self.fun.loc.RECIPIENT_1)
        self.fun.set_text_field(main_window, self.fun.loc.AUTO_CMR, "345678912Йц", timeout=2)
        self.fun.set_text_field(main_window, self.fun.loc.AUTO_CMR_POR, "Ук1234123", timeout=1)
        self.fun.set_text_field(main_window, self.fun.loc.NOTE, "ываапв234123вамчвпаиач 12312533457", timeout=1)
        self.fun.click_element_sp(main_window, self.fun.loc.APPLY_BUTTON1)
        time.sleep(1)

        # 7. Проверка полей после редактирования
        self.fun.order_data.update({
            'auto_status_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.STATUS_COMBO, "Value"),
            'auto_priority_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.PRIORITY_COMBO, "Value"),
            'auto_otv_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.RESPONSIBLE_COMBO, "Value"),

            'auto_type_freight_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.TYPE_FREIGHT, "Value"),
            'auto_class_freight_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.CLASS_FREIGHT_AUTO, "Value"),
            'auto_download_method_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.DOWNLOAD_METHOD_AUTO, "Value"),
            'auto_ref_freight_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.REFERENCE_FREIGHT, "Value"),

            'auto_mode_date_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.MOD_DATE, "Name"),
            'auto_finish_date_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.COMPLETION_DATE, "Name"),

            'auto_carrier_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.AUTO_CARRIER, "Value"),
            'auto_cmr_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.AUTO_CMR, "Value"),
            'auto_cmr_por_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.AUTO_CMR_POR, "Value"),

            'auto_note_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.NOTE, "Value"),
        })
        self.fun.click_element_sp(main_window, self.fun.loc.TAB_ROUTES)

        # 8. Создание маршрутов автоперевозки
        # 9. Отгрузка
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.ROUTES_WINDOWS)
        self.fun.click_element_sp(main_window, self.loc.SHIPMENT)
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON)

        # 10. Прибытие
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.ROUTES_WINDOWS)
        self.fun.click_element_sp(main_window, self.loc.ARRIVAL)
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON)

        # 11. Сдача контейнера
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.ROUTES_WINDOWS)
        self.fun.click_element_sp(main_window, self.loc.CONTAINER_DELIVERY)
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON)

        # 13. Выставить водителя
        self.fun.click_element_sp(main_window, self.loc.DRIVER)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element_sp(main_window, self.loc.DRIVER)
        self.fun.click_element_sp(main_window, self.loc.NAME_LINE1)

        # 14. Указать Плановая дата отгрузки
        self.fun.click_element_sp(main_window, self.loc.PLAN_LOAD1)
        keyboard.send_keys('1')

        # 15. Указать Фактическая дата отгрузки
        self.fun.click_element_sp(main_window, self.loc.FACT_LOAD1)
        keyboard.send_keys('2')

        # 16. Указать Автомобиль
        self.fun.click_element_sp(main_window, self.loc.AUTO)
        keyboard.send_keys('х777хх 77 rus')
        keyboard.send_keys('{ENTER}')

        # 17. Указать Плановая дата прибытия
        self.fun.click_element_sp(main_window, self.loc.PLAN_ARRIVAL2)
        keyboard.send_keys('3')
        self.fun.click_element_sp(main_window, self.loc.PLAN_ARRIVAL3)
        keyboard.send_keys('4')

        # 18. Указать Фактическая дата прибытия
        self.fun.click_element_sp(main_window, self.loc.FACT_ARRIVAL2)
        keyboard.send_keys('5')
        self.fun.click_element_sp(main_window, self.loc.FACT_ARRIVAL3)
        keyboard.send_keys('6')
        self.fun.click_element_sp(main_window, self.fun.loc.APPLY_BUTTON1)
        time.sleep(1)
        self.fun.order_data.update({
            'address1': self.fun.get_element_property(main_window, self.fun.loc.ADDRESS_TABLE1, "Value"),
            'address2': self.fun.get_element_property(main_window, self.fun.loc.ADDRESS_TABLE2, "Value"),
            'address3': self.fun.get_element_property(main_window, self.fun.loc.ADDRESS_TABLE3, "Value"),
            'shipment1': self.fun.get_element_property_sp(main_window, self.fun.loc.SHIPMENT1, "Value"),
            'shipment2': self.fun.get_element_property_sp(main_window, self.fun.loc.SHIPMENT2, "Value"),
            'shipment3': self.fun.get_element_property_sp(main_window, self.fun.loc.SHIPMENT3, "Value"),
            'driver1': self.fun.get_element_property_sp(main_window, self.fun.loc.DRIVER_TABLE1, "Value"),
            'driver2': self.fun.get_element_property_sp(main_window, self.fun.loc.DRIVER_TABLE2, "Value"),
            'driver3': self.fun.get_element_property_sp(main_window, self.fun.loc.DRIVER_TABLE3, "Value"),
            'plan_load1': self.fun.get_element_property_sp(main_window, self.fun.loc.PLAN_LOAD1, "Value"),
            'plan_load2': self.fun.get_element_property_sp(main_window, self.fun.loc.PLAN_LOAD2, "Value"),
            'plan_load3': self.fun.get_element_property_sp(main_window, self.fun.loc.PLAN_LOAD3, "Value"),
            'fact_load1': self.fun.get_element_property_sp(main_window, self.fun.loc.FACT_LOAD1, "Value"),
            'fact_load2': self.fun.get_element_property_sp(main_window, self.fun.loc.FACT_LOAD2, "Value"),
            'fact_load3': self.fun.get_element_property_sp(main_window, self.fun.loc.FACT_LOAD3, "Value"),
            'car1': self.fun.get_element_property_sp(main_window, self.fun.loc.CAR_TABLE1, "Value"),
            'car2': self.fun.get_element_property_sp(main_window, self.fun.loc.CAR_TABLE2, "Value"),
            'car3': self.fun.get_element_property_sp(main_window, self.fun.loc.CAR_TABLE3, "Value"),
            'plan_arrival1': self.fun.get_element_property_sp(main_window, self.fun.loc.PLAN_ARRIVAL_DATA1, "Value"),
            'plan_arrival2': self.fun.get_element_property_sp(main_window, self.fun.loc.PLAN_ARRIVAL_DATA2, "Value"),
            'plan_arrival3': self.fun.get_element_property_sp(main_window, self.fun.loc.PLAN_ARRIVAL_DATA3, "Value"),
            'fact_arrival1': self.fun.get_element_property_sp(main_window, self.fun.loc.FACT_ARRIVAL_DATA1, "Value"),
            'fact_arrival2': self.fun.get_element_property_sp(main_window, self.fun.loc.FACT_ARRIVAL_DATA2, "Value"),
            'fact_arrival3': self.fun.get_element_property_sp(main_window, self.fun.loc.FACT_ARRIVAL_DATA3, "Value"),
        })
        # Открываем форму маршрутов Отгрузка
        self.fun.click_element_double_sp(main_window, self.fun.loc.RECIPIENT_1)

        main_window = self.fun.get_auto_shipment_form()
        main_window.set_focus()
        time.sleep(1)
        self.fun.order_data.update({
            'shipment_address': self.fun.get_element_property_sp(main_window, self.fun.loc.AUTO_ADDRESS,"Value"),
            'shipment_name': self.fun.get_element_property_sp(main_window, self.fun.loc.AUTO_NAME_TRANSPORTATION, "Value"),
            'shipment_driver': self.fun.get_element_property_sp(main_window, self.fun.loc.AUTO_DRIVER, "Value"),
            'shipment_auto': self.fun.get_element_property_sp(main_window, self.fun.loc.AUTO_FORM1, "Value"),
            'shipment_plan_data': self.fun.get_element_property_sp(main_window, self.fun.loc.SHIPMENT_DATA1, "Value"),
            'shipment_fact_data': self.fun.get_element_property_sp(main_window, self.fun.loc.PREFORWARDING_FACT_DATA, "Value"),
            'shipment_note': self.fun.get_element_property_sp(main_window, self.fun.loc.NOTE, "Value"),
        })
        self.fun.click_element_sp(main_window, self.loc.AUTO_ADDRESS)
        self.fun.click_element_sp(main_window, self.fun.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.AUTO_DRIVER)
        self.fun.click_element_double_sp(main_window, self.fun.loc.RECIPIENT_2)
        self.fun.click_element_double_sp(main_window, self.loc.AUTO_FORM1)
        keyboard.send_keys('rus44r444r')
        keyboard.send_keys('{ENTER}')
        self.fun.click_element_sp(main_window, self.loc.SHIPMENT_DATA1)
        time.sleep(1)
        keyboard.send_keys('{LEFT}' * 2)
        keyboard.send_keys('10')
        self.fun.click_element_sp(main_window, self.loc.PREFORWARDING_FACT_DATA)
        time.sleep(1)
        keyboard.send_keys('{LEFT}' * 2)
        keyboard.send_keys('11')
        time.sleep(1)
        self.fun.set_text_field(main_window, self.fun.loc.NOTE ,"Отгрузка", timeout=1)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.fun.loc.APPLY_BUTTON1)
        self.fun.order_data.update({
            'shipment_address_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.AUTO_ADDRESS, "Value"),
            'shipment_driver_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.AUTO_DRIVER, "Value"),
            'shipment_auto_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.AUTO_FORM1, "Value"),
            'shipment_plan_data_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.SHIPMENT_DATA1, "Value"),
            'shipment_fact_data_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.PREFORWARDING_FACT_DATA, "Value"),
            'shipment_note_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.NOTE, "Value"),
        })
        self.fun.click_element_sp(main_window, self.fun.loc.SAVE_BUTTON)
        main_window = self.fun.get_auto_form()
        main_window.set_focus()
        time.sleep(1)

        # 19. Открываем форму Прибытие
        self.fun.click_element_double_sp(main_window, self.fun.loc.RECIPIENT_2)
        main_window = self.fun.get_auto_shipment_form()
        main_window.set_focus()
        time.sleep(1)
        self.fun.order_data.update({
            'arrival_address': self.fun.get_element_property_sp(main_window, self.fun.loc.AUTO_ADDRESS, "Value"),
            'arrival_plan_data': self.fun.get_element_property_sp(main_window, self.fun.loc.ARRIVAL_DATA1, "Value"),
            'arrival_fact_data': self.fun.get_element_property_sp(main_window, self.fun.loc.ARRIVAL_DATA_FACT, "Value"),
            'arrival_note': self.fun.get_element_property(main_window, self.fun.loc.NOTE, "Value"),
        })
        self.fun.click_element_sp(main_window, self.loc.AUTO_ADDRESS)
        self.fun.click_element_sp(main_window, self.fun.loc.RECIPIENT_2)
        self.fun.click_element_sp(main_window, self.loc.ARRIVAL_DATA1)
        time.sleep(1)
        keyboard.send_keys('{LEFT}' * 2)
        keyboard.send_keys('12')
        self.fun.click_element_sp(main_window, self.loc.ARRIVAL_DATA_FACT)
        time.sleep(1)
        keyboard.send_keys('{LEFT}' * 2)
        keyboard.send_keys('13')
        time.sleep(1)
        self.fun.set_text_field(main_window, self.fun.loc.NOTE, "Прибытие", timeout=1)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.fun.loc.APPLY_BUTTON1)
        time.sleep(1)
        self.fun.order_data.update({
            'arrival_address_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.AUTO_ADDRESS, "Value"),
            'arrival_plan_data_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.ARRIVAL_DATA1, "Value"),
            'arrival_fact_data_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.ARRIVAL_DATA_FACT, "Value"),
            'arrival_note_mod': self.fun.get_element_property(main_window, self.fun.loc.NOTE, "Value"),
        })
        self.fun.click_element_sp(main_window, self.fun.loc.SAVE_BUTTON)

        main_window = self.fun.get_auto_form()
        main_window.set_focus()
        time.sleep(1)

        # 20. Открываем формы маршрутов Сдача контейнера
        self.fun.click_element_double_sp(main_window, self.fun.loc.RECIPIENT_3)
        main_window = self.fun.get_auto_shipment_form()
        main_window.set_focus()
        time.sleep(1)
        self.fun.order_data.update({
            #'shipment3': self.fun.get_element_property(main_window, self.fun.loc.SHIPMENT3, "Value"),
            'drop_con_address': self.fun.get_element_property_sp(main_window, self.fun.loc.TERMINAL_CHANGE, "Value"),
            'drop_con_plan_data': self.fun.get_element_property_sp(main_window, self.fun.loc.ARRIVAL_DATA1, "Value"),
            'drop_con_fact_data': self.fun.get_element_property_sp(main_window, self.fun.loc.ARRIVAL_DATA_FACT, "Value"),
            'drop_con_note': self.fun.get_element_property_sp(main_window, self.fun.loc.NOTE, "Value"),
        })
        self.fun.click_element_sp(main_window, self.loc.TERMINAL_CHANGE)
        self.fun.click_element_sp(main_window, self.fun.loc.RECIPIENT_5)
        self.fun.click_element_sp(main_window, self.loc.ARRIVAL_DATA1)
        time.sleep(1)
        keyboard.send_keys('{LEFT}' * 2)
        keyboard.send_keys('14')
        self.fun.click_element_sp(main_window, self.loc.ARRIVAL_DATA_FACT)
        time.sleep(1)
        keyboard.send_keys('{LEFT}' * 2)
        keyboard.send_keys('15')
        self.fun.set_text_field(main_window, self.fun.loc.NOTE, "Сдача контейнера", timeout=1)
        self.fun.click_element_sp(main_window, self.fun.loc.APPLY_BUTTON1)
        self.fun.order_data.update({
            'drop_con_address_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.TERMINAL_CHANGE, "Value"),
            'drop_con_plan_data_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.ARRIVAL_DATA1, "Value"),
            'drop_con_fact_data_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.ARRIVAL_DATA_FACT, "Value"),
            'drop_con_note_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.NOTE, "Value"),
        })
        self.fun.click_element_sp(main_window, self.fun.loc.SAVE_BUTTON)
        main_window = self.fun.get_auto_form()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.fun.loc.REFRESH_BUTTON_ORDER)
        self.fun.order_data.update({
            'shipment1_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.SHIPMENT1, "Value"),
            'shipment2_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.SHIPMENT2, "Value"),
            'shipment3_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.SHIPMENT3, "Value"),
            'address1_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.ADDRESS_TABLE1, "Value"),
            'address2_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.ADDRESS_TABLE2, "Value"),
            'address3_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.ADDRESS_TABLE3, "Value"),
            'driver1_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.DRIVER_TABLE1, "Value"),
            'driver2_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.DRIVER_TABLE2, "Value"),
            'driver3_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.DRIVER_TABLE3, "Value"),
            'plan_load1_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.PLAN_LOAD1, "Value"),
            'plan_load2_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.PLAN_LOAD2, "Value"),
            'plan_load3_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.PLAN_LOAD3, "Value"),
            'fact_load1_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.FACT_LOAD1, "Value"),
            'fact_load2_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.FACT_LOAD2, "Value"),
            'fact_load3_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.FACT_LOAD3, "Value"),
            'car1_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.CAR_TABLE1, "Value"),
            'car2_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.CAR_TABLE2, "Value"),
            'car3_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.CAR_TABLE3, "Value"),
            'plan_arrival1_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.PLAN_ARRIVAL_DATA1, "Value"),
            'plan_arrival2_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.PLAN_ARRIVAL_DATA2, "Value"),
            'plan_arrival3_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.PLAN_ARRIVAL_DATA3, "Value"),
            'fact_arrival1_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.FACT_ARRIVAL_DATA1, "Value"),
            'fact_arrival2_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.FACT_ARRIVAL_DATA2, "Value"),
            'fact_arrival3_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.FACT_ARRIVAL_DATA3, "Value"),
        })
        self.fun.click_element_sp(main_window, self.fun.loc.SAVE_BUTTON)

        # 21. Открываем таблицу для проверки изменений
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.fun.loc.DEL_WINDOW_BUTTON)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.AUTO_TRANSPORTATION1)
        time.sleep(2)
        self.fun.order_data.update({
            'order_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.ORDER_TABLE1, "Value"),
            'status_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_STATUS, "Value"),
            'priority_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_PRIORITY, "Value"),
            'responsible_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.RESPONSIBLE_TABLE1, "Value"),
            'carrier_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.CARRIER_TABLE1, "Value"),
            'cargo_class_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.CARGO_CLASS_TABLE1, "Value"),
            'loading_method_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.LOADING_METHOD_TABLE1, "Value"),
            'cmr_number_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.CMR_NUMBER_TABLE1, "Value"),
            'note_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.NOTE_LINE1, "Value"),
            'created_by_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.CREATED_BY_TABLE1, "Value"),
            'creation_date_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.CREATION_DATE_TABLE1, "Value"),
            'modification_date_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.MODIFICATION_DATE_TABLE1, "Value"),
            'completion_date_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.COMPLETION_DATE_TABLE1, "Value"),
            'cargo_type_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.CARGO_TYPE_TABLE1, "Value"),
        })
        self.fun.click_element_sp(main_window, self.fun.loc.ORDERS_TAB)
        time.sleep(2)
        self.fun.click_element_sp(main_window, self.fun.loc.TABLE_ORDER_NUMBER_FILTER)
        keyboard.send_keys(text, with_spaces=True)
        self.fun.click_element_double_sp(main_window, self.fun.loc.TABLE_ORDER_NUMBER)
        time.sleep(2)
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)
        self.fun.order_data.update({
            'order_number': self.fun.get_element_property_sp(main_window, self.fun.loc.ORDER_NUMBER, "Value"),
            'order_type': self.fun.get_element_property_sp(main_window, self.fun.loc.ORDER_TYPE_TEXT, "Name"),
            'order_status': self.fun.get_element_property_sp(main_window, self.fun.loc.STATUS_COMBO, "Value"),
            'order_priority': self.fun.get_element_property_sp(main_window, self.fun.loc.PRIORITY_COMBO, "Value"),
            'order_otv': self.fun.get_element_property_sp(main_window, self.fun.loc.RESPONSIBLE_COMBO, "Value"),

            'order_client': self.fun.get_element_property_sp(main_window, self.fun.loc.CLIENT_COMBO, "Value"),
            'order_senders': self.fun.get_element_property_sp(main_window, self.fun.loc.SENDERS_1, "Value"),
            'order_recipient': self.fun.get_element_property_sp(main_window, self.fun.loc.RECIPIENT, "Value"),
            'order_delivery': self.fun.get_element_property_sp(main_window, self.fun.loc.DELIVERY_CONDITION, "Value"),

            'order_create_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.MOD_DATE, "Name"),
            'order_create_date': self.fun.get_element_property_sp(main_window, self.fun.loc.CREATE_DATE, "Name"),
            'order_completion_date': self.fun.get_element_property_sp(main_window, self.fun.loc.COMPLETION_DATE, "Name"),
            'order_reference': self.fun.get_element_property_sp(main_window, self.fun.loc.REFERENCE, "Value"),
            'order_note': self.fun.get_element_property_sp(main_window, self.fun.loc.NOTE, "Value"),

            'order_tab_freight': self.fun.get_element_property_sp(main_window, self.fun.loc.TAB_FREIGHT, "Name"),
            'order_tab_transportation': self.fun.get_element_property_sp(main_window, self.fun.loc.TAB_TRANSPORTATION, "Name"),
            'order_tab_forwarding': self.fun.get_element_property_sp(main_window, self.fun.loc.TAB_FORWARDING, "Name"),
            'order_tab_gtd': self.fun.get_element_property_sp(main_window, self.fun.loc.TAB_GTD, "Name"),
            'order_tab_check': self.fun.get_element_property_sp(main_window, self.fun.loc.TAB_CHECK, "Name"),
            'order_tab_file': self.fun.get_element_property_sp(main_window, self.fun.loc.TAB_FILE, "Name"),
            'order_tab_services': self.fun.get_element_property_sp(main_window, self.fun.loc.TAB_SERVICES, "Name"),
            'order_tab_tracking': self.fun.get_element_property_sp(main_window, self.fun.loc.TAB_TRACKING, "Name"),
        })
        # Проверка автоперевозки в заказе
        self.fun.click_element_sp(main_window, self.fun.loc.TAB_TRANSPORTATION)
        self.fun.order_data.update({
            'trans_type': self.fun.get_element_property_sp(main_window, self.fun.loc.TRANSPORTATION_ITEM, "Value"),
            'trans_number': self.fun.get_element_property_sp(main_window, self.fun.loc.TRANSPORTATION_NUMBER1, "Name"),
            'trans_status': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_STATUS, "Value"),
            'trans_carrier': self.fun.get_element_property_sp(main_window, self.fun.loc.CARRIER_TABLE1, "Value"),
            'trans_doc': self.fun.get_element_property_sp(main_window, self.fun.loc.AUTO_DOC, "Value"),

            'trans_data': self.fun.get_element_property_sp(main_window, self.fun.loc.AUTO_DATE, "Value"),
            'trans_address': self.fun.get_element_property_sp(main_window, self.fun.loc.AUTO_DEPARTURE_PLACE, "Value"),
            'trans_arrival_date': self.fun.get_element_property_sp(main_window, self.fun.loc.AUTO_ARRIVAL_DATE, "Value"),
            'trans_arrival_address': self.fun.get_element_property_sp(main_window, self.fun.loc.AUTO_ARRIVAL_PLACE, "Value"),
            'trans_priority': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_PRIORITY, "Value"),
            'trans_type_cargo': self.fun.get_element_property_sp(main_window, self.fun.loc.CARGO_TYPE_TABLE1, "Value"),
        })
        return self.fun.order_data

    def close(self):
        """Завершение работы приложения"""
        self.fun.app.kill(soft=True)
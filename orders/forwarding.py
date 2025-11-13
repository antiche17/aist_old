from pywinauto import Application, keyboard
from locators.locators import LocOrders
from locators.function import Function
import time


class WinAISTApp:
    def __init__(self):
        self.fun = Function()
        self.loc = LocOrders()
        self.app = self.fun.app

    def forwarding(self):
        # 1. Запуск приложения
        self.fun.start_application()
        time.sleep(3)

        # 3.
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(1)

        self.fun.click_element_sp(main_window, self.loc.FORWARDING)
        time.sleep(4)
        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)
        time.sleep(1)

        # 4. Заполнение формы Экспедирования
        self.fun.click_element_sp(main_window, self.fun.loc.CLIENT_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.CLIENT_COMBO_3)
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_ORDER_W)
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_ORDER_CREATE)
        time.sleep(1)
        text = self.fun.get_element_value(main_window, self.loc.FREIGHT_ORDER_W, timeout=1)
        self.fun.order_data = {
            'forwarding_dialog_type': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_TYPE_DIALOG, "Value"),
            'forwarding_dialog_client': self.fun.get_element_property_sp(main_window, self.fun.loc.CLIENT_COMBO, "Value"),
            'forwarding_dialog_number': self.fun.get_element_property_sp(main_window, self.fun.loc.FREIGHT_ORDER_W, "Value"),
            'forwarding_dialog_otv': self.fun.get_element_property_sp(main_window, self.fun.loc.RESPONSIBLE_COMBO, "Value"),
        }
        self.fun.click_element_sp(main_window, self.fun.loc.OK_BUTTON)
        time.sleep(2)

        main_window = self.fun.get_forwarding_form()
        main_window.set_focus()
        time.sleep(1)

        # 5. Проверка полей формы Экспедирования
        self.fun.order_data.update({
            'forwarding_order_number': self.fun.get_element_property(main_window, self.fun.loc.AUTO_NAME_TRANSPORTATION, "Value"),
            'forwarding_type': self.fun.get_element_property(main_window, self.fun.loc.AUTO_TYPE_TEXT, "Name"),
            'forwarding_status': self.fun.get_element_property(main_window, self.fun.loc.STATUS_COMBO, "Value"),
            'forwarding_priority': self.fun.get_element_property(main_window, self.fun.loc.PRIORITY_COMBO, "Value"),
            'forwarding_otv': self.fun.get_element_property(main_window, self.fun.loc.RESPONSIBLE_COMBO, "Value"),

            'forwarding_create_date': self.fun.get_element_property(main_window, self.fun.loc.CREATE_DATE, "Name"),
            'forwarding_mode_date': self.fun.get_element_property(main_window, self.fun.loc.MOD_DATE, "Name"),
            'forwarding_finish_date': self.fun.get_element_property(main_window, self.fun.loc.COMPLETION_DATE, "Name"),

            'forwarding_type_freight': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_FORWARDER, "Value"),
            'forwarding_class_freight': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_NOMINATION, "Value"),
            'forwarding_download_method': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_TELEX, "Value"),
            'forwarding_ref_freight': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_RECEIVING_DOC, "Value"),

            'forwarding_note': self.fun.get_element_property(main_window, self.fun.loc.NOTE, "Value"),

            'tab_info': self.fun.get_element_property(main_window, self.fun.loc.TAB_INFO, "Name"),
            'tab_forwarding': self.fun.get_element_property(main_window, self.fun.loc.TAB_FORWARDING_FREIGHT, "Name"),
            'tab_services': self.fun.get_element_property(main_window, self.fun.loc.TAB_SERVICES, "Name"),
            'tab_file': self.fun.get_element_property(main_window, self.fun.loc.TAB_FILE, "Name"),
        })
        time.sleep(1)

        self.fun.click_element_sp(main_window, self.fun.loc.STATUS_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.CARGO_RECEIVED)
        self.fun.click_element_sp(main_window, self.fun.loc.PRIORITY_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.PRIORITY_COMBO_LOW)
        self.fun.click_element_sp(main_window, self.fun.loc.RESPONSIBLE_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.RECIPIENT_6)
        self.fun.click_element_sp(main_window, self.fun.loc.FORWARDING_FORWARDER)
        self.fun.click_element_sp(main_window, self.fun.loc.RECIPIENT_2)
        self.fun.click_element(main_window, self.loc.FORWARDING_NOMINATION, timeout=1)
        keyboard.send_keys('1')
        self.fun.click_element_sp(main_window, self.loc.FORWARDING_TELEX)
        keyboard.send_keys('2')
        self.fun.click_element_sp(main_window, self.loc.FORWARDING_RECEIVING_DOC)
        keyboard.send_keys('3')
        time.sleep(1)
        self.fun.set_text_field(main_window, self.fun.loc.NOTE, "Экспедирование", timeout=1)
        self.fun.click_element_sp(main_window, self.fun.loc.APPLY_BUTTON1)
        time.sleep(1)

        # 5. Проверка полей Экспедирования после редактирования
        self.fun.order_data.update({
            'forwarding_status_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.STATUS_COMBO, "Value"),
            'forwarding_priority_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.PRIORITY_COMBO, "Value"),
            'forwarding_otv_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.RESPONSIBLE_COMBO, "Value"),
            
            'forwarding_type_freight_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_FORWARDER, "Value"),
            'forwarding_class_freight_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_NOMINATION, "Value"),
            'forwarding_download_method_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_TELEX, "Value"),
            'forwarding_ref_freight_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_RECEIVING_DOC, "Value"),

            'forwarding_note_mod': self.fun.get_element_property(main_window, self.fun.loc.NOTE, "Value"),
        })

        self.fun.click_element_sp(main_window, self.fun.loc.TAB_FORWARDING_FREIGHT)
        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.fun.loc.ADD_TE)
        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)
        self.fun.click_element(main_window, self.fun.loc.FREIGHT_CREATE_TE, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.FREIGHT_CREATE_TE1, timeout=1)
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_CREATE_TYPE)
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_CREATE_TYPE1)
        self.fun.set_text_field(main_window, self.fun.loc.FREIGHT_CREATE_QUANTITY, 1, timeout=1)
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_CREATE_UOM)
        self.fun.click_element_sp(main_window, self.fun.loc.FREIGHT_CREATE_UOM1)
        time.sleep(1)

        # 8 Взять данные из создания ТЕ
        self.fun.order_data.update({
            'order_dialog_te': self.fun.get_element_property_sp(main_window, self.fun.loc.FREIGHT_CREATE_TE, "Value"),
            'order_dialog_type': self.fun.get_element_property_sp(main_window, self.fun.loc.FREIGHT_CREATE_TYPE, "Value"),
            'order_dialog_quantity': self.fun.get_element_property_sp(main_window, self.fun.loc.FREIGHT_CREATE_QUANTITY, "Value"),
            'order_dialog_uom': self.fun.get_element_property_sp(main_window, self.fun.loc.FREIGHT_CREATE_UOM, "Value"),
            'order_dialog_number': self.fun.get_element_property_sp(main_window, self.fun.loc.FREIGHT_CREATE_ORDER, "Value"),
        })
        time.sleep(1)
        self.fun.click_element(main_window, self.fun.loc.OK_BUTTON, timeout=1)
        time.sleep(1)
        main_window = self.fun.get_forwarding_form()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element(main_window, self.fun.loc.ADD_TE, timeout=1)
        keyboard.send_keys('{DOWN}')
        self.fun.click_element(main_window, self.fun.loc.OK_BUTTON, timeout=1)

        self.fun.click_element_double(main_window, self.fun.loc.RECIPIENT_1)
        time.sleep(1)
        main_window = self.fun.get_freight_form()
        main_window.set_focus()
        time.sleep(1)

        self.fun.click_element_sp(main_window, self.loc.FORWARDING_RECEIVING_DO)
        keyboard.send_keys('4')
        self.fun.set_text_field(main_window, self.fun.loc.NOTE_CONTAINER, "Экспедирование", timeout=1)
        self.fun.click_element_sp(main_window, self.fun.loc.APPLY_BUTTON1)

        # 5. Проверка полей bulkership
        self.fun.order_data.update({
            'bul_type_form': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_TYPE_TEXT, "Name"),
            'bul_type_te_form': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_CREATE_TYPE, "Value"),
            'bul_quantity_form': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_TE_QUANTITY_FORM, "Value"),
            'bul_uom_form': self.fun.get_element_property(main_window, self.loc.FREIGHT_TE_UOM, "Value"),
            'bul_te_number_form': self.fun.get_element_property(main_window, self.loc.FREIGHT_TE_NUMBER_FORM, "Value"),
            'bul_number_form': self.fun.get_element_property(main_window, self.loc.FREIGHT_TE_NUMBER_FORM, "Value"),
            'bul_te_number': self.fun.get_element_property(main_window, self.loc.FREIGHT_TE_NUMBER_FORM, "Value"),

            'bul_do_form': self.fun.get_element_property(main_window, self.loc.FORWARDING_RECEIVING_DO, "Value"),
            'bul_note_form': self.fun.get_element_property(main_window, self.loc.NOTE_CONTAINER, "Value"),
        })
        self.fun.click_element(main_window, self.fun.loc.OK_BUTTON, timeout=1)
        main_window = self.fun.get_forwarding_form()
        main_window.set_focus()
        time.sleep(1)

        self.fun.click_element(main_window, self.fun.loc.OK_BUTTON, timeout=1)

        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(4)
        self.fun.click_element_sp(main_window, self.fun.loc.ORDERS_TAB)
        time.sleep(5)
        self.fun.click_element_sp(main_window, self.fun.loc.TABLE_ORDER_NUMBER_FILTER)
        keyboard.send_keys(text, with_spaces=True)
        self.fun.click_element_double(main_window, self.fun.loc.RECIPIENT_1)

        # 7. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)
        self.fun.order_data.update({
            'order_type_form': self.fun.get_element_property(main_window, self.fun.loc.ORDER_TYPE_TEXT, "Name"),
            'order_client_form': self.fun.get_element_property(main_window, self.fun.loc.CLIENT_COMBO, "Value"),
            'order_otv_form': self.fun.get_element_property(main_window, self.fun.loc.RESPONSIBLE_COMBO, "Value"),
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

        self.fun.click_element(main_window, self.loc.FEEDER_LINE, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TE2, timeout=1)
        self.fun.set_text_field(main_window, self.loc.FEEDER_KONOS, "Документы №2", timeout=1)
        self.fun.click_element(main_window, self.loc.APPLY_BUTTON1, timeout=1)
        self.fun.click_element_sp(main_window, self.fun.loc.APPLY_BUTTON1)

        # 5. Проверка полей морской перевозки
        self.fun.order_data.update({
            'feeder_line': self.fun.get_element_property_sp(main_window, self.fun.loc.FEEDER_LINE, "Value"),
            'feeder_konos': self.fun.get_element_property_sp(main_window, self.fun.loc.FEEDER_KONOS, "Value"),
        })

        self.fun.click_element_sp(main_window, self.fun.loc.TAB_ROUTES)

        # 9. Прибытие
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.ROUTES_WINDOWS, timeout=3)
        self.fun.click_element(main_window, self.loc.ARRIVAL, timeout=3)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)
        time.sleep(1)
        # 9. Порт выставление данных в маршруты
        self.fun.click_element_double_sp(main_window, self.loc.RECIPIENT_1)
        main_window = self.fun.get_preforwarding_form()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.PREFORWARDING_TERMINAL2)
        self.fun.click_element_sp(main_window, self.loc.SEARCH_BOX)
        keyboard.send_keys('москва')
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.SAVE_BUTTON)
        main_window = self.fun.get_sea_form()
        main_window.set_focus()
        time.sleep(1)

        self.fun.click_element(main_window, self.loc.PLAN_ARRIVAL1, timeout=3)
        keyboard.send_keys('3')
        self.fun.click_element(main_window, self.loc.FACT_ARRIVAL1, timeout=3)
        keyboard.send_keys('4')
        self.fun.click_element_sp(main_window, self.fun.loc.APPLY_BUTTON1)
        # 9. Поля прибытие
        self.fun.order_data.update({
            'port': self.fun.get_element_property_sp(main_window, self.fun.loc.PORT1, "Value"),
            'terminal': self.fun.get_element_property_sp(main_window, self.fun.loc.TERMINAL_LINE1, "Value"),
            'plan_arrival': self.fun.get_element_property_sp(main_window, self.fun.loc.PLAN_ARRIVAL1, "Value"),
            'fact_arrival': self.fun.get_element_property_sp(main_window, self.fun.loc.FACT_ARRIVAL1, "Value"),
        })

        self.fun.click_element_sp(main_window, self.fun.loc.TAB_FREIGHT)
        # 10. Добавить груз в морскую перевозку
        self.fun.click_element_sp(main_window, self.loc.TAB_FREIGHT)
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.OPEN_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.DELIVERY_CONDITION_0)
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON)

        # Закрываем морскую перевозку
        self.fun.click_element_sp(main_window, self.loc.SAVE_BUTTON)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        self.fun.click_element_sp(main_window, self.fun.loc.TAB_FORWARDING)
        # Проверка данных в заказе
        self.fun.order_data.update({
            'order_forwading_item': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_ITEM, "Value"),
            'order_forwading_numder': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_NUMBER, "Value"),
            'order_forwading_status': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_STATUS, "Value"),
            'order_forwading_otv': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_OTV, "Value"),
            'order_forwading_forward': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_FORWARD, "Value"),
            'order_forwading_te': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_TE, "Value"),
            'order_forwading_data_create': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_DATA_CREATE, "Value"),
            'order_forwading_data_finish': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_DATA_FINISH, "Value"),
            'order_forwading_note': self.fun.get_element_property(main_window, self.fun.loc.NOTE_LINE1, "Value"),

        })
        self.fun.click_element_double(main_window, self.loc.LINE_TRANSPORTATION, timeout=2)

        # 14. Переключится на форму Экспедирование
        main_window = self.fun.get_forwarding_form()
        main_window.set_focus()
        time.sleep(1)

        self.fun.click_element_sp(main_window, self.fun.loc.TAB_FORWARDING_FREIGHT)
        self.fun.click_element_sp(main_window, self.fun.loc.REFRESH_BUTTON1)
        time.sleep(1)
        # Проверка отображения данных в вкладке Экспедируемый груз
        self.fun.order_data.update({
            'order_forwarding_fid_kons1': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_FID_KONS1, "Value"),
            'order_forwarding_plan_arrival1': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_PLAN_ARRIVAL1, "Value"),
            'order_forwarding_fact_arrival1': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_FACT_ARRIVAL1, "Value"),
            'order_forwarding_fid_line1': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_FID_LINE1, "Value"),
            'order_forwarding_port1': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_PORT1, "Value"),
            'order_forwarding_terminal1': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_TERMINAL1, "Value"),
            'order_forwarding_te1': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_TE1, "Value"),
            'order_forwarding_te_type1': self.fun.get_element_property_sp(main_window, self.fun.loc.TYPE_TE_TABLE1, "Value"),
            'order_forwarding_te_number1': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_TE_NUMBER1, "Value"),
            'order_forwarding_release1': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_RELEASE1, "Value"),
            'order_forwarding_doc1': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_DOC1, "Value"),
            'order_forwarding_nomination1': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_NOMINATION1, "Value"),
            'order_forwarding_do_do1': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_DO_DO1, "Value"),
            'order_forwarding_note1': self.fun.get_element_property(main_window, self.fun.loc.NOTE_LINE1, "Value"),

        })

        self.fun.click_element(main_window, self.loc.SAVE_BUTTON, timeout=2)

        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element(main_window, self.loc.SAVE_BUTTON, timeout=2)

        main_window = self.fun.get_main_window()
        main_window.set_focus()

        self.fun.click_element_sp(main_window, self.loc.FORWARDING)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.fun.loc.REFRESH_BUTTON)
        time.sleep(1)
        self.fun.right_click_element(main_window, self.loc.ORDER_TABLE, timeout=2)
        time.sleep(1)
        keyboard.send_keys('{DOWN}' * 7)
        keyboard.send_keys('{ENTER}')
        time.sleep(1)

        self.fun.click_element_double_sp(main_window, self.loc.QUANTITY_TE_TABLE)
        self.fun.click_element_double_sp(main_window, self.loc.NUMBER_FORWARDING_TABLE)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_ORDER_TABLE)
        keyboard.send_keys(text, with_spaces=True)

        # 5. Данные в таблице Экспедиция
        self.fun.order_data.update({
            'order_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.ORDER_TABLE1, "Value"),
            'type_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.TYPE_TABLE1, "Value"),
            'status_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_STATUS, "Value"),
            'priority_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_PRIORITY, "Value"),
            'responsible_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.RESPONSIBLE_TABLE1, "Value"),
            'expeditor_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.EXPEDITOR_TABLE1, "Value"),
            'telex_release_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.TELEX_RELEASE_TABLE1, "Value"),
            'receive_doc_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.RECEIVE_DOC_TABLE1, "Value"),
            'nomination_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.NOMINATION_TABLE1, "Value"),
            'note_table1': self.fun.get_element_property(main_window, self.fun.loc.NOTE_LINE1, "Value", timeout=1),
            'created_by_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.CREATED_BY_TABLE1, "Value"),
            'created_date_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.CREATED_DATE_TABLE1, "Value"),
            'updated_date_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.UPDATED_DATE_TABLE1, "Value"),
            'finished_date_table1': self.fun.get_element_property_sp(main_window, self.fun.loc.FINISHED_DATE_TABLE1, "Value"),
            'forwarding_number_header': self.fun.get_element_property_sp(main_window, self.fun.loc.FORWARDING_NUMBER_HEADER, "Value"),
            'te_count_header': self.fun.get_element_property_sp(main_window, self.fun.loc.TE_COUNT_HEADER, "Value"),
        })

        return self.fun.order_data

    def close(self):
        """Завершение работы приложения"""
        self.fun.app.kill(soft=True)
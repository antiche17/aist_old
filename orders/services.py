from pywinauto import Application, keyboard
from locators.locators import LocOrders
from locators.function import Function
import time


class WinAISTApp:
    def __init__(self):
        self.fun = Function()
        self.loc = LocOrders()
        self.app = self.fun.app

    def services(self):
        # 1. Запуск приложения
        self.fun.start_application()

        # 2. Переход в раздел Заказы
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(4)

        self.fun.click_element_sp(main_window, self.fun.loc.ORDERS_TAB)
        time.sleep(5)

        # 4. Создание нового заказа
        self.fun.click_element_sp(main_window, self.fun.loc.ADD_BUTTON)
        time.sleep(2)

        # 5. Заполнение формы заказа
        self.fun.click_element_sp(main_window, self.fun.loc.ORDER_TYPE_COMBO)
        time.sleep(1)
        self.fun.click_element(main_window, self.fun.loc.LOGISTICS_ITEM, timeout=1)
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
            'order_number': self.fun.get_element_property(main_window, self.fun.loc.ORDER_NUMBER, "Value")
        })

        # 6. Перейти во вкладку Услуги
        self.fun.click_element_sp(main_window, self.fun.loc.TAB_SERVICES)
        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.fun.loc.SERVICES_ADD)
        keyboard.send_keys('Перет')
        keyboard.send_keys('{ENTER}')
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.fun.loc.OK_BUTTON)
        time.sleep(1)
        # 7. Проверка полей
        self.fun.order_data.update({
            'service_type': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICE_LINE1, "Value"),
            'service_rate': self.fun.get_element_property_sp(main_window, self.fun.loc.RATE_LINE1, "Value"),
            'service_currency': self.fun.get_element_property_sp(main_window, self.fun.loc.CURRENCY_LINE1, "Value"),
            'service_vat': self.fun.get_element_property_sp(main_window, self.fun.loc.VAT_LINE1, "Value"),
            'service_quantity': self.fun.get_element_property_sp(main_window, self.fun.loc.QUANTITY_TABLE1, "Value"),
            'service_te_type': self.fun.get_element_property(main_window, self.fun.loc.TYPE_TE_TABLE1, "Value"),
            'service_te_number': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_TE_NUMBER, "Value"),
            'service_note': self.fun.get_element_property_sp(main_window, self.fun.loc.NOTE_LINE1, "Value"),
            'service_source': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICE_SOURCE, "Value"),
            'service_account': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICE_ACCOUNT, "Value"),
        })

        # 8. Редактирование услуги в гриде
        self.fun.click_element_sp(main_window, self.fun.loc.RATE_LINE1)
        keyboard.send_keys('100')
        self.fun.click_element_sp(main_window, self.fun.loc.CURRENCY_LINE1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element_sp(main_window, self.fun.loc.CURRENCY_LINE1)
        self.fun.click_element_sp(main_window, self.fun.loc.RUR)
        self.fun.click_element_sp(main_window, self.fun.loc.VAT_LINE1)
        keyboard.send_keys('0')
        keyboard.send_keys('{ENTER}')
        self.fun.click_element_sp(main_window, self.fun.loc.NOTE_LINE1)
        keyboard.send_keys('Услуга')
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.fun.loc.APPLY_BUTTON1)
        time.sleep(1)

        # 7. Проверка полей
        self.fun.order_data.update({
            'service_type_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICE_LINE1, "Value"),
            'service_rate_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.RATE_LINE1, "Value"),
            'service_currency_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.CURRENCY_LINE1, "Value"),
            'service_vat_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.VAT_LINE1, "Value"),
            'service_quantity_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.QUANTITY_TABLE1, "Value"),
            'service_te_type_mod': self.fun.get_element_property(main_window, self.fun.loc.TYPE_TE_TABLE1, "Value"),
            'service_te_number_mod': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_TE_NUMBER, "Value"),
            'service_note_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.NOTE_LINE1, "Value"),
            'service_source_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICE_SOURCE, "Value"),
            'service_account_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICE_ACCOUNT, "Value"),
        })
        # Открываем форму Услуги
        self.fun.click_element_double_sp(main_window, self.fun.loc.SERVICE_LINE1)

        main_window = self.fun.get_services_form_new()
        main_window.set_focus()
        time.sleep(1)

        self.fun.order_data.update({
            'service_name_form': self.fun.get_element_property_sp(main_window, self.fun.loc.ORDER_NUMBER, "Value"),
            'service_rate_form': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICE_RATE_FORM, "Value"),
            'service_currency_form': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICE_CURRENCY_FORM, "Value"),
            'service_vat_form': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICE_VAT_FORM, "Value"),
            'service_quantity_form': self.fun.get_element_property_sp(main_window, self.fun.loc.FREIGHT_QUANTITY_APPLY, "Value"),
            'service_te_type_form': self.fun.get_element_property(main_window, self.fun.loc.FREIGHT_TE_TYPE1, "Value"),
            'service_te_number_form': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_TE_NUMBER_FORM, "Value"),
            'service_note_form': self.fun.get_element_property_sp(main_window, self.fun.loc.NOTE, "Value"),
            'service_uom_form': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICE_UOM_FORM, "Value"),
        })

        # Редактирование услуги
        self.fun.set_text_field(main_window, self.loc.FREIGHT_QUANTITY_APPLY, "2,1000", timeout=1)
        self.fun.click_element_sp(main_window, self.loc.SERVICE_UOM_FORM)
        self.fun.click_element_sp(main_window, self.loc.SERVICE_M3_FORM)
        self.fun.set_text_field(main_window, self.loc.SERVICE_RATE_FORM, "234", timeout=1)
        self.fun.click_element_sp(main_window, self.loc.SERVICE_CURRENCY_FORM)
        self.fun.click_element(main_window, self.loc.USD, timeout=1)
        self.fun.click_element_sp(main_window, self.loc.SERVICE_VAT_FORM)
        time.sleep(1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        # Создать ТЕ в услуге
        self.fun.click_element_double_sp(main_window, self.fun.loc.SERVICE_TE_NUMBER_FORM)
        self.fun.click_element_double_sp(main_window, self.fun.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_CREATE_TE)
        time.sleep(2)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TE2, timeout=2)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TYPE, timeout=1)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_CREATE_TYPE1)
        self.fun.set_text_field(main_window, self.loc.FREIGHT_CREATE_QUANTITY, 1, timeout=1)
        self.fun.order_data.update({
            'type_te': self.fun.get_element_property_sp(main_window, self.fun.loc.FREIGHT_CREATE_TYPE, "Value"),
            'number_te': self.fun.get_element_property_sp(main_window, self.fun.loc.FREIGHT_CREATE_ORDER, "Value"),
        })
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON)

        # Выставляем созданный ТЕ
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_CREATE_TYPE)
        self.fun.click_element(main_window, self.loc.RECIPIENT_1, timeout=1)
        self.fun.click_element_sp(main_window, self.loc.SERVICE_TE_NUMBER_FORM)
        keyboard.send_keys('{DOWN}')

        self.fun.set_text_field(main_window, self.loc.NOTE, "Редактирование услуги", timeout=2)
        self.fun.click_element_sp(main_window, self.loc.APPLY_BUTTON1)
        self.fun.order_data.update({
            'service_name_form_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.ORDER_NUMBER, "Value"),
            'service_rate_form_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICE_RATE_FORM, "Value"),
            'service_currency_form_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICE_CURRENCY_FORM,
                                                                      "Value"),
            'service_vat_form_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICE_VAT_FORM, "Value"),
            'service_quantity_form_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.FREIGHT_QUANTITY_APPLY,
                                                                      "Value"),
            'service_te_type_form_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.FREIGHT_CREATE_TYPE,
                                                                     "Value"),
            'service_te_number_form_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICE_TE_NUMBER_FORM,
                                                                       "Value"),
            'service_note_form_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.NOTE, "Value"),
            'service_uom_form_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICE_UOM_FORM, "Value"),
        })

        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON)
        time.sleep(1)
        main_window = self.fun.get_main_form()
        main_window.set_focus()

        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON_ORDER)
        time.sleep(1)
        self.fun.order_data.update({
            'service_rate_mod1': self.fun.get_element_property_sp(main_window, self.fun.loc.RATE_LINE1, "Value"),
            'service_currency_mod1': self.fun.get_element_property_sp(main_window, self.fun.loc.CURRENCY_LINE1, "Value"),
            'service_vat_mod1': self.fun.get_element_property_sp(main_window, self.fun.loc.VAT_LINE1, "Value"),
            'service_quantity_mod1': self.fun.get_element_property_sp(main_window, self.fun.loc.QUANTITY_TABLE1,
                                                                     "Value"),
            'service_te_type_mod1': self.fun.get_element_property_sp(main_window, self.fun.loc.TYPE_TE_TABLE1, "Value"),
            'service_te_number_mod1': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICE_TE_NUMBER,
                                                                      "Value"),
            'service_note_mod1': self.fun.get_element_property_sp(main_window, self.fun.loc.NOTE_LINE1, "Value"),
            'service_source_mod1': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICE_SOURCE, "Value"),
            'service_account_mod1': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICE_ACCOUNT, "Value"),
        })

        # Создание услуги в морской перевозке
        self.fun.click_element_sp(main_window, self.loc.TAB_TRANSPORTATION)

        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.fun.loc.TYPE_TRANSPORTATION)
        self.fun.click_element_sp(main_window, self.fun.loc.SEA_TRANSPORTATION)
        self.fun.click_element_sp(main_window, self.fun.loc.OK_BUTTON)

        main_window = self.fun.get_sea_form()
        main_window.set_focus()
        time.sleep(1)

        # 6. Перейти во вкладку Услуги
        self.fun.click_element_sp(main_window, self.fun.loc.TAB_SERVICES)
        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.fun.loc.SERVICES_ADD)
        keyboard.send_keys('Фрахт')
        keyboard.send_keys('{ENTER}')
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.fun.loc.OK_BUTTON)
        time.sleep(1)

        self.fun.order_data.update({
            'sea_service_type': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_LINE1, "Value"),
            'sea_service_source': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_SOURCE, "Value")
        })
        # Закрываем морскую перевозку
        self.fun.click_element_sp(main_window, self.fun.loc.SAVE_BUTTON)
        time.sleep(1)

        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # Создание услуги в автоперевозке
        # Создаём автоперевозку
        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)
        self.fun.click_element(main_window, self.fun.loc.TYPE_TRANSPORTATION, timeout=1)
        self.fun.click_element(main_window, self.fun.loc.AUTO_TRANSPORTATION, timeout=1)
        keyboard.send_keys('{ENTER}')  # нажать на ОК работает если есть фокус на кнопке, могут быть проблемы

        # 5. Переключится на форму автоперевозки
        main_window = self.fun.get_auto_form()
        main_window.set_focus()
        time.sleep(2)
        # 6. Перейти во вкладку Услуги
        self.fun.click_element(main_window, self.fun.loc.TAB_SERVICES, timeout=1)
        time.sleep(4)
        self.fun.click_element(main_window, self.fun.loc.CREATE_BUTTON, timeout=2)
        self.fun.click_element_sp(main_window, self.fun.loc.SERVICES_ADD)
        keyboard.send_keys('КТС')
        keyboard.send_keys('{ENTER}')
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.fun.loc.OK_BUTTON)
        time.sleep(1)
        self.fun.order_data.update({
            'auto_service_type': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_LINE1, "Value"),
            'auto_service_source': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_SOURCE, "Value")
        })
        # Закрываем автоперевозку
        self.fun.click_element_sp(main_window, self.fun.loc.SAVE_BUTTON)
        time.sleep(1)

        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # Создание услуги в ЖД-перевозке
        # Создаём ЖД-перевозку
        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.fun.loc.TYPE_TRANSPORTATION)
        self.fun.click_element_sp(main_window, self.fun.loc.JD_TRANSPORTATION)
        keyboard.send_keys('{ENTER}')  # нажать на ОК работает если есть фокус на кнопке, могут быть проблемы

        # 5. Переключится на форму автоперевозки
        main_window = self.fun.get_jd_form()
        main_window.set_focus()
        time.sleep(1)
        # 6. Перейти во вкладку Услуги
        self.fun.click_element_sp(main_window, self.fun.loc.TAB_SERVICES)
        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.fun.loc.SERVICES_ADD)
        keyboard.send_keys('Услуги по сопро')
        keyboard.send_keys('{ENTER}')
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.fun.loc.OK_BUTTON)
        time.sleep(1)
        self.fun.order_data.update({
            'jd_service_type': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_LINE1, "Value"),
            'jd_service_source': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_SOURCE, "Value")
        })
        # Закрываем ЖД-перевозку
        self.fun.click_element_sp(main_window, self.fun.loc.SAVE_BUTTON)
        time.sleep(1)

        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # Создание услуги в авиаперевозке
        # Создаём авиаперевозку
        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.fun.loc.TYPE_TRANSPORTATION)
        self.fun.click_element_sp(main_window, self.fun.loc.AVIA_TRANSPORTATION)
        keyboard.send_keys('{ENTER}')  # нажать на ОК работает если есть фокус на кнопке, могут быть проблемы

        # 5. Переключится на форму авиаперевозки
        main_window = self.fun.get_avia_form()
        main_window.set_focus()
        time.sleep(1)
        # 6. Перейти во вкладку Услуги
        self.fun.click_element_sp(main_window, self.fun.loc.TAB_SERVICES)
        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.fun.loc.SERVICES_ADD)
        keyboard.send_keys('Безо')
        keyboard.send_keys('{ENTER}')
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.fun.loc.OK_BUTTON)
        time.sleep(1)
        self.fun.order_data.update({
            'avia_service_type': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_LINE1, "Value"),
            'avia_service_source': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_SOURCE, "Value")
        })
        # Закрываем авиаперевозку
        self.fun.click_element_sp(main_window, self.fun.loc.SAVE_BUTTON)
        time.sleep(1)

        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # Проверяем номера
        self.fun.order_data.update({
            'sea_number': self.fun.get_element_property(main_window, self.fun.loc.TRANSPORTATION_NUMBER1, "Value"),
            'auto_number': self.fun.get_element_property(main_window, self.fun.loc.TRANSPORTATION_NUMBER2, "Value"),
            'jd_number': self.fun.get_element_property(main_window, self.fun.loc.TRANSPORTATION_NUMBER3, "Value"),
            'avia_number': self.fun.get_element_property(main_window, self.fun.loc.TRANSPORTATION_NUMBER4, "Value"),

        })

        # Создание услуги в экспедирование
        # 7. Перейти во вкладку
        self.fun.click_element_sp(main_window, self.fun.loc.TAB_FORWARDING)

        # 8. Создать Экспедирование
        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)
        self.fun.order_data.update({
            'forwarding_dialog_type': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_TYPE_DIALOG,
                                                                    "Value"),
            'forwarding_dialog_otv': self.fun.get_element_property(main_window, self.fun.loc.RESPONSIBLE_COMBO,
                                                                   "Value"),
        })

        self.fun.click_element_sp(main_window, self.fun.loc.OK_BUTTON)

        # 9. Переключится на форму Экспедирования
        main_window = self.fun.get_forwarding_form()
        main_window.set_focus()
        time.sleep(1)

        # 6. Перейти во вкладку Услуги
        self.fun.click_element_sp(main_window, self.fun.loc.TAB_SERVICES)
        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.fun.loc.SERVICES_ADD)
        keyboard.send_keys('Страх')
        keyboard.send_keys('{ENTER}')
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.fun.loc.OK_BUTTON)
        time.sleep(2)
        self.fun.order_data.update({
            'for_service_type': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_LINE1, "Value"),
            'for_service_source': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_SOURCE, "Value")
        })
        # Закрываем Экспедирования
        self.fun.click_element_sp(main_window, self.fun.loc.SAVE_BUTTON)
        time.sleep(1)

        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)
        self.fun.order_data.update({
            'for_number': self.fun.get_element_property(main_window, self.fun.loc.FORWARDING_NUMBER, "Value"),
        })

        self.fun.click_element_sp(main_window, self.fun.loc.TAB_SERVICES)
        time.sleep(2)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON_ORDER)
        time.sleep(2)
        self.fun.order_data.update({
            'service_sea': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_LINE6, "Value"),
            'service_auto': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_LINE2, "Value"),
            'service_jd': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_LINE5, "Value"),
            'service_avia': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_LINE4, "Value"),
            'service_for': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_LINE3, "Value"),


            'source_sea': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_SOURCE3, "Value"),
            'source_auto': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_SOURCE6, "Value"),
            'source_jd': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_SOURCE4, "Value"),
            'source_avia': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_SOURCE, "Value"),
            'source_for': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_SOURCE5, "Value"),
        })

        # В заказе создать ИС
        self.fun.click_element_sp(main_window, self.fun.loc.TAB_CHECK)

        # 7 Создать Исходящий счет
        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)

        # 8. Переключение на форму ИС
        main_window = self.fun.get_check_form()
        main_window.set_focus()

        self.fun.click_element_sp(main_window, self.loc.TAB_SERVICES)
        self.fun.click_element_sp(main_window, self.loc.ADD_FROM_ORDER_BUTTON)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.FILE_SELECT1)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.FILE_SELECT1)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.FILE_SELECT1)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON)
        time.sleep(1)
        self.fun.order_data.update({
            'service_is_1form': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_LINE1, "Value"),
            'service_is_2form': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_LINE2, "Value"),
            'service_is_3form': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_LINE3, "Value"),
        })
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON1)
        time.sleep(1)


        # 11. Переключить на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)
        time.sleep(2)
        self.fun.click_element_double(main_window, self.loc.VS_CREATE_ORDER, timeout=2)
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)

        # 7 Переключение на форму ВС
        main_window = self.fun.get_check_vs_form()
        main_window.set_focus()

        self.fun.click_element_sp(main_window, self.loc.TAB_SERVICES)
        self.fun.click_element_sp(main_window, self.loc.ADD_FROM_ORDER_BUTTON)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.FILE_SELECT1)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.FILE_SELECT1)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.FILE_SELECT1)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON)
        time.sleep(1)
        self.fun.order_data.update({
            'service_vs_1form': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_LINE1, "Value"),
            'service_vs_2form': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_LINE2, "Value"),
            'service_vs_3form': self.fun.get_element_property(main_window, self.fun.loc.SERVICE_LINE2, "Value"),
        })
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON1)
        time.sleep(1)

        # Переключить на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.TAB_SERVICES)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON_ORDER)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.TABLE_DELETE)
        time.sleep(1)
        self.fun.order_data.update({
            'service_del_text': self.fun.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),

        })
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        time.sleep(10)


        return self.fun.order_data

    def close(self):
        """Завершение работы приложения"""
        self.fun.app.kill(soft=True)
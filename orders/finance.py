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

    def finance(self):
        # 1. Запуск приложения
        self.fun.start_application()
        time.sleep(3)

        # 3.
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(1)

        self.fun.click_element_sp(main_window, self.loc.FINANCE)
        time.sleep(3)
        self.fun.click_element_sp(main_window, self.loc.OUTGOING_INVOICES)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.ADD_BUTTON)
        time.sleep(1)
        main_window = self.fun.get_check_form()
        main_window.set_focus()

        # Редактирование формы
        self.fun.click_element_sp(main_window, self.loc.IS_SUPPLIER)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.GTD_CLIENT)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        text = self.fun.get_element_value(main_window, self.loc.GTD_CLIENT, timeout=1)

        self.fun.click_element_sp(main_window, self.loc.GTD_ORDER)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_ORDER_CREATE)
        self.fun.click_element_sp(main_window, self.loc.ORDER_TYPE_COMBO)
        self.fun.click_element_sp(main_window, self.loc.LOGISTICS_ITEM)
        self.fun.click_element_sp(main_window, self.loc.CUSTOMER_COMBO)
        keyboard.send_keys(text, with_spaces=True)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.APPLY_BUTTON)
        time.sleep(2)

        # Добавить услугу
        self.fun.click_element_sp(main_window, self.loc.TAB_SERVICES)
        self.fun.click_element_sp(main_window, self.loc.ADD_BUTTON)
        time.sleep(1)
        main_window = self.fun.get_services_form()
        main_window.set_focus()
        self.fun.click_element_sp(main_window, self.loc.SERVICES_SERVICES)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.set_text_field(main_window, self.loc.SERVICES_BET, "100", timeout=1)
        self.fun.click_element_sp(main_window, self.loc.SERVICES_CURRENCY)
        self.fun.click_element_sp(main_window, self.loc.USD)
        self.fun.set_text_field(main_window, self.loc.NOTE_SERVICES, "Авто тесты Исходящий счет связи", timeout=1)
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON1)
        time.sleep(1)

        main_window = self.fun.get_check_form()
        main_window.set_focus()

        # Связываем с Вх. платежом
        self.fun.click_element_sp(main_window, self.loc.INCOMING_PAYMENTS)
        self.fun.click_element_sp(main_window, self.loc.CONNECT_VP)
        time.sleep(2)
        self.fun.click_element_sp(main_window, self.loc.SERVICES_OPTIONS)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.ADD_SERVICES)
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON1)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.TAB_SERVICES)
        self.fun.check_element_disappeared(main_window, self.loc.ADD_BUTTON)
        self.fun.check_element_disappeared(main_window, self.loc.ADD_FROM_ORDER_BUTTON)
        self.fun.check_element_disappeared(main_window, self.loc.QUICK_CREATE_MENU)

        # Связываем с Вх. переводы
        self.fun.click_element_sp(main_window, self.loc.INCOMING_TRANSFERS)
        self.fun.click_element_sp(main_window, self.loc.CONNECT_TRANSFERS)
        time.sleep(2)
        self.fun.click_element_sp(main_window, self.loc.SERVICES_OPTIONS)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')
        time.sleep(1)
        self.fun.click_element(main_window, self.loc.EXPAND, timeout=1)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.ADD_SERVICES)
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON1)
        time.sleep(1)

        # Связываем с Вх. счета
        self.fun.click_element_sp(main_window, self.loc.INCOMING_INVOICES)
        self.fun.click_element_sp(main_window, self.loc.CONNECT_INVOICES)
        time.sleep(2)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.ADD_SERVICES)
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON1)

        time.sleep(1)

        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON1)
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON1)

        time.sleep(10)

        return self.fun.order_data

    def close(self):
        """Завершение работы приложения"""
        self.fun.app.kill(soft=True)
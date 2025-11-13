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

    def order_del(self):
        # 1. Запуск приложения
        self.fun.start_application()
        time.sleep(2)

        # 2. Переход в раздел Заказы
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(2)
        self.fun.click_element(main_window, self.fun.loc.ORDERS_TAB, timeout=3)
        time.sleep(6)

        # 3. Выделение 10 заказа с сущностью
        self.fun.order_data = {
            'order8': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_ORDER_NUMBER8, "Value"),
            'order9': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_ORDER_NUMBER9, "Value"),
            'order10': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_ORDER_NUMBER10, "Value"),
        }
        self.fun.select_range_with_shift(main_window, self.fun.loc.TABLE_ORDER_NUMBER, self.fun.loc.TABLE_ORDER_NUMBER10)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.fun.loc.TABLE_DELETE)
        self.fun.click_element_sp(main_window, self.fun.loc.YES_BUTTON)
        self.fun.order_data.update({
            'del_window': self.fun.get_element_property(main_window, self.fun.loc.DEL_WINDOW, "Name"),
        })

        self.fun.click_element_sp(main_window, self.fun.loc.DEL_WINDOW_BUTTON)

        # 4. Создание нового заказа
        self.fun.click_element_sp(main_window, self.fun.loc.ADD_BUTTON)
        time.sleep(1)

        # 5. Заполнение формы заказа
        self.fun.click_element_sp(main_window, self.fun.loc.ORDER_TYPE_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.LOGISTICS_ITEM)
        self.fun.click_element_sp(main_window, self.fun.loc.CUSTOMER_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.CUSTOMER_ITEM)
        self.fun.click_element_sp(main_window, self.fun.loc.OK_BUTTON)
        time.sleep(1)
        main_window = self.fun.get_main_form()
        main_window.set_focus()

        # 6. В заказе прикрепить фаил
        self.fun.click_element_sp(main_window, self.fun.loc.TAB_FILE)
        self.fun.click_element_sp(main_window, self.fun.loc.ADD_BUTTON)
        self.fun.click_element_sp(main_window, self.fun.loc.ADD_FILE)
        self.fun.click_element(main_window, self.fun.loc.TEST_FILE, timeout=1)
        self.fun.click_element_sp(main_window, self.fun.loc.OPEN_BUTTON1)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.fun.loc.ADD_BUTTON)
        time.sleep(1)
        self.fun.order_data.update({
            'add_file': self.fun.get_element_property_sp(main_window, self.loc.FILE_1, "Value"),
        })
        self.fun.click_element_sp(main_window, self.fun.loc.FILE_1)

        # 7. Удалить заказ
        self.fun.click_element_sp(main_window, self.loc.OTHER_ACTIONS)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')
        self.fun.click_element_sp(main_window, self.loc.YES_BUTTON)
        self.fun.order_data.update({
            'del_window_file': self.fun.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 8. Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.TABLE_ORDER_NUMBER)
        self.fun.click_element_sp(main_window, self.loc.TABLE_DELETE)
        self.fun.click_element_sp(main_window, self.loc.YES_BUTTON)
        self.fun.order_data.update({
            'del_window_file1': self.fun.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 9. Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_form()
        main_window.set_focus()

        # 10. Удалить Фаил
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.TABLE_DELETE)
        self.fun.click_element_sp(main_window, self.loc.YES_BUTTON)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON1)
        self.fun.order_data.update({
            'del_file': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })
        # 11. В заказе создать Услугу
        self.fun.click_element_sp(main_window, self.fun.loc.TAB_SERVICES)

        # Создать Услугу
        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.SERVICES_ADD)
        self.fun.click_element_sp(main_window, self.loc.DELIVERY_CONDITION_0)
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON_ORDER)

        # Удалить заказ
        self.fun.click_element_sp(main_window, self.loc.OTHER_ACTIONS)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')
        self.fun.click_element_sp(main_window, self.loc.YES_BUTTON)
        self.fun.order_data.update({
            'del_window_services': self.fun.get_element_property_sp(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.TABLE_ORDER_NUMBER)
        self.fun.click_element_sp(main_window, self.loc.TABLE_DELETE)
        self.fun.click_element_sp(main_window, self.loc.YES_BUTTON)
        self.fun.order_data.update({
            'del_window_services1': self.fun.get_element_property_sp(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_form()
        main_window.set_focus()

        # 12. Удалить ИС
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.TABLE_DELETE)
        self.fun.click_element_sp(main_window, self.loc.YES_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON_ORDER)
        self.fun.order_data.update({
            'del_services': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # В заказе создать ИС
        self.fun.click_element_sp(main_window, self.fun.loc.TAB_CHECK)

        # Создать Исходящий счет и выставить покупателя
        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)

        # 8. Переключение на форму ИС
        main_window = self.fun.get_check_form()
        main_window.set_focus()
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON1)

        # Переключить на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON_ORDER)

        # Удалить заказ
        self.fun.click_element_sp(main_window, self.loc.OTHER_ACTIONS)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')
        self.fun.click_element_sp(main_window, self.loc.YES_BUTTON)
        self.fun.order_data.update({
            'del_window_is': self.fun.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.TABLE_ORDER_NUMBER)
        self.fun.click_element_sp(main_window, self.loc.TABLE_DELETE)
        self.fun.click_element_sp(main_window, self.loc.YES_BUTTON)
        self.fun.order_data.update({
            'del_window_is1': self.fun.get_element_property_sp(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_form()
        main_window.set_focus()

        # Удалить ИС
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.TABLE_DELETE)
        self.fun.click_element_sp(main_window, self.loc.YES_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON_ORDER)
        self.fun.order_data.update({
            'del_is': self.fun.get_element_property(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # 13 Создать Входящий счет
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)
        time.sleep(1)
        self.fun.click_element_double(main_window, self.loc.VS_CREATE_ORDER, timeout=1)
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)

        # Переключение на форму ВС
        main_window = self.fun.get_check_vs_form()
        main_window.set_focus()
        self.fun.click_element(main_window, self.loc.OK_BUTTON1)
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON_ORDER)

        # Удалить заказ
        self.fun.click_element_sp(main_window, self.loc.OTHER_ACTIONS)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')
        self.fun.click_element_sp(main_window, self.loc.YES_BUTTON)
        self.fun.order_data.update({
            'del_window_vs': self.fun.get_element_property_sp(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.TABLE_ORDER_NUMBER)
        self.fun.click_element_sp(main_window, self.loc.TABLE_DELETE)
        self.fun.click_element_sp(main_window, self.loc.YES_BUTTON)
        self.fun.order_data.update({
            'del_window_vs1': self.fun.get_element_property_sp(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_form()
        main_window.set_focus()

        # Удалить
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.TABLE_DELETE)
        self.fun.click_element_sp(main_window, self.loc.YES_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON_ORDER)
        self.fun.order_data.update({
            'del_vs': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # 14. Создать Исходящего платежа и выставить покупателя
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)
        time.sleep(1)
        self.fun.click_element_double(main_window, self.loc.IP_CREATE_ORDER, timeout=1)
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)
        main_window = self.fun.get_check_ip_form()
        main_window.set_focus()
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON1)

        # Переключить на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        self.fun.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=1)

        # Удалить заказ
        self.fun.click_element(main_window, self.loc.OTHER_ACTIONS, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.order_data.update({
            'del_window_ip': self.fun.get_element_property_sp(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.TABLE_ORDER_NUMBER)
        self.fun.click_element_sp(main_window, self.loc.TABLE_DELETE)
        self.fun.click_element_sp(main_window, self.loc.YES_BUTTON)
        self.fun.order_data.update({
            'del_window_ip1': self.fun.get_element_property_sp(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_form()
        main_window.set_focus()

        # Удалить
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.TABLE_DELETE)
        self.fun.click_element_sp(main_window, self.loc.YES_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON_ORDER)
        self.fun.order_data.update({
            'del_ip': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # 15. Создать Входящий платеж
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)
        time.sleep(1)
        self.fun.click_element_double(main_window, self.loc.VP_CREATE_ORDER)
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)
        main_window = self.fun.get_check_vp_form()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element(main_window, self.loc.OK_BUTTON1, timeout=1)

        # Переключить на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=1)

        # Удалить заказ
        self.fun.click_element_sp(main_window, self.loc.OTHER_ACTIONS)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')
        self.fun.click_element_sp(main_window, self.loc.YES_BUTTON)
        self.fun.order_data.update({
            'del_window_vp': self.fun.get_element_property_sp(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.TABLE_ORDER_NUMBER)
        self.fun.click_element_sp(main_window, self.loc.TABLE_DELETE)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.order_data.update({
            'del_window_vp1': self.fun.get_element_property_sp(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_form()
        main_window.set_focus()

        # Удалить
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.TABLE_DELETE)
        self.fun.click_element_sp(main_window, self.loc.YES_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON_ORDER)
        self.fun.order_data.update({
            'del_vp': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # 16. В заказе создать Морская перевозка
        self.fun.click_element(main_window, self.loc.TAB_TRANSPORTATION, timeout=3)

        # 8. Создать морскую перевозку
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.TYPE_TRANSPORTATION)
        self.fun.click_element_sp(main_window, self.loc.SEA_TRANSPORTATION)
        keyboard.send_keys('{ENTER}')  # нажать на ОК работает если есть фокус на кнопке, могут быть проблемы
        main_window = self.fun.get_sea_form()
        main_window.set_focus()
        time.sleep(1)

        # Закрываем морскую перевозку
        self.fun.click_element_sp(main_window, self.loc.SAVE_BUTTON)
        time.sleep(1)
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # Удалить заказ
        self.fun.click_element_sp(main_window, self.loc.OTHER_ACTIONS)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        self.fun.click_element_sp(main_window, self.loc.YES_BUTTON)
        self.fun.order_data.update({
            'del_window_sea': self.fun.get_element_property_sp(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.TABLE_ORDER_NUMBER)
        self.fun.click_element_sp(main_window, self.loc.TABLE_DELETE)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.order_data.update({
            'del_window_sea1': self.fun.get_element_property_sp(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_form()
        main_window.set_focus()

        # Удаляем морскую перевозку
        self.fun.click_element_sp(main_window, self.loc.LINE_TRANSPORTATION)
        self.fun.click_element_sp(main_window, self.loc.DEL_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.YES_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON_ORDER)
        self.fun.order_data.update({
            'del_sea': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # 17. Создаем автоперевозку
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.TYPE_TRANSPORTATION)
        self.fun.click_element_sp(main_window, self.loc.AUTO_TRANSPORTATION)
        keyboard.send_keys('{ENTER}')  # нажать на ОК работает если есть фокус на кнопке, могут быть проблемы
        main_window = self.fun.get_auto_form()
        main_window.set_focus()
        time.sleep(1)

        # Закрываем морскую перевозку
        self.fun.click_element(main_window, self.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 12. Удалить заказ
        self.fun.click_element_sp(main_window, self.loc.OTHER_ACTIONS)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')
        time.sleep(2)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=2)
        self.fun.order_data.update({
            'del_window_auto': self.fun.get_element_property_sp(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.TABLE_ORDER_NUMBER)
        self.fun.click_element_sp(main_window, self.loc.TABLE_DELETE)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.order_data.update({
            'del_window_auto1': self.fun.get_element_property_sp(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_form()
        main_window.set_focus()

        # Удаляем автоперевозку
        self.fun.click_element(main_window, self.loc.LINE_TRANSPORTATION, timeout=2)
        self.fun.click_element(main_window, self.loc.DEL_BUTTON, timeout=2)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=2)
        self.fun.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=2)
        self.fun.order_data.update({
            'del_auto': self.fun.get_element_property(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # 18. Создаем ЖД-перевозку
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.TYPE_TRANSPORTATION)
        self.fun.click_element_sp(main_window, self.loc.JD_TRANSPORTATION)
        keyboard.send_keys('{ENTER}')  # нажать на ОК работает если есть фокус на кнопке, могут быть проблемы
        main_window = self.fun.get_jd_form()
        main_window.set_focus()
        time.sleep(1)

        # Закрываем ЖД-перевозку
        self.fun.click_element(main_window, self.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # Удалить заказ с ЖД-перевозкой
        self.fun.click_element_sp(main_window, self.loc.OTHER_ACTIONS)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.order_data.update({
            'del_window_jd': self.fun.get_element_property_sp(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # Окно удаления заказа с ЖД-перевозкой
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.TABLE_ORDER_NUMBER)
        self.fun.click_element_sp(main_window, self.loc.TABLE_DELETE)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.order_data.update({
            'del_window_jd1': self.fun.get_element_property_sp(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # Окно удаления заказа с ЖД-перевозкой
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_form()
        main_window.set_focus()

        # Удаляем ЖД-перевозку
        self.fun.click_element_sp(main_window, self.loc.LINE_TRANSPORTATION)
        self.fun.click_element_sp(main_window, self.loc.DEL_BUTTON)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON_ORDER)
        self.fun.order_data.update({
            'del_jd': self.fun.get_element_property(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # 19. Создаем Авиаперевозку
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.TYPE_TRANSPORTATION)
        self.fun.click_element_sp(main_window, self.loc.AVIA_TRANSPORTATION)
        keyboard.send_keys('{ENTER}')  # нажать на ОК работает если есть фокус на кнопке, могут быть проблемы
        main_window = self.fun.get_avia_form()
        main_window.set_focus()
        time.sleep(1)

        # Закрываем Авиаперевозку
        self.fun.click_element(main_window, self.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # Удалить заказ с Авиаперевозкой
        self.fun.click_element_sp(main_window, self.loc.OTHER_ACTIONS)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.order_data.update({
            'del_window_avia': self.fun.get_element_property_sp(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # Окно удаления заказа с Авиаперевозкой
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.TABLE_ORDER_NUMBER)
        self.fun.click_element_sp(main_window, self.loc.TABLE_DELETE)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.order_data.update({
            'del_window_avia1': self.fun.get_element_property_sp(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # Окно удаления заказа с Авиаперевозкой
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_form()
        main_window.set_focus()

        # Удаляем Авиаперевозку
        self.fun.click_element_sp(main_window, self.loc.LINE_TRANSPORTATION)
        self.fun.click_element_sp(main_window, self.loc.DEL_BUTTON)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON_ORDER)
        self.fun.order_data.update({
            'del_avia': self.fun.get_element_property(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # 20. Удаление груза
        # Перейти во вкладку
        self.fun.click_element(main_window, self.loc.TAB_FREIGHT, timeout=2)

        # 18 Создать Bulkership
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TE)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_CREATE_TE1)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_CREATE_TYPE)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_CREATE_TYPE1)
        self.fun.set_text_field(main_window, self.loc.FREIGHT_CREATE_QUANTITY, 1, timeout=1)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_CREATE_UOM)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_CREATE_UOM1)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)
        time.sleep(1)

        # Удалить заказ
        self.fun.click_element_sp(main_window, self.loc.OTHER_ACTIONS)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.order_data.update({
            'del_window_bul': self.fun.get_element_property_sp(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)

        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.TABLE_ORDER_NUMBER)
        self.fun.click_element_sp(main_window, self.loc.TABLE_DELETE)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.order_data.update({
            'del_window_bul1': self.fun.get_element_property_sp(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_form()
        main_window.set_focus()

        # Удалить Bulkership
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_ITEM)
        self.fun.click_element_sp(main_window, self.loc.DEL_BUTTON)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=2)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON_ORDER)
        self.fun.order_data.update({
            'del_bul': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })
        time.sleep(1)

        # 19. Создать Container
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_CREATE_TE)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TE2, timeout=1)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_CREATE_TYPE)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_CREATE_TYPE1)
        self.fun.set_text_field(main_window, self.loc.FREIGHT_CREATE_QUANTITY, 1, timeout=1)
        time.sleep(1)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

        # Удалить заказ
        self.fun.click_element_sp(main_window, self.loc.OTHER_ACTIONS)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.order_data.update({
            'del_window_con': self.fun.get_element_property_sp(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.TABLE_ORDER_NUMBER)
        self.fun.click_element_sp(main_window, self.loc.TABLE_DELETE)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.order_data.update({
            'del_window_con1': self.fun.get_element_property_sp(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_form()
        main_window.set_focus()

        # Удалить Container
        self.fun.click_element_sp(main_window, self.loc.LINE_TRANSPORTATION)
        self.fun.click_element_sp(main_window, self.loc.DEL_BUTTON)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=2)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON_ORDER)
        self.fun.order_data.update({
            'del_con': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })
        time.sleep(1)

        # В заказе создать ГТД и удалить груз
        # 7. Перейти во вкладку груза
        self.fun.click_element_sp(main_window, self.loc.TAB_FREIGHT)

        # 8 Создать Bulkership
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_CREATE_TE)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_CREATE_TE1)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_CREATE_TYPE)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_CREATE_TYPE1)
        self.fun.set_text_field(main_window, self.loc.FREIGHT_CREATE_QUANTITY, 1, timeout=1)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_CREATE_UOM)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_CREATE_UOM1)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)
        time.sleep(1)

        # 10. Перейти во вкладку Декларирования
        self.fun.click_element_sp(main_window, self.loc.TAB_GTD)
        self.fun.click_element_sp(main_window, self.loc.ADD_BUTTON)
        time.sleep(2)
        main_window = self.fun.get_gtd_form()
        main_window.set_focus()
        time.sleep(1)

        # 12. Прикрепить ТЕ
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.ADD_TE)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON1)

        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 6. Перейти во вкладку груза
        self.fun.click_element_sp(main_window, self.loc.TAB_FREIGHT)

        # 5. Удалить Bulkership
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_ITEM)
        self.fun.click_element_sp(main_window, self.loc.DEL_BUTTON)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=2)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON_ORDER)

        # 10. Перейти во вкладку Декларирования
        self.fun.click_element_sp(main_window, self.loc.TAB_GTD)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON)

        # 12. Удалить заказ
        self.fun.click_element(main_window, self.loc.OTHER_ACTIONS, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.order_data.update({
            'del_window_gtd': self.fun.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 9. Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)

        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.TABLE_ORDER_NUMBER)
        self.fun.click_element_sp(main_window, self.loc.TABLE_DELETE)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.order_data.update({
            'del_window_gtd1': self.fun.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 10. Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_form()
        main_window.set_focus()

        # 12. Удалить ГТД
        self.fun.click_element(main_window, self.loc.TABLE_DELETE, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(main_window, self.loc.REFRESH_BUTTON, timeout=2)
        self.fun.order_data.update({
            'del_gtd': self.fun.get_element_property(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # 7. Создание и удаление Экспедирование
        self.fun.click_element(main_window, self.loc.TAB_FORWARDING, timeout=3)

        # 8. Создать Экспедирование
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

        # 9. Переключится на форму Экспедирования
        main_window = self.fun.get_forwarding_form()
        main_window.set_focus()
        time.sleep(1)

        # 11. Закрываем Экспедирование
        self.fun.click_element(main_window, self.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 12. Удалить заказ
        self.fun.click_element_sp(main_window, self.loc.OTHER_ACTIONS)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=2)
        self.fun.order_data.update({
            'del_window_exp': self.fun.get_element_property_sp(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 9. Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.TABLE_ORDER_NUMBER)
        self.fun.click_element_sp(main_window, self.loc.TABLE_DELETE)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.order_data.update({
            'del_window_exp1': self.fun.get_element_property_sp(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 10. Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)
        main_window = self.fun.get_main_form()
        main_window.set_focus()

        # 23. Удаляем Экспедирование
        self.fun.click_element_sp(main_window, self.loc.LINE_TRANSPORTATION)
        self.fun.click_element_sp(main_window, self.loc.DEL_BUTTON)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=2)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON_ORDER)
        self.fun.order_data.update({
            'del_exp': self.fun.get_element_property_sp(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })
        self.fun.click_element(main_window, self.loc.SAVE_BUTTON, timeout=2)
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(4)

        # 4. Создаем 1 заказ
        # 5. Создание нового заказа
        self.fun.click_element_sp(main_window, self.fun.loc.ADD_BUTTON)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.fun.loc.ORDER_TYPE_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.LOGISTICS_ITEM)
        self.fun.click_element_sp(main_window, self.fun.loc.CUSTOMER_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.CUSTOMER_ITEM)
        self.fun.click_element_sp(main_window, self.fun.loc.OK_BUTTON)
        time.sleep(1)
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        self.fun.click_element(main_window, self.fun.loc.SAVE_BUTTON, timeout=1)
        time.sleep(1)
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        self.fun.click_element(main_window, self.fun.loc.REFRESH_BUTTON, timeout=1)

        self.fun.order_data.update({
            'delete_order': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_ORDER_NUMBER, "Value")
        })

        # 5. Удаление 1 заказа
        self.fun.click_element_sp(main_window, self.fun.loc.TABLE_ORDER_NUMBER)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.fun.loc.TABLE_DELETE)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.click_element_sp(main_window, self.fun.loc.REFRESH_BUTTON)

        # 7. Cравнение изменений
        self.fun.order_data.update({
            'table_order': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_ORDER_NUMBER, "Value")
        })

        # 8. Создаем 2 заказа
        # 5. Создание нового заказа
        self.fun.click_element_sp(main_window, self.fun.loc.ADD_BUTTON)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.fun.loc.ORDER_TYPE_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.LOGISTICS_ITEM)
        self.fun.click_element_sp(main_window, self.fun.loc.CUSTOMER_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.CUSTOMER_ITEM)
        self.fun.click_element_sp(main_window, self.fun.loc.OK_BUTTON)
        time.sleep(1)
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        self.fun.click_element(main_window, self.fun.loc.SAVE_BUTTON, timeout=1)
        time.sleep(1)
        main_window = self.fun.get_main_window()
        main_window.set_focus()

        # 22. Создание нового заказа Другие услуги
        self.fun.click_element_sp(main_window, self.fun.loc.ADD_BUTTON)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.fun.loc.ORDER_TYPE_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.LOGISTICS_ITEM_DR)
        self.fun.click_element_sp(main_window, self.fun.loc.CUSTOMER_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.CUSTOMER_ITEM)
        time.sleep(1)
        self.fun.click_element(main_window, self.fun.loc.OK_BUTTON, timeout=1)
        time.sleep(1)
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        self.fun.click_element(main_window, self.fun.loc.SAVE_BUTTON, timeout=1)
        time.sleep(1)
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        self.fun.click_element(main_window, self.fun.loc.REFRESH_BUTTON, timeout=1)
        self.fun.order_data.update({
            'table_order_del1': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_ORDER_NUMBER, "Value"),
            'table_order_del2': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_ORDER_NUMBER2, "Value")
        })

        # Выбор 2х заказов и удаление их
        self.fun.select_two_elements_with_ctrl(main_window, self.fun.loc.RECIPIENT_1, self.fun.loc.RECIPIENT_2)
        self.fun.click_element_sp(main_window, self.fun.loc.TABLE_DELETE)

        # Обновить таблицу
        self.fun.click_element_sp(main_window, self.fun.loc.REFRESH_BUTTON)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)

        # Cравнение изменений
        self.fun.order_data.update({
            'table_order_1': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_ORDER_NUMBER, "Value"),
            'table_order_2': self.fun.get_element_property_sp(main_window, self.fun.loc.TABLE_ORDER_NUMBER2, "Value")
        })
        self.fun.click_element(main_window, self.fun.loc.REFRESH_BUTTON, timeout=1)
        return self.fun.order_data

    def close(self):
        """Завершение работы приложения"""
        self.app.kill(soft=True)
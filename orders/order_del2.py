from pywinauto import Application, keyboard
from locators.locators import LocOrders
import time
import subprocess
import psutil


class WinAISTApp:
    def __init__(self):
        self.app = Application(backend='uia')
        self.loc = LocOrders()
        self.order_data = {}  # Для хранения данных заказа
        self.process = None
        self.child_pid = None

    def start_application(self):
        """Запускает WinAIST и подключается к дочернему процессу с окнами"""
        # Запуск приложения через subprocess, чтобы получить родительский PID
        self.process = subprocess.Popen(r'C:\AIST\WinAIST.exe')
        time.sleep(20)  # Ждём, пока окна загрузятся

        # Получаем дочерние процессы
        parent = psutil.Process(self.process.pid)
        children = parent.children(recursive=True)

        if not children:
            raise RuntimeError("Дочерние процессы не найдены")

        # Подключаемся к первому дочернему процессу (где окна)
        self.child_pid = children[0].pid
        self.app.connect(process=self.child_pid)

        # Получаем стартовое окно
        window = self.app.window(**self.loc.STARTUP_WINDOW)
        window.wait('visible', timeout=30)
        window.set_focus()

        return window

    def get_main_window(self):
        """Получение главного окна"""
        return self.app.window(**self.loc.MAIN_WINDOW)

    def get_main_form(self):
        """Получение главного окна"""
        return self.app.window(**self.loc.ORDER_FORM)

    def get_sea_form(self):
        """Получение главного окна"""
        return self.app.window(**self.loc.SEA_FORM)

    def get_auto_form(self):
        """Получение главного окна"""
        return self.app.window(**self.loc.AUTO_FORM)

    def get_forwarding_form(self):
        """Получение главного окна"""
        return self.app.window(**self.loc.FORWARDING_FROM)

    def get_freight_form(self):
        """Получение главного окна"""
        return self.app.window(**self.loc.FREIGHT_FROM)

    def get_gtd_form(self):
        """Получение главного окна"""
        return self.app.window(**self.loc.GTD_FROM)

    def get_check_form(self):
        """Получение главного окна"""
        return self.app.window(**self.loc.CHECK_FROM)

    def get_check_vs_form(self):
        """Получение главного окна"""
        return self.app.window(**self.loc.CHECK_FROM_VS)

    def get_check_ip_form(self):
        """Получение главного окна"""
        return self.app.window(**self.loc.CHECK_FROM_IP)

    def get_check_vp_form(self):
        """Получение главного окна"""
        return self.app.window(**self.loc.CHECK_FROM_VP)

    def click_element(self, window, locator, timeout=5):
        """Клик по элементу с ожиданием"""
        element = window.child_window(**locator)
        element.wait('visible', timeout=timeout)
        element.click_input()
        return element

    def click_element_double(self, window, locator, timeout=5):
        """Клик по элементу с ожиданием"""
        element = window.child_window(**locator)
        element.wait('visible', timeout=timeout)
        element.click_input(double=True)
        return element

    def select_two_elements_with_ctrl(self, window, locator1, locator2, timeout=5):
        # Первый элемент
        el1_spec = window.child_window(**locator1)
        el1_spec.wait('visible', timeout=timeout)
        el1 = el1_spec.wrapper_object()

        # Второй элемент
        el2_spec = window.child_window(**locator2)
        el2_spec.wait('visible', timeout=timeout)
        el2 = el2_spec.wrapper_object()

        # Клик по первому элементу
        el1.click_input()

        # Зажимаем Ctrl и кликаем по второму элементу
        keyboard.send_keys('{VK_CONTROL down}')
        el2.click_input()
        keyboard.send_keys('{VK_CONTROL up}')

        return [el1, el2]

    def select_range_with_shift(self, window, first_locator, last_locator, timeout=5):
        # Клик по первому элементу
        first_el_spec = window.child_window(**first_locator)
        first_el_spec.wait('visible', timeout=timeout)
        first_el = first_el_spec.wrapper_object()
        first_el.click_input()

        # Зажать Shift и клик по последнему элементу
        keyboard.send_keys('{VK_SHIFT down}')
        try:
            last_el_spec = window.child_window(**last_locator)
            last_el_spec.wait('visible', timeout=timeout)
            last_el = last_el_spec.wrapper_object()
            last_el.click_input()
        finally:
            keyboard.send_keys('{VK_SHIFT up}')

        return [first_el, last_el]

    def type_keys(self, window, locator, timeout=1):
        """Клик по элементу с ожиданием"""
        element = window.child_window(**locator)
        element.wait('visible', timeout=timeout)
        element.type_keys("{DOWN}")
        return element

    def set_text_field(self, window, locator, text, timeout=1):
        """Устанавливает текст в текстовое поле"""
        element = window.child_window(**locator)
        element.wait('visible enabled ready', timeout=timeout)
        wrapper = element.wrapper_object()
        wrapper.set_text(str(text))
        return wrapper

    def get_element_property(self, window, locator, property_name, timeout=3):
        """Получение свойства элемента"""
        element = window.child_window(**locator)
        element.wait('visible', timeout=timeout)
        return element.legacy_properties()[property_name]

    def order_del2(self):
        # 1. Запуск приложения
        startup_window = self.start_application()
        startup_window.set_focus()

        # 2. Нажатие кнопки Запуск
        self.click_element(startup_window, self.loc.STAGE_EF, timeout=1)
        self.click_element(startup_window, self.loc.START_BUTTON, timeout=1)
        time.sleep(15)

        # 3. Переход в раздел Заказы
        main_window = self.get_main_window()
        main_window.set_focus()
        time.sleep(3)
        self.click_element(main_window, self.loc.ORDERS_TAB, timeout=3)
        time.sleep(4)

        # 4. Выделение 10 заказа с сущностью
        self.order_data = {
            'order8': self.get_element_property(main_window, self.loc.TABLE_ORDER_NUMBER8, "Value"),
            'order9': self.get_element_property(main_window, self.loc.TABLE_ORDER_NUMBER9, "Value"),
            'order10': self.get_element_property(main_window, self.loc.TABLE_ORDER_NUMBER10, "Value"),
        }
        self.select_range_with_shift(main_window, self.loc.TABLE_ORDER_NUMBER, self.loc.TABLE_ORDER_NUMBER10)
        self.click_element(main_window, self.loc.TABLE_DELETE, timeout=1)
        self.order_data.update({
            'del_window': self.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        self.click_element(main_window, self.loc.DEL_WINDOW_BUTTON, timeout=1)

        # 5. Создание нового заказа
        self.click_element(main_window, self.loc.ADD_BUTTON, timeout=5)
        time.sleep(1)

        # 6. Заполнение формы заказа
        self.click_element(main_window, self.loc.ORDER_TYPE_COMBO, timeout=1)
        self.click_element(main_window, self.loc.LOGISTICS_ITEM, timeout=1)
        self.click_element(main_window, self.loc.CUSTOMER_COMBO, timeout=1)
        self.click_element(main_window, self.loc.CUSTOMER_ITEM, timeout=1)
        self.click_element(main_window, self.loc.OK_BUTTON, timeout=1)
        time.sleep(1)

        main_window = self.get_main_form()
        main_window.set_focus()
        order_form = self.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)

        # 7. В заказе Прикрепить Фаил пока пропускаем

        # 8. В заказе создать ИС
        # 6. Перейти во вкладку
        self.click_element(main_window, self.loc.TAB_CHECK, timeout=1)

        # 7 Создать Исходящий счет и выставить покупателя
        self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
        self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)

        # 8. Переключение на форму ИС
        main_window = self.get_check_form()
        main_window.set_focus()
        order_form = self.app.window(**self.loc.CHECK_FROM)
        time.sleep(1)

        self.click_element(main_window, self.loc.OK_BUTTON2, timeout=1)

        # 11. Переключить на форму заказа
        main_window = self.get_main_form()
        main_window.set_focus()
        order_form = self.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)
        self.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=1)

        # 12. Удалить заказ
        self.click_element(main_window, self.loc.OTHER_ACTIONS, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')
        self.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.order_data.update({
            'del_window_is': self.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 12. Окно удаления заказа
        self.click_element(main_window, self.loc.DEL_WINDOW_BUTTON, timeout=1)

        # 13. Удалить ИС
        self.click_element(main_window, self.loc.RECIPIENT_1, timeout=1)
        self.click_element(main_window, self.loc.TABLE_DELETE, timeout=1)
        self.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=1)
        self.order_data.update({
            'del_is': self.get_element_property(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })


        # 14 Создать Входящий счет
        self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
        time.sleep(1)
        self.click_element_double(main_window, self.loc.VS_CREATE_ORDER, timeout=1)
        self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)

        # 7 Переключение на форму ВС
        main_window = self.get_check_vs_form()
        main_window.set_focus()
        order_form = self.app.window(**self.loc.CHECK_FROM_VS)
        time.sleep(1)

        self.click_element(main_window, self.loc.OK_BUTTON2, timeout=1)

        # Переключить на форму заказа
        main_window = self.get_main_form()
        main_window.set_focus()
        order_form = self.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)
        self.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=1)

        # 12. Удалить заказ
        self.click_element(main_window, self.loc.OTHER_ACTIONS, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        self.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.order_data.update({
            'del_window_vs': self.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 12. Окно удаления заказа
        self.click_element(main_window, self.loc.DEL_WINDOW_BUTTON, timeout=1)

        # 7 Удалить
        self.click_element(main_window, self.loc.RECIPIENT_1, timeout=1)
        self.click_element(main_window, self.loc.TABLE_DELETE, timeout=1)
        self.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=1)
        self.order_data.update({
            'del_vs': self.get_element_property(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # 7 Создать Исходящего платежа и выставить покупателя
        self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
        time.sleep(1)
        self.click_element_double(main_window, self.loc.IP_CREATE_ORDER, timeout=1)
        self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)

        # 7 Переключение на форму ИП
        main_window = self.get_check_ip_form()
        main_window.set_focus()
        order_form = self.app.window(**self.loc.CHECK_FROM_IP)
        time.sleep(1)
        self.click_element(main_window, self.loc.OK_BUTTON2, timeout=1)

        # Переключить на форму заказа
        main_window = self.get_main_form()
        main_window.set_focus()
        order_form = self.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)
        self.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=1)

        # 12. Удалить заказ
        self.click_element(main_window, self.loc.OTHER_ACTIONS, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        self.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.order_data.update({
            'del_window_ip': self.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 12. Окно удаления заказа
        self.click_element(main_window, self.loc.DEL_WINDOW_BUTTON, timeout=1)

        # 7 Удалить
        self.click_element(main_window, self.loc.RECIPIENT_1, timeout=1)
        self.click_element(main_window, self.loc.TABLE_DELETE, timeout=1)
        self.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=1)
        self.order_data.update({
            'del_ip': self.get_element_property(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # 7 Создать Входящий платеж и выставить покупателя
        self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
        time.sleep(1)
        self.click_element_double(main_window, self.loc.VP_CREATE_ORDER, timeout=1)
        self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)

        # 7 Переключение на форму ВП
        main_window = self.get_check_vp_form()
        main_window.set_focus()
        order_form = self.app.window(**self.loc.CHECK_FROM_VP)
        time.sleep(1)
        self.click_element(main_window, self.loc.OK_BUTTON2, timeout=1)

        # Переключить на форму заказа
        main_window = self.get_main_form()
        main_window.set_focus()
        order_form = self.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)
        self.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=1)

        # 12. Удалить заказ
        self.click_element(main_window, self.loc.OTHER_ACTIONS, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')
        self.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.order_data.update({
            'del_window_vp': self.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 12. Окно удаления заказа
        self.click_element(main_window, self.loc.DEL_WINDOW_BUTTON, timeout=1)

        # 7 Удалить
        self.click_element(main_window, self.loc.RECIPIENT_1, timeout=1)
        self.click_element(main_window, self.loc.TABLE_DELETE, timeout=1)
        self.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=1)
        self.order_data.update({
            'del_vp': self.get_element_property(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # В заказе создать Морская перевозка
        # 7. Перейти во вкладку
        self.click_element(main_window, self.loc.TAB_TRANSPORTATION, timeout=3)

        # 8. Создать морскую перевозку
        self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.click_element(main_window, self.loc.TYPE_TRANSPORTATION, timeout=3)
        self.click_element(main_window, self.loc.SEA_TRANSPORTATION, timeout=3)
        keyboard.send_keys('{ENTER}')  # нажать на ОК работает если есть фокус на кнопке, могут быть проблемы

        # 9. Переключится на форму морской перевозки
        main_window = self.get_sea_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.SEA_FORM)
        time.sleep(1)

        # Закрываем морскую перевозку
        self.click_element(order_form, self.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)

        # 12. Удалить заказ
        self.click_element(main_window, self.loc.OTHER_ACTIONS, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        self.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.order_data.update({
            'del_window_sea': self.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 12. Окно удаления заказа
        self.click_element(main_window, self.loc.DEL_WINDOW_BUTTON, timeout=1)

        # Удаляем морскую перевозку
        self.click_element(order_form, self.loc.LINE_TRANSPORTATION, timeout=2)
        self.click_element(order_form, self.loc.DEL_BUTTON, timeout=2)
        self.click_element(order_form, self.loc.YES_BUTTON, timeout=2)
        self.click_element(order_form, self.loc.REFRESH_BUTTON_ORDER, timeout=2)
        self.order_data.update({
            'del_sea': self.get_element_property(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # Создаем автоперевозку
        self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.click_element(main_window, self.loc.TYPE_TRANSPORTATION, timeout=3)
        self.click_element(main_window, self.loc.AUTO_TRANSPORTATION, timeout=3)
        keyboard.send_keys('{ENTER}')  # нажать на ОК работает если есть фокус на кнопке, могут быть проблемы

        # 5. Переключится на форму автоперевозку
        main_window = self.get_auto_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.AUTO_FORM)
        time.sleep(1)

        # Закрываем морскую перевозку
        self.click_element(order_form, self.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)
        # 5. Переключение на форму заказа
        main_window = self.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)

        # 12. Удалить заказ
        self.click_element(main_window, self.loc.OTHER_ACTIONS, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        self.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.order_data.update({
            'del_window_auto': self.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 12. Окно удаления заказа
        self.click_element(main_window, self.loc.DEL_WINDOW_BUTTON, timeout=1)

        # Удаляем автоперевозку
        self.click_element(order_form, self.loc.LINE_TRANSPORTATION, timeout=2)
        self.click_element(order_form, self.loc.DEL_BUTTON, timeout=2)
        self.click_element(order_form, self.loc.YES_BUTTON, timeout=2)
        self.click_element(order_form, self.loc.REFRESH_BUTTON_ORDER, timeout=2)
        self.order_data.update({
            'del_auto': self.get_element_property(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # В заказе создать Экспедирование
        # В заказе создать Груз
        # 6. Перейти во вкладку
        self.click_element(main_window, self.loc.TAB_FREIGHT, timeout=2)

        # 7 Создать Bulkership
        self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
        self.click_element(main_window, self.loc.FREIGHT_CREATE_TE, timeout=1)
        self.click_element(main_window, self.loc.FREIGHT_CREATE_TE1, timeout=1)
        self.click_element(main_window, self.loc.FREIGHT_CREATE_TYPE, timeout=1)
        self.click_element(main_window, self.loc.FREIGHT_CREATE_TYPE1, timeout=1)
        self.set_text_field(main_window, self.loc.FREIGHT_CREATE_QUANTITY, 1, timeout=1)
        self.click_element(main_window, self.loc.FREIGHT_CREATE_UOM, timeout=1)
        self.click_element(main_window, self.loc.FREIGHT_CREATE_UOM1, timeout=1)
        self.click_element(main_window, self.loc.OK_BUTTON, timeout=1)
        time.sleep(1)

        # 12. Удалить заказ
        self.click_element(main_window, self.loc.OTHER_ACTIONS, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        self.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.order_data.update({
            'del_window_bul': self.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 12. Окно удаления заказа
        self.click_element(main_window, self.loc.DEL_WINDOW_BUTTON, timeout=1)

        # 5. Удалить Bulkership
        self.click_element(order_form, self.loc.FREIGHT_ITEM, timeout=5)
        self.click_element(order_form, self.loc.DEL_BUTTON, timeout=2)
        self.click_element(order_form, self.loc.YES_BUTTON, timeout=2)
        self.click_element(order_form, self.loc.REFRESH_BUTTON_ORDER, timeout=2)
        self.order_data.update({
            'del_bul': self.get_element_property(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # 7 Создать Container
        self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
        self.click_element(main_window, self.loc.FREIGHT_CREATE_TE, timeout=1)
        self.click_element(main_window, self.loc.FREIGHT_CREATE_TE2, timeout=1)
        time.sleep(1)
        self.click_element(main_window, self.loc.FREIGHT_CREATE_TYPE, timeout=1)
        self.click_element(main_window, self.loc.FREIGHT_CREATE_TYPE1, timeout=1)
        self.set_text_field(main_window, self.loc.FREIGHT_CREATE_QUANTITY, 1, timeout=1)
        time.sleep(1)
        self.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

        # 12. Удалить заказ
        self.click_element(main_window, self.loc.OTHER_ACTIONS, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        self.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.order_data.update({
            'del_window_con': self.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 12. Окно удаления заказа
        self.click_element(main_window, self.loc.DEL_WINDOW_BUTTON, timeout=1)

        # 5. Удалить Container
        self.click_element(main_window, self.loc.LINE_TRANSPORTATION, timeout=1)
        self.click_element(main_window, self.loc.DEL_BUTTON, timeout=2)
        self.click_element(main_window, self.loc.YES_BUTTON, timeout=2)
        self.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=2)
        self.order_data.update({
            'del_con': self.get_element_property(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # В заказе создать ГТД и удалить груз
        # 7. Перейти во вкладку груза
        self.click_element(main_window, self.loc.TAB_FREIGHT, timeout=3)

        # 8 Создать Bulkership
        self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=5)
        self.click_element(main_window, self.loc.FREIGHT_CREATE_TE, timeout=1)
        self.click_element(main_window, self.loc.FREIGHT_CREATE_TE1, timeout=1)
        self.click_element(main_window, self.loc.FREIGHT_CREATE_TYPE, timeout=1)
        self.click_element(main_window, self.loc.FREIGHT_CREATE_TYPE1, timeout=1)
        self.set_text_field(main_window, self.loc.FREIGHT_CREATE_QUANTITY, 1, timeout=1)
        self.click_element(main_window, self.loc.FREIGHT_CREATE_UOM, timeout=1)
        self.click_element(main_window, self.loc.FREIGHT_CREATE_UOM1, timeout=1)
        keyboard.send_keys('{ENTER}')  # нажать на ОК работает если есть фокус на кнопке, могут быть проблемы
        time.sleep(1)

        # 10. Перейти во вкладку Декларирования
        self.click_element(main_window, self.loc.TAB_GTD, timeout=1)
        self.click_element(main_window, self.loc.ADD_BUTTON, timeout=1)
        time.sleep(2)

        # 11. Переключение на форму ГТД
        main_window = self.get_gtd_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.GTD_FROM)

        # 12. Прикрепить ТЕ
        self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
        self.click_element(order_form, self.loc.ADD_TE, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        self.click_element(main_window, self.loc.OK_BUTTON2, timeout=1)

        # 5. Переключение на форму заказа
        main_window = self.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)

        # 6. Перейти во вкладку груза
        self.click_element(main_window, self.loc.TAB_FREIGHT, timeout=2)

        # 5. Удалить Bulkership
        self.click_element(order_form, self.loc.FREIGHT_ITEM, timeout=5)
        self.click_element(order_form, self.loc.DEL_BUTTON, timeout=2)
        self.click_element(order_form, self.loc.YES_BUTTON, timeout=2)
        self.click_element(order_form, self.loc.REFRESH_BUTTON_ORDER, timeout=2)

        # 10. Перейти во вкладку Декларирования
        self.click_element(main_window, self.loc.TAB_GTD, timeout=1)
        self.click_element(main_window, self.loc.REFRESH_BUTTON, timeout=2)

        # 12. Удалить заказ
        self.click_element(main_window, self.loc.OTHER_ACTIONS, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        self.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.order_data.update({
            'del_window_gtd': self.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 12. Окно удаления заказа
        self.click_element(main_window, self.loc.DEL_WINDOW_BUTTON, timeout=1)

        # 12. Удалить ГТД
        self.click_element(order_form, self.loc.TABLE_DELETE, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.click_element(main_window, self.loc.REFRESH_BUTTON, timeout=2)
        self.order_data.update({
            'del_gtd': self.get_element_property(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # 7. Создание и удаление Экспедирование
        self.click_element(main_window, self.loc.TAB_FORWARDING, timeout=3)

        # 8. Создать Экспедирование
        self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
        self.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

        # 9. Переключится на форму Экспедирования
        main_window = self.get_forwarding_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.FORWARDING_FROM)
        time.sleep(1)

        # 11. Закрываем Экспедирование
        self.click_element(order_form, self.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)

        # 21. Переключение на форму заказа
        main_window = self.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)

        # 12. Удалить заказ
        self.click_element(main_window, self.loc.OTHER_ACTIONS, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')
        self.click_element(main_window, self.loc.YES_BUTTON, timeout=2)
        self.order_data.update({
            'del_window_exp': self.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 12. Окно удаления заказа
        self.click_element(main_window, self.loc.DEL_WINDOW_BUTTON, timeout=1)

        # 23. Удаляем Экспедирование
        self.click_element(order_form, self.loc.LINE_TRANSPORTATION, timeout=2)
        self.click_element(order_form, self.loc.DEL_BUTTON, timeout=2)
        self.click_element(order_form, self.loc.YES_BUTTON, timeout=2)
        self.click_element(order_form, self.loc.REFRESH_BUTTON_ORDER, timeout=2)
        self.order_data.update({
            'del_exp': self.get_element_property(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        return self.order_data

    def close(self):
        """Завершение работы приложения"""
        self.app.kill(soft=True)
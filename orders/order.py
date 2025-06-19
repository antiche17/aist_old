from pywinauto import Application, keyboard
from locators.locators import LocOrders
import time


class WinAISTApp:
    def __init__(self):
        self.app = Application(backend='uia')
        self.loc = LocOrders()
        self.order_data = {}  # Для хранения данных заказа

    def start_application(self):
        """Запуск приложения"""
        self.app.start(r"C:\Ilya\Debug\WinAIST.exe")
        # Ждем появления окна старта и подключаемся к нему
        window = self.app.window(**self.loc.STARTUP_WINDOW)
        window.wait('visible', timeout=30)  # ждём, пока окно появится
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

    def create_order(self):
        """Создание заказа с типом Логистика и заполнение order_data"""
        # 1. Запуск приложения
        startup_window = self.start_application()
        startup_window.set_focus()

        # 2. Нажатие кнопки Запуск
        self.click_element(startup_window, self.loc.START_BUTTON, timeout=1)
        time.sleep(15)

        # 3. Переход в раздел Заказы
        main_window = self.get_main_window()
        main_window.set_focus()
        time.sleep(4)

        self.click_element(main_window, self.loc.ORDERS_TAB, timeout=3)
        time.sleep(5)

        # 4. Создание нового заказа
        self.click_element(main_window, self.loc.ADD_BUTTON, timeout=5)
        time.sleep(1)

        # 5. Заполнение формы заказа
        self.click_element(main_window, self.loc.ORDER_TYPE_COMBO, timeout=1)
        self.click_element(main_window, self.loc.LOGISTICS_ITEM, timeout=1)
        self.click_element(main_window, self.loc.CUSTOMER_COMBO, timeout=1)
        self.click_element(main_window, self.loc.CUSTOMER_ITEM, timeout=1)
        time.sleep(1)

        # 6. Взять значения для проверок
        self.order_data = {
            'order_dialog_type': self.get_element_property(main_window, self.loc.ORDER_TYPE_COMBO, "Value"),
            'order_dialog_client': self.get_element_property(main_window, self.loc.CUSTOMER_COMBO, "Value"),
            'order_dialog_otv': self.get_element_property(main_window, self.loc.RESPONSIBLE_COMBO, "Value"),
        }
        self.click_element(main_window, self.loc.OK_BUTTON, timeout=1)
        time.sleep(1)

        order_form = self.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)

        # 7. Получение данных из формы заказа
        self.order_data.update({
            'order_number': self.get_element_property(order_form, self.loc.ORDER_NUMBER, "Value"),
            'order_type': self.get_element_property(order_form, self.loc.ORDER_TYPE_TEXT, "Name"),
            'order_status': self.get_element_property(order_form, self.loc.STATUS_COMBO, "Value"),
            'order_priority': self.get_element_property(order_form, self.loc.PRIORITY_COMBO, "Value"),
            'order_otv': self.get_element_property(order_form, self.loc.RESPONSIBLE_COMBO, "Value"),

            'order_client': self.get_element_property(order_form, self.loc.CLIENT_COMBO, "Value"),
            'order_senders': self.get_element_property(order_form, self.loc.SENDERS_1, "Value"),
            'order_recipient': self.get_element_property(order_form, self.loc.RECIPIENT, "Value"),
            'order_delivery': self.get_element_property(order_form, self.loc.DELIVERY_CONDITION, "Value"),

            'order_create_mod': self.get_element_property(order_form, self.loc.MOD_DATE, "Name"),
            'order_create_date': self.get_element_property(order_form, self.loc.CREATE_DATE, "Name"),
            'order_completion_date': self.get_element_property(order_form, self.loc.COMPLETION_DATE, "Name"),
            'order_reference': self.get_element_property(order_form, self.loc.REFERENCE, "Value"),
            'order_note': self.get_element_property(order_form, self.loc.NOTE, "Value"),

            'order_tab_freight': self.get_element_property(order_form, self.loc.TAB_FREIGHT, "Name"),
            'order_tab_transportation': self.get_element_property(order_form, self.loc.TAB_TRANSPORTATION, "Name"),
            'order_tab_forwarding': self.get_element_property(order_form, self.loc.TAB_FORWARDING, "Name"),
            'order_tab_gtd': self.get_element_property(order_form, self.loc.TAB_GTD, "Name"),
            'order_tab_check': self.get_element_property(order_form, self.loc.TAB_CHECK, "Name"),
            'order_tab_file': self.get_element_property(order_form, self.loc.TAB_FILE, "Name"),
            'order_tab_services': self.get_element_property(order_form, self.loc.TAB_SERVICES, "Name"),
            'order_tab_tracking': self.get_element_property(order_form, self.loc.TAB_TRACKING, "Name"),
        })

        # 8. Сохранение заказа
        self.click_element(order_form, self.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)

        # 9. Обновляем таблицу
        main_window.set_focus()
        time.sleep(1)
        self.click_element(main_window, self.loc.REFRESH_BUTTON, timeout=2)

        # 10. Проверка данных в таблице
        self.order_data.update({
            'table_order': self.get_element_property(main_window, self.loc.TABLE_ORDER_NUMBER, "Value"),
            'table_type': self.get_element_property(main_window, self.loc.TABLE_ORDER_TYPE, "Value"),
            'table_status': self.get_element_property(main_window, self.loc.TABLE_STATUS, "Value"),
            'table_priority': self.get_element_property(main_window, self.loc.TABLE_PRIORITY, "Value"),
            'table_creator': self.get_element_property(main_window, self.loc.TABLE_CREATOR, "Value"),
            'table_client': self.get_element_property(main_window, self.loc.TABLE_CLIENT, "Value")
        })

        return self.order_data

    def create_order_update(self):
        """Добавить сравнение в таблице """
        """Создание заказа с типом Другие услуги и заполнение order_data"""
        # 1. Запуск приложения
        startup_window = self.start_application()
        startup_window.set_focus()

        # 2. Нажатие кнопки Запуск
        self.click_element(startup_window, self.loc.START_BUTTON, timeout=1)
        time.sleep(15)

        # 3. Переход в раздел Заказы
        main_window = self.get_main_window()
        main_window.set_focus()
        time.sleep(4)

        self.click_element(main_window, self.loc.ORDERS_TAB, timeout=3)
        time.sleep(5)

        # 4. Открыть заказ заказа
        self.click_element_double(main_window, self.loc.TABLE_ORDER_NUMBER, timeout=5)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 6. Меняем данные
        self.click_element(main_window, self.loc.STATUS_COMBO, timeout=1)
        self.click_element(main_window, self.loc.STATUS_COMBO_CANCEL, timeout=1)
        self.click_element(main_window, self.loc.PRIORITY_COMBO, timeout=1)
        self.click_element(main_window, self.loc.PRIORITY_COMBO_KRIT, timeout=1)

        self.click_element(main_window, self.loc.CLIENT_COMBO, timeout=1)
        self.click_element(main_window, self.loc.CLIENT_COMBO_3, timeout=3)
        self.click_element(main_window, self.loc.SENDERS_1, timeout=3)
        self.type_keys(main_window, self.loc.SENDERS_1, timeout=3)
        self.click_element(main_window, self.loc.RECIPIENT, timeout=1)
        self.click_element(main_window, self.loc.RECIPIENT_1, timeout=1)
        self.click_element(main_window, self.loc.DELIVERY_CONDITION, timeout=1)
        self.click_element(main_window, self.loc.DELIVERY_CONDITION_0, timeout=1)

        self.set_text_field(main_window, self.loc.REFERENCE, "Привет, мир!", timeout=1)
        self.set_text_field(main_window, self.loc.NOTE, "Привет, наш огромный дивный мир! 666 ", timeout=1)

        # 7. Получение данных из формы заказа
        order_form = self.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)

        self.order_data = {
            'order_status': self.get_element_property(order_form, self.loc.STATUS_COMBO, "Value"),
            'order_priority': self.get_element_property(order_form, self.loc.PRIORITY_COMBO, "Value"),

            'order_client': self.get_element_property(order_form, self.loc.CLIENT_COMBO, "Value"),
            'order_senders': self.get_element_property(order_form, self.loc.SENDERS_1, "Value"),
            'order_recipient': self.get_element_property(order_form, self.loc.RECIPIENT, "Value"),
            'order_delivery': self.get_element_property(order_form, self.loc.DELIVERY_CONDITION, "Value"),

            'order_reference': self.get_element_property(order_form, self.loc.REFERENCE, "Value"),
            'order_note': self.get_element_property(order_form, self.loc.NOTE, "Value"),
            'order_mod_date': self.get_element_property(order_form, self.loc.MOD_DATE, "Name")
        }

        # 8. Сохранение заказа
        self.click_element(order_form, self.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)

        # 3. Переход в раздел Заказы
        main_window = self.get_main_window()
        main_window.set_focus()
        time.sleep(4)

        # 7. Обновляем таблицу
        main_window.set_focus()
        time.sleep(1)
        self.click_element(main_window, self.loc.REFRESH_BUTTON, timeout=2)

        self.order_data.update({
            'table_type': self.get_element_property(main_window, self.loc.TABLE_ORDER_TYPE, "Value"),
            'table_status': self.get_element_property(main_window, self.loc.TABLE_STATUS, "Value"),
            'table_priority': self.get_element_property(main_window, self.loc.TABLE_PRIORITY, "Value"),
            'table_client': self.get_element_property(main_window, self.loc.TABLE_CLIENT, "Value"),
            'table_recipient': self.get_element_property(main_window, self.loc.TABLE_RECIPIENT, "Value"),
            'table_delivery': self.get_element_property(main_window, self.loc.TABLE_DELIVERY, "Value"),
            'table_note': self.get_element_property(main_window, self.loc.TABLE_NOTE, "Value")
        })

        # 8. Открыть заказ
        self.click_element_double(main_window, self.loc.TABLE_ORDER_NUMBER, timeout=5)
        time.sleep(1)

        # 9. Переключение на форму заказа
        main_window = self.get_main_form()
        main_window.set_focus()
        time.sleep(3)

        # 10. Проверка сохранённых данных
        self.order_data.update ({
            'repeat_status': self.get_element_property(order_form, self.loc.STATUS_COMBO, "Value"),
            'repeat_priority': self.get_element_property(order_form, self.loc.PRIORITY_COMBO, "Value"),
            'repeat_client': self.get_element_property(order_form, self.loc.CLIENT_COMBO, "Value"),
            'repeat_senders': self.get_element_property(order_form, self.loc.SENDERS_1, "Value"),
            'repeat_recipient': self.get_element_property(order_form, self.loc.RECIPIENT, "Value"),
            'repeat_delivery': self.get_element_property(order_form, self.loc.DELIVERY_CONDITION, "Value"),
            'repeat_reference': self.get_element_property(order_form, self.loc.REFERENCE, "Value"),
            'repeat_note': self.get_element_property(order_form, self.loc.NOTE, "Value"),
            'order_mod_date1': self.get_element_property(order_form, self.loc.MOD_DATE, "Name")
        })

        return self.order_data

    def create_order_dr(self):
        """Создание заказа с типом Другие услуги и заполнение order_data"""
        # 1. Запуск приложения
        startup_window = self.start_application()
        startup_window.set_focus()

        # 2. Нажатие кнопки Запуск
        self.click_element(startup_window, self.loc.START_BUTTON, timeout=1)
        time.sleep(15)

        # 3. Переход в раздел Заказы
        main_window = self.get_main_window()
        main_window.set_focus()
        time.sleep(3)
        self.click_element(main_window, self.loc.ORDERS_TAB, timeout=3)

        # 4. Создание нового заказа
        self.click_element(main_window, self.loc.ADD_BUTTON, timeout=1)
        time.sleep(1)
        self.click_element(main_window, self.loc.ORDER_TYPE_COMBO, timeout=1)
        self.click_element(main_window, self.loc.LOGISTICS_ITEM_DR, timeout=1)
        self.click_element(main_window, self.loc.CUSTOMER_COMBO, timeout=1)
        self.click_element(main_window, self.loc.CUSTOMER_ITEM, timeout=1)
        time.sleep(1)
        self.order_data = {
            'order_dialog_type': self.get_element_property(main_window, self.loc.ORDER_TYPE_COMBO, "Value"),
            'order_dialog_client': self.get_element_property(main_window, self.loc.CUSTOMER_COMBO, "Value"),
            'order_dialog_otv': self.get_element_property(main_window, self.loc.RESPONSIBLE_COMBO, "Value"),
        }
        self.click_element(main_window, self.loc.OK_BUTTON, timeout=1)
        time.sleep(3)

        # 5. Получение данных из формы заказа
        order_form = self.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)

        self.order_data.update({
            'order_number': self.get_element_property(order_form, self.loc.ORDER_NUMBER, "Value"),
            'order_type': self.get_element_property(order_form, self.loc.ORDER_TYPE_TEXT, "Name"),
            'order_status': self.get_element_property(order_form, self.loc.STATUS_COMBO, "Value"),
            'order_priority': self.get_element_property(order_form, self.loc.PRIORITY_COMBO, "Value"),
            'order_otv': self.get_element_property(order_form, self.loc.RESPONSIBLE_COMBO, "Value"),
            'order_client': self.get_element_property(order_form, self.loc.CLIENT_COMBO, "Value"),
            'order_create_mod': self.get_element_property(order_form, self.loc.MOD_DATE, "Name"),
            'order_create_date': self.get_element_property(order_form, self.loc.CREATE_DATE, "Name"),
            'order_completion_date': self.get_element_property(order_form, self.loc.COMPLETION_DATE, "Name"),
            'order_reference': self.get_element_property(order_form, self.loc.REFERENCE, "Value"),
            'order_tab_check': self.get_element_property(order_form, self.loc.TAB_CHECK, "Name"),
            'order_tab_file': self.get_element_property(order_form, self.loc.TAB_FILE, "Name"),
            'order_tab_services': self.get_element_property(order_form, self.loc.TAB_SERVICES, "Name"),
            'order_note': self.get_element_property(order_form, self.loc.NOTE, "Value"),
        })

        # 6. Сохранение заказа
        self.click_element(order_form, self.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)

        # 7. Получение данных из таблицы
        main_window.set_focus()
        time.sleep(1)
        self.click_element(main_window, self.loc.REFRESH_BUTTON, timeout=2)

        self.order_data.update({
            'table_order': self.get_element_property(main_window, self.loc.TABLE_ORDER_NUMBER, "Value"),
            'table_type': self.get_element_property(main_window, self.loc.TABLE_ORDER_TYPE, "Value"),
            'table_status': self.get_element_property(main_window, self.loc.TABLE_STATUS, "Value"),
            'table_priority': self.get_element_property(main_window, self.loc.TABLE_PRIORITY, "Value"),
            'table_creator': self.get_element_property(main_window, self.loc.TABLE_CREATOR, "Value"),
            'table_date': self.get_element_property(main_window, self.loc.TABLE_DATE, "Value"),
            'table_client': self.get_element_property(main_window, self.loc.TABLE_CLIENT, "Value")
        })

        return self.order_data

    def create_order_del(self):
        """Сравнение удаленных строчек"""
        """Создание заказа с типом Другие услуги и заполнение order_data"""
        # 1. Запуск приложения
        startup_window = self.start_application()
        startup_window.set_focus()

        # 2. Нажатие кнопки Запуск
        self.click_element(startup_window, self.loc.START_BUTTON, timeout=1)
        time.sleep(15)

        # 3. Переход в раздел Заказы
        main_window = self.get_main_window()
        main_window.set_focus()
        time.sleep(4)

        self.click_element(main_window, self.loc.ORDERS_TAB, timeout=3)
        time.sleep(5)

        # Берем номер 1 заказа с таблицей
        self.order_data = {
            'delete_order': self.get_element_property(main_window, self.loc.TABLE_ORDER_NUMBER, "Value")
        }

        # Удаление 1 заказа
        self.click_element(main_window, self.loc.TABLE_ORDER_NUMBER, timeout=5)
        time.sleep(1)
        self.click_element(main_window, self.loc.TABLE_DELETE, timeout=1)
        self.click_element(main_window, self.loc.TABLE_DELETE_WINDOW, timeout=1)

        # Обновить таблицу
        self.click_element(main_window, self.loc.REFRESH_BUTTON, timeout=2)

        # Cравнение изменений
        self.order_data.update({
            'table_order': self.get_element_property(main_window, self.loc.TABLE_ORDER_NUMBER, "Value")
        })

        # Берем номер 2 заказа с таблицей
        self.order_data.update({
            'table_order_del1': self.get_element_property(main_window, self.loc.TABLE_ORDER_NUMBER, "Value"),
            'table_order_del2': self.get_element_property(main_window, self.loc.TABLE_ORDER_NUMBER_2, "Value")
        })
        # Выбор 2х заказов и удаление их
        self.select_two_elements_with_ctrl(main_window,self.loc.TABLE_ORDER_NUMBER, self.loc.TABLE_ORDER_NUMBER_2)
        self.click_element(main_window, self.loc.TABLE_DELETE, timeout=1)
        self.click_element(main_window, self.loc.TABLE_DELETE_WINDOW, timeout=1)

        # Обновить таблицу
        self.click_element(main_window, self.loc.REFRESH_BUTTON, timeout=2)

        # Cравнение изменений
        self.order_data.update({
            'table_order_1': self.get_element_property(main_window, self.loc.TABLE_ORDER_NUMBER, "Value"),
            'table_order_2': self.get_element_property(main_window, self.loc.TABLE_ORDER_NUMBER_2, "Value")
        })

        return self.order_data

    def transportation(self):
        """Создание перевозок"""
        """Создание морской перевозки"""
        # 1. Запуск приложения
        startup_window = self.start_application()
        startup_window.set_focus()

        # 2. Нажатие кнопки Запуск
        self.click_element(startup_window, self.loc.START_BUTTON, timeout=1)
        time.sleep(15)

        # 3. Переход в раздел Заказы
        main_window = self.get_main_window()
        main_window.set_focus()
        time.sleep(4)

        self.click_element(main_window, self.loc.ORDERS_TAB, timeout=3)
        time.sleep(5)

        # 4. Открыть заказ заказа
        self.click_element_double(main_window, self.loc.TABLE_ORDER_NUMBER, timeout=5)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)

        # 6. Взять номер заказа
        self.order_data = {
            'order_number': self.get_element_property(order_form, self.loc.ORDER_NUMBER, "Name")
        }

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

        # 10. Проверка полей
        self.order_data.update({
            'sea_order_number': self.get_element_property(order_form, self.loc.ORDER_NUMBER, "Name"),
            'sea_order_name': self.get_element_property(order_form, self.loc.SEA_ORDER_NAME, "Name"),
            'sea_type': self.get_element_property(order_form, self.loc.SEA_TYPE_TEXT, "Name"),
            'sea_status': self.get_element_property(order_form, self.loc.STATUS_COMBO, "Value"),
            'sea_priority': self.get_element_property(order_form, self.loc.PRIORITY_COMBO, "Value"),
            'sea_otv': self.get_element_property(order_form, self.loc.RESPONSIBLE_COMBO, "Value"),
            'sea_create_date': self.get_element_property(order_form, self.loc.CREATE_DATE, "Value"),
            'sea_mode_date': self.get_element_property(order_form, self.loc.MOD_DATE, "Value")
        })

        # Закрываем морскую перевозку
        self.click_element(order_form, self.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)

        # Во вкладке Перевозки, таблица
        self.order_data.update({
            'sea_order_table': self.get_element_property(order_form, self.loc.TRANSPORTATION_ITEM, "Value")
        })

        # Удаляем морскую перевозку
        self.click_element(order_form, self.loc.LINE_TRANSPORTATION, timeout=2)
        self.click_element(order_form, self.loc.DEL_BUTTON, timeout=2)
        self.click_element(order_form, self.loc.YES_BUTTON, timeout=2)
        self.click_element(order_form, self.loc.REFRESH_BUTTON_ORDER, timeout=2)

        # Создаем автоперевозку
        self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.click_element(main_window, self.loc.TYPE_TRANSPORTATION, timeout=3)
        self.click_element(main_window, self.loc.AUTO_TRANSPORTATION, timeout=3)
        keyboard.send_keys('{ENTER}')  # нажать на ОК работает если есть фокус на кнопке, могут быть проблемы

        # 5. Переключится на форму морской перевозки
        main_window = self.get_auto_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.AUTO_FORM)
        time.sleep(1)

        # 5. Проверка полей
        self.order_data.update({
            'auto_order_number': self.get_element_property(order_form, self.loc.AUTO_NAME_TRANSPORTATION, "Name"),
            'auto_type': self.get_element_property(order_form, self.loc.AUTO_TYPE_TEXT, "Name"),
            'auto_status': self.get_element_property(order_form, self.loc.STATUS_COMBO, "Value"),
            'auto_priority': self.get_element_property(order_form, self.loc.PRIORITY_COMBO, "Value"),
            'auto_otv': self.get_element_property(order_form, self.loc.RESPONSIBLE_COMBO, "Value"),
            'auto_create_date': self.get_element_property(order_form, self.loc.CREATE_DATE, "Value"),
            'auto_mode_date': self.get_element_property(order_form, self.loc.MOD_DATE, "Value")
        })

        return self.order_data

    def forwarding(self):
        # 1. Запуск приложения
        startup_window = self.start_application()
        startup_window.set_focus()

        # 2. Нажатие кнопки Запуск
        self.click_element(startup_window, self.loc.START_BUTTON, timeout=1)
        time.sleep(15)

        # 3. Переход в раздел Заказы
        main_window = self.get_main_window()
        main_window.set_focus()
        time.sleep(4)

        self.click_element(main_window, self.loc.ORDERS_TAB, timeout=3)
        time.sleep(5)

        # 4. Открыть заказ заказа
        self.click_element_double(main_window, self.loc.TABLE_ORDER_NUMBER, timeout=5)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)

        # 6. Взять номер заказа
        self.order_data = {
            'order_number': self.get_element_property(order_form, self.loc.ORDER_NUMBER, "Name")
        }

        # 7. Перейти во вкладку
        self.click_element(main_window, self.loc.TAB_FORWARDING, timeout=3)

        # 8. Создать Экспедирование
        self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
        self.order_data.update({
            'forwarding_dialog_type': self.get_element_property(order_form, self.loc.FORWARDING_TYPE_DIALOG, "Value"),
            'forwarding_dialog_otv': self.get_element_property(order_form, self.loc.RESPONSIBLE_COMBO, "Value"),

        })

        self.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

        # 9. Переключится на форму морской перевозки
        main_window = self.get_forwarding_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.FORWARDING_FROM)
        time.sleep(1)

        # 10. Проверка полей
        self.order_data.update({
            'forwarding_order_number': self.get_element_property(order_form, self.loc.ORDER_NUMBER, "Name"),
            'forwarding_type': self.get_element_property(order_form, self.loc.FORWARDING_TYPE_TEXT, "Name"),
            'forwarding_status': self.get_element_property(order_form, self.loc.STATUS_COMBO, "Value"),
            'forwarding_priority': self.get_element_property(order_form, self.loc.PRIORITY_COMBO, "Value"),
            'forwarding_otv': self.get_element_property(order_form, self.loc.RESPONSIBLE_COMBO, "Value"),

            'forwarding_forwarder': self.get_element_property(order_form, self.loc.FORWARDING_FORWARDER, "Value"),

            'forwarding_create_date': self.get_element_property(order_form, self.loc.CREATE_DATE, "Value"),
            'forwarding_mode_date': self.get_element_property(order_form, self.loc.MOD_DATE, "Value"),
            'forwarding_completion_data': self.get_element_property(order_form, self.loc.COMPLETION_DATE, "Value"),

            'forwarding_telex': self.get_element_property(order_form, self.loc.FORWARDING_TELEX, "Value"),
            'forwarding_receiving_doc': self.get_element_property(order_form, self.loc.FORWARDING_RECEIVING_DOC,
                                                                  "Value"),
            'forwarding_nomination': self.get_element_property(order_form, self.loc.FORWARDING_NOMINATION, "Value"),
            'forwarding_receiving_do': self.get_element_property(order_form, self.loc.FORWARDING_RECEIVING_DO, "Value"),

            'forwarding_note': self.get_element_property(order_form, self.loc.NOTE, "Value"),

            'tab_info': self.get_element_property(order_form, self.loc.TAB_INFO, "Name"),
            'tab_forwarding_freight': self.get_element_property(order_form, self.loc.TAB_FORWARDING_FREIGHT, "Name"),
            'tab_services': self.get_element_property(order_form, self.loc.TAB_SERVICES, "Name"),
            'tab_file': self.get_element_property(order_form, self.loc.TAB_FILE, "Name"),
        })

        # 11. Закрываем морскую перевозку
        self.click_element(order_form, self.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)

        # 12. Переключение на форму заказа
        main_window = self.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)

        # 13. Открыть Экспедирование
        self.click_element_double(order_form, self.loc.LINE_TRANSPORTATION, timeout=1)

        # 14. Переключится на форму морской перевозки
        main_window = self.get_forwarding_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.FORWARDING_FROM)
        time.sleep(1)

        # 15. Редактирование Экспедирование
        self.click_element(order_form, self.loc.STATUS_COMBO, timeout=1)
        self.click_element(order_form, self.loc.STATUS_FINISH, timeout=1)
        self.click_element(order_form, self.loc.PRIORITY_COMBO, timeout=1)
        self.click_element(order_form, self.loc.PRIORITY_COMBO_LOW, timeout=1)

        self.click_element(order_form, self.loc.FORWARDING_FORWARDER, timeout=1)
        self.click_element(order_form, self.loc.RECIPIENT_1, timeout=1)

        self.click_element(order_form, self.loc.FORWARDING_TELEX, timeout=1)
        time.sleep(1)
        keyboard.send_keys('1')
        self.click_element(order_form, self.loc.FORWARDING_RECEIVING_DOC, timeout=1)
        time.sleep(1)
        keyboard.send_keys('2')
        self.click_element(order_form, self.loc.FORWARDING_NOMINATION, timeout=1)
        time.sleep(1)
        keyboard.send_keys('3')
        self.click_element(order_form, self.loc.FORWARDING_RECEIVING_DO, timeout=1)
        time.sleep(1)
        keyboard.send_keys('4')
        self.set_text_field(main_window, self.loc.NOTE, "CAAU 111111 \n"
                                                        "MSMU 2222222 + СААU 333333  2х20 ставка перевоза по 7 000р/щт\n"
                                                        "\n"
                                                        "Иван Иванов Иванович 30.12.1985\n"
                                                        "0000 111111 МВД по Республике Дагестан от 05.07.2021 Мира 1 кв1\n"
                                                        "89888333222 SCANIA А777УЕ05 прицеп УЕ1111 05\n"
                                                        "погрузка визит 13\05 1:40 - 4:50 ;\n"
                                                        "сдача на КТСП 13/05 ", timeout=1)

        # 16. Проверка введенных данных
        self.order_data.update({
            'forwarding_status_up': self.get_element_property(order_form, self.loc.STATUS_COMBO, "Value"),
            'forwarding_priority_up': self.get_element_property(order_form, self.loc.PRIORITY_COMBO, "Value"),
            'forwarding_forwarder_up': self.get_element_property(order_form, self.loc.FORWARDING_FORWARDER, "Value"),

            'forwarding_telex_up': self.get_element_property(order_form, self.loc.FORWARDING_TELEX, "Value"),
            'forwarding_receiving_doc_up': self.get_element_property(order_form, self.loc.FORWARDING_RECEIVING_DOC,"Value"),
            'forwarding_nomination_up': self.get_element_property(order_form, self.loc.FORWARDING_NOMINATION, "Value"),
            'forwarding_receiving_do_up': self.get_element_property(order_form, self.loc.FORWARDING_RECEIVING_DO,"Value"),
            'forwarding_note_up': self.get_element_property(order_form, self.loc.NOTE, "Value"),
        })

        self.click_element(order_form, self.loc.SAVE_BUTTON, timeout=1)

        # 17. Переключение на форму заказа
        main_window = self.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)

        # 18. Открыть Экспедирование
        self.click_element_double(order_form, self.loc.LINE_TRANSPORTATION, timeout=1)

        # 14. Переключится на форму морской перевозки
        main_window = self.get_forwarding_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.FORWARDING_FROM)
        time.sleep(1)

        # 19. Проверка сохраненных данных
        self.order_data.update({
            'forwarding_status_save': self.get_element_property(order_form, self.loc.STATUS_COMBO, "Value"),
            'forwarding_priority_save': self.get_element_property(order_form, self.loc.PRIORITY_COMBO, "Value"),

            'forwarding_forwarder_save': self.get_element_property(order_form, self.loc.FORWARDING_FORWARDER, "Value"),
            'forwarding_telex_save': self.get_element_property(order_form, self.loc.FORWARDING_TELEX, "Value"),
            'forwarding_receiving_doc_save': self.get_element_property(order_form, self.loc.FORWARDING_RECEIVING_DOC,"Value"),
            'forwarding_nomination_save': self.get_element_property(order_form, self.loc.FORWARDING_NOMINATION,"Value"),
            'forwarding_receiving_do_save': self.get_element_property(order_form, self.loc.FORWARDING_RECEIVING_DO,"Value"),
            'forwarding_note_save': self.get_element_property(order_form, self.loc.NOTE, "Value"),
        })

        # 20. Переключится на форму морской перевозки
        main_window = self.get_forwarding_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.FORWARDING_FROM)
        time.sleep(1)

        self.click_element(order_form, self.loc.SAVE_BUTTON, timeout=1)

        # 21. Переключение на форму заказа
        main_window = self.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)

        # 22. Во вкладке Перевозки, таблица
        self.order_data.update({
            'forwarding_type_table': self.get_element_property(order_form, self.loc.FORWARDING_ITEM, "Value"),
            'forwarding_order_table': self.get_element_property(order_form, self.loc.FORWARDING_NUMBER, "Value"),
            'forwarding_status_table': self.get_element_property(order_form, self.loc.FORWARDING_STATUS, "Value"),
            'forwarding_otv_table': self.get_element_property(order_form, self.loc.FORWARDING_OTV, "Value"),
            'forwarding_forward_table': self.get_element_property(order_form, self.loc.FORWARDING_FORWARD, "Value"),
            'forwarding_te_table': self.get_element_property(order_form, self.loc.FORWARDING_TE, "Value"),
            'forwarding_create_table': self.get_element_property(order_form, self.loc.FORWARDING_DATA_CREATE, "Value"),
            'forwarding_mod_table': self.get_element_property(order_form, self.loc.FORWARDING_DATA_FINISH, "Value"),
            'forwarding_note_table': self.get_element_property(order_form, self.loc.FORWARDING_NOTE, "Value")
        })

        # 23. Удаляем морскую перевозку
        self.click_element(order_form, self.loc.LINE_TRANSPORTATION, timeout=2)
        self.click_element(order_form, self.loc.DEL_BUTTON, timeout=2)
        self.click_element(order_form, self.loc.YES_BUTTON, timeout=2)
        self.click_element(order_form, self.loc.REFRESH_BUTTON_ORDER, timeout=2)

        # 23. Проверка удаление морской перевозки
        self.order_data.update({
            'forwarding_panel': self.get_element_property(order_form, self.loc.DATA_PANEL, "Value"),
        })

        return self.order_data

    def freight(self):
        # 1. Запуск приложения
        startup_window = self.start_application()
        startup_window.set_focus()

        # 2. Нажатие кнопки Запуск
        self.click_element(startup_window, self.loc.START_BUTTON, timeout=1)
        time.sleep(15)

        # 3. Переход в раздел Заказы
        main_window = self.get_main_window()
        main_window.set_focus()
        time.sleep(4)

        self.click_element(main_window, self.loc.ORDERS_TAB, timeout=3)
        time.sleep(5)

        # 4. Открыть заказ заказа
        self.click_element_double(main_window, self.loc.TABLE_ORDER_NUMBER, timeout=5)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)

        # 5. Взять номер заказа
        self.order_data = {
            'order_number': self.get_element_property(order_form, self.loc.ORDER_NUMBER, "Name")
        }

        # 5. Перейти во вкладку
        self.click_element(main_window, self.loc.TAB_FREIGHT, timeout=3)

        # 5 Создать Bulkership
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

        # Во вкладке Перевозки, таблица
        self.order_data.update({
            'freight_order_table': self.get_element_property(order_form, self.loc.FREIGHT_ITEM, "Value")
        })

        # 5. Открыть груз заказа
        self.click_element_double(main_window, self.loc.FREIGHT_ITEM, timeout=5)

        # 5. Переключение на форму груза
        main_window = self.get_freight_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.FREIGHT_FROM)
        time.sleep(1)
        # 5. Проверка полей
        self.order_data.update({
            'freight_order_number': self.get_element_property(order_form, self.loc.ORDER_NUMBER, "Name"),
            'freight_type': self.get_element_property(order_form, self.loc.FREIGHT_TYPE_FORM, "Name"),
            'freight_number': self.get_element_property(order_form, self.loc.FREIGHT_TE_NUMBER_FORM, "Value"),
            'freight_te_type': self.get_element_property(order_form, self.loc.FREIGHT_TE_TYPE, "Value"),
            'freight_priority': self.get_element_property(order_form, self.loc.FREIGHT_TE_QUANTITY_FORM, "Value"),
            'freight_oum': self.get_element_property(order_form, self.loc.FREIGHT_TE_UOM, "Value")
        })

        # 5 Закрыть груз
        self.click_element(order_form, self.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)

        # 5. Удалить Bulkership
        self.click_element(order_form, self.loc.FREIGHT_ITEM, timeout=5)
        self.click_element(order_form, self.loc.DEL_BUTTON, timeout=2)
        self.click_element(order_form, self.loc.YES_BUTTON, timeout=2)
        self.click_element(order_form, self.loc.REFRESH_BUTTON_ORDER, timeout=2)

        # 5 Создать Container
        self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=5)
        self.click_element(main_window, self.loc.FREIGHT_CREATE_TE, timeout=1)
        self.click_element(main_window, self.loc.FREIGHT_CREATE_TE2, timeout=1)
        self.click_element(main_window, self.loc.FREIGHT_CREATE_TYPE, timeout=1)
        self.click_element(main_window, self.loc.FREIGHT_CREATE_TYPE1, timeout=1)
        self.set_text_field(main_window, self.loc.FREIGHT_CREATE_QUANTITY, 1, timeout=1)
        keyboard.send_keys('{ENTER}')  # нажать на ОК работает если есть фокус на кнопке, могут быть проблемы
        time.sleep(1)

        # Во вкладке Перевозки, таблица
        self.order_data1 = {
            'freight_order_table': self.get_element_property(order_form, self.loc.FREIGHT_ITEM, "Value")
        }

        # Во вкладке Перевозки, таблица
        self.order_data.update({
            'freight_order_table_con': self.get_element_property(order_form, self.loc.FREIGHT_ITEM, "Value")
        })

        # 5. Открыть груз заказа
        self.click_element_double(main_window, self.loc.FREIGHT_ITEM, timeout=5)

        # 5. Переключение на форму груза
        main_window = self.get_freight_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.FREIGHT_FROM)
        time.sleep(1)

        # 5. Проверка полей
        self.order_data.update({
            'freight_order_number_con': self.get_element_property(order_form, self.loc.ORDER_NUMBER, "Name"),
            'freight_type_con': self.get_element_property(order_form, self.loc.FREIGHT_TYPE_FORM, "Name"),
            'freight_number_con': self.get_element_property(order_form, self.loc.FREIGHT_TE_NUMBER_FORM, "Value"),
            'freight_te_type_con': self.get_element_property(order_form, self.loc.FREIGHT_TE_TYPE, "Value"),
        })

        # 5 Закрыть груз
        self.click_element(order_form, self.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)

        self.click_element(order_form, self.loc.FREIGHT_ITEM, timeout=5)
        self.click_element(order_form, self.loc.DEL_BUTTON, timeout=2)
        self.click_element(order_form, self.loc.YES_BUTTON, timeout=2)
        self.click_element(order_form, self.loc.REFRESH_BUTTON_ORDER, timeout=2)

        return self.order_data

    def gtd(self):
        # 1. Запуск приложения
        startup_window = self.start_application()
        startup_window.set_focus()

        # 2. Нажатие кнопки Запуск
        self.click_element(startup_window, self.loc.START_BUTTON, timeout=1)
        time.sleep(15)

        # 3. Переход в раздел Заказы
        main_window = self.get_main_window()
        main_window.set_focus()
        time.sleep(4)

        self.click_element(main_window, self.loc.ORDERS_TAB, timeout=3)
        time.sleep(5)

        # 4. Открыть заказ заказа
        self.click_element_double(main_window, self.loc.TABLE_ORDER_NUMBER, timeout=5)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)

        # 5. Взять номер заказа
        self.order_data = {
            'order_number': self.get_element_property(order_form, self.loc.ORDER_NUMBER, "Name")
        }

        # 5. Перейти во вкладку груза
        self.click_element(main_window, self.loc.TAB_FREIGHT, timeout=3)

        # 5 Создать Bulkership
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

        # Во вкладке Перевозки, таблица
        self.order_data.update({
            'freight_order_table': self.get_element_property(order_form, self.loc.FREIGHT_ITEM, "Value")
        })

        # 5. Перейти во вкладку Декларирования
        self.click_element(main_window, self.loc.TAB_GTD, timeout=1)
        self.click_element(main_window, self.loc.ADD_BUTTON, timeout=1)

        # 5. Переключение на форму ГТД
        main_window = self.get_gtd_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.GTD_FROM)
        time.sleep(1)

        self.order_data = {
            'order_client': self.get_element_property(order_form, self.loc.CLIENT_GTD, "Value"),
            'order_number': self.get_element_property(order_form, self.loc.ORDER_GTD, "Value"),
            'procedure_gtd': self.get_element_property(order_form, self.loc.PROCEDURE_GTD, "Value"),
        }

        # 5. Создать ТЕ
        self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=2)

        self.order_data.update({
            'order_number_dialogue': self.get_element_property(order_form, self.loc.DIALOGUE_TEXT, "Name"),
        })

        self.click_element(order_form, self.loc.OPEN_TEXT1, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        self.order_data.update({
            'number_te': self.get_element_property(order_form, self.loc.TE_ORDER_GTD, "Value")
        })
        keyboard.send_keys('{ENTER}')

        # 5. Переключение на форму заказа
        main_window = self.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.app.window(**self.loc.ORDER_FORM)
        time.sleep(1)
        self.click_element(main_window, self.loc.REFRESH_GTD_ORDER, timeout=2)

        self.order_data.update({
            'client_gtd': self.get_element_property(order_form, self.loc.TABLE_CLIENT, "Value"),
            'client_order': self.get_element_property(order_form, self.loc.CLIENT_COMBO, "Value"),
            'number_te_order': self.get_element_property(order_form, self.loc.TE_GTD_ORDER, "Value"),
        })

        self.click_element(order_form, self.loc.TABLE_DELETE, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.click_element(main_window, self.loc.REFRESH_GTD_ORDER, timeout=2)

        self.order_data.update({
            'all_status': self.get_element_property(order_form, self.loc.ALL_STATUS, "Value")
        })
        time.sleep(1)
        return self.order_data


    def close(self):
        """Завершение работы приложения"""
        self.app.kill(soft=True)
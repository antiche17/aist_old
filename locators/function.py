from pywinauto import Application, keyboard
from .locators import LocOrders
import time
import subprocess
import psutil
from pywinauto.keyboard import send_keys
from pywinauto.findwindows import ElementNotFoundError


class Function:
    def __init__(self):
        self.app = Application(backend='uia')
        self.loc = LocOrders()
        self.order_data = {}
        self.process = None
        self.child_pid = None

    def start_application(self):
        # Запускаем приложение
        self.process = subprocess.Popen(r'C:\AIST\WinAIST.exe')
        time.sleep(15)

        # Ищем реальный процесс WinAIST среди дочерних
        parent = psutil.Process(self.process.pid)
        for child in parent.children(recursive=True):
            if 'winaist' in child.name().lower():
                real_pid = child.pid
                break
        else:
            raise Exception("Не найден реальный процесс WinAIST")

        # Подключаемся к реальному процессу
        self.app.connect(process=real_pid)

        # Находим главное окно
        window = self.app.window(auto_id="frmMain")
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

    def get_preforwarding_form(self):
        """Получение главного окна"""
        return self.app.window(**self.loc.PREFORWARDING_FORM)

    def get_auto_form(self):
        """Получение главного окна"""
        return self.app.window(**self.loc.AUTO_FORM)

    def get_jd_form(self):
        """Получение главного окна"""
        return self.app.window(**self.loc.JD_FORM)

    def get_avia_form(self):
        """Получение главного окна"""
        return self.app.window(**self.loc.AVIA_FORM)

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

    def get_product_form(self):
        """Получение главного окна"""
        return self.app.window(**self.loc.PRODUCT_FORM)

    def get_auto_shipment_form(self):
        """Получение главного окна"""
        return self.app.window(**self.loc.AUTO_SHIPMENT_FORM)

    def get_services_form(self):
        """Получение главного окна"""
        return self.app.window(**self.loc.SERVICES_FORM)

    def get_services_form_new(self):
        """Получение главного окна"""
        return self.app.window(**self.loc.SERVICES_FORM_NEW)

    def get_transfer_form(self):
        """Получение главного окна"""
        return self.app.window(**self.loc.TRANSFER_FORM)

    def click_element(self, window, locator, timeout=1.5):
        """Клик по элементу с ожиданием"""
        element = window.child_window(**locator)
        element.wait('visible', timeout=timeout)
        element.click_input()
        return element

    def click_element_sp(self, window, locator):
        """Клик по элементу без ожидания visible"""
        element = window.child_window(**locator)
        element.click_input()
        return element

    def click_element_double(self, window, locator, timeout=1):
        """Клик по элементу с ожиданием"""
        element = window.child_window(**locator)
        element.wait('visible', timeout=timeout)
        element.click_input(double=True)
        return element

    def click_element_double_sp(self, window, locator):
        """Двойной клик по элементу без ожидания visible"""
        element = window.child_window(**locator)
        element.click_input(double=True)
        return element

    def right_click_element(self, window, locator, timeout=1):
        """ПКМ по элементу с ожиданием"""
        element = window.child_window(**locator)
        element.wait('visible', timeout=timeout)
        element.right_click_input()
        return element

    def select_two_elements_with_ctrl(self, window, locator1, locator2, timeout=1):
        # Первый элемент
        el1_spec = window.child_window(**locator1)
        el1_spec.wait('visible', timeout=timeout)
        el1 = el1_spec.wrapper_object()
        time.sleep(1)
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

    def select_range_with_shift(self, window, first_locator, last_locator, timeout=3):
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

    def is_element_present(self, window, locator, timeout=2):
        element = window.child_window(**locator)
        try:
            element.wait('visible', timeout=timeout)
            return True
        except Exception:
            return False


    def set_text_field(self, window, locator, text, timeout=1):
        """Устанавливает текст в текстовое поле"""
        element = window.child_window(**locator)
        element.wait('visible enabled ready', timeout=timeout)
        wrapper = element.wrapper_object()
        wrapper.set_text(str(text))
        return wrapper

    def get_element_property(self, window, locator, property_name, timeout=1):
        """Получение свойства элемента"""
        element = window.child_window(**locator)
        element.wait('visible', timeout=timeout)
        return element.legacy_properties()[property_name]

    def get_element_property_sp(self, window, locator, property_name):
        """Получение свойства элемента без ожидания visible"""
        element = window.child_window(**locator).wrapper_object()

        try:
            # Радиокнопки, чекбоксы, элементы списка
            if property_name in ["SelectionItem.IsSelected", "IsSelected"]:
                return element.iface_selection_item.CurrentIsSelected

            # Значение поля ввода / текста
            elif property_name in ["Value.Value", "Value"]:
                return element.iface_value.CurrentValue

            # Проверка на доступность редактирования
            elif property_name in ["Value.IsReadOnly", "IsReadOnly"]:
                return element.iface_value.CurrentIsReadOnly

            # Для CheckBox и ToggleButton
            elif property_name in ["Toggle.ToggleState", "ToggleState"]:
                return element.iface_toggle.CurrentToggleState

            else:
                # fallback — legacy (AutomationElement)
                props = element.legacy_properties()
                return props.get(property_name, None)

        except Exception as e:
            pass
            return None

    def get_element_value(self, window, locator, timeout=1):
        # Ожидание видимости и готовности элемента
        ctrl = window.child_window(**locator).wait('visible ready', timeout=timeout)
        if hasattr(ctrl, 'wrapper_object'):
            ctrl = ctrl.wrapper_object()

        # Если это ComboBoxWrapper — возвращаем выбранный текст
        if ctrl.friendly_class_name() == 'ComboBox':
            try:
                return ctrl.selected_text()
            except Exception:
                # fallback если по каким-то причинам selected_text() не сработал
                return ctrl.window_text()

        # Попробуем получить значение из свойства "Value"
        try:
            value = ctrl.get_value()
            if value not in (None, ''):
                return value
        except Exception:
            pass

        # Если get_value() не сработал — проверим свойства напрямую
        try:
            props = ctrl.get_properties()
            if 'Value' in props and props['Value'] not in (None, ''):
                return props['Value']
        except Exception:
            pass

        # Если Value не нашли — вернем текст элемента (Name)
        return ctrl.window_text()

    @staticmethod
    def check_element_disappeared(window, locator, timeout=3):
        """
        Проверяет, что элемент исчез (не существует или невидим).
        """
        try:
            element = window.child_window(**locator).wait('exists', timeout=timeout)
            return False  # элемент всё ещё существует
        except Exception:
            return True  # элемент не найден → значит исчез
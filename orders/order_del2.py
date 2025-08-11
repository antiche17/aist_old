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

    def order_del2(self):
        # 1. Запуск приложения
        self.fun.start_application()
        # startup_window.set_focus()

        # 2. Нажатие кнопки Запуск
        # self.fun.click_element(startup_window, self.loc.AIST_EF, timeout=1)
        # self.fun.click_element(startup_window, self.loc.START_BUTTON, timeout=1)
        time.sleep(2)

        # 3. Переход в раздел Заказы
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(2)
        self.fun.click_element(main_window, self.fun.loc.ORDERS_TAB, timeout=3)
        time.sleep(6)

        # 4. Выделение 10 заказа с сущностью
        self.fun.order_data = {
            'order8': self.fun.get_element_property(main_window, self.fun.loc.TABLE_ORDER_NUMBER8, "Value"),
            'order9': self.fun.get_element_property(main_window, self.fun.loc.TABLE_ORDER_NUMBER9, "Value"),
            'order10': self.fun.get_element_property(main_window, self.fun.loc.TABLE_ORDER_NUMBER10, "Value"),
        }
        self.fun.select_range_with_shift(main_window, self.fun.loc.TABLE_ORDER_NUMBER, self.fun.loc.TABLE_ORDER_NUMBER10)
        self.fun.click_element_sp(main_window, self.fun.loc.TABLE_DELETE)
        self.fun.order_data.update({
            'del_window': self.fun.get_element_property(main_window, self.fun.loc.DEL_WINDOW, "Name"),
        })

        self.fun.click_element_sp(main_window, self.fun.loc.DEL_WINDOW_BUTTON)

        # 5. Создание нового заказа
        self.fun.click_element_sp(main_window, self.fun.loc.ADD_BUTTON)
        time.sleep(1)

        # 6. Заполнение формы заказа
        self.fun.click_element_sp(main_window, self.fun.loc.ORDER_TYPE_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.LOGISTICS_ITEM)
        self.fun.click_element_sp(main_window, self.fun.loc.CUSTOMER_COMBO)
        self.fun.click_element_sp(main_window, self.fun.loc.CUSTOMER_ITEM)
        self.fun.click_element_sp(main_window, self.fun.loc.OK_BUTTON)
        time.sleep(1)

        main_window = self.fun.get_main_form()
        main_window.set_focus()

        # 7. В заказе Прикрепить Фаил пока пропускаем

        # 8. В заказе создать ИС
        # 6. Перейти во вкладку
        self.fun.click_element_sp(main_window, self.fun.loc.TAB_CHECK)

        # 7 Создать Исходящий счет и выставить покупателя
        self.fun.click_element_sp(main_window, self.fun.loc.CREATE_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)

        # 8. Переключение на форму ИС
        main_window = self.fun.get_check_form()
        main_window.set_focus()

        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON2)

        # 11. Переключить на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()

        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON_ORDER)

        # 12. Удалить заказ
        self.fun.click_element_sp(main_window, self.loc.OTHER_ACTIONS)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')
        self.fun.click_element_sp(main_window, self.loc.YES_BUTTON)
        self.fun.order_data.update({
            'del_window_is': self.fun.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 12. Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)

        # 13. Удалить ИС
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.TABLE_DELETE)
        self.fun.click_element_sp(main_window, self.loc.YES_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON_ORDER)
        self.fun.order_data.update({
            'del_is': self.fun.get_element_property(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # 14 Создать Входящий счет
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)
        time.sleep(1)
        self.fun.click_element_double(main_window, self.loc.VS_CREATE_ORDER, timeout=1)
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)

        # 7 Переключение на форму ВС
        main_window = self.fun.get_check_vs_form()
        main_window.set_focus()

        self.fun.click_element(main_window, self.loc.OK_BUTTON2)

        # Переключить на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON_ORDER)

        # 12. Удалить заказ
        self.fun.click_element_sp(main_window, self.loc.OTHER_ACTIONS)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        self.fun.click_element_sp(main_window, self.loc.YES_BUTTON)
        self.fun.order_data.update({
            'del_window_vs': self.fun.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 12. Окно удаления заказа
        self.fun.click_element_sp(main_window, self.loc.DEL_WINDOW_BUTTON)

        # 7 Удалить
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.TABLE_DELETE)
        self.fun.click_element_sp(main_window, self.loc.YES_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.REFRESH_BUTTON_ORDER)
        self.fun.order_data.update({
            'del_vs': self.fun.get_element_property(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # 7 Создать Исходящего платежа и выставить покупателя
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)
        time.sleep(1)
        self.fun.click_element_double(main_window, self.loc.IP_CREATE_ORDER, timeout=1)
        self.fun.click_element_sp(main_window, self.loc.CREATE_BUTTON)

        # 7 Переключение на форму ИП
        main_window = self.fun.get_check_ip_form()
        main_window.set_focus()
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON2)

        # Переключить на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()

        self.fun.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=1)

        # 12. Удалить заказ
        self.fun.click_element(main_window, self.loc.OTHER_ACTIONS, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.order_data.update({
            'del_window_ip': self.fun.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 12. Окно удаления заказа
        self.fun.click_element(main_window, self.loc.DEL_WINDOW_BUTTON, timeout=1)

        # 7 Удалить
        self.fun.click_element(main_window, self.loc.RECIPIENT_1, timeout=1)
        self.fun.click_element(main_window, self.loc.TABLE_DELETE, timeout=1)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=1)
        self.fun.order_data.update({
            'del_ip': self.fun.get_element_property(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # 7 Создать Входящий платеж и выставить покупателя
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
        time.sleep(1)
        self.fun.click_element_double(main_window, self.loc.VP_CREATE_ORDER, timeout=1)
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)

        # 7 Переключение на форму ВП
        main_window = self.fun.get_check_vp_form()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element(main_window, self.loc.OK_BUTTON2, timeout=1)

        # Переключить на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)
        self.fun.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=1)

        # 12. Удалить заказ
        self.fun.click_element(main_window, self.loc.OTHER_ACTIONS, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.order_data.update({
            'del_window_vp': self.fun.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 12. Окно удаления заказа
        self.fun.click_element(main_window, self.loc.DEL_WINDOW_BUTTON, timeout=1)

        # 7 Удалить
        self.fun.click_element(main_window, self.loc.RECIPIENT_1, timeout=1)
        self.fun.click_element(main_window, self.loc.TABLE_DELETE, timeout=1)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=1)
        self.fun.order_data.update({
            'del_vp': self.fun.get_element_property(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # В заказе создать Морская перевозка
        # 7. Перейти во вкладку
        self.fun.click_element(main_window, self.loc.TAB_TRANSPORTATION, timeout=3)

        # 8. Создать морскую перевозку
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.TYPE_TRANSPORTATION, timeout=3)
        self.fun.click_element(main_window, self.loc.SEA_TRANSPORTATION, timeout=3)
        keyboard.send_keys('{ENTER}')  # нажать на ОК работает если есть фокус на кнопке, могут быть проблемы

        # 9. Переключится на форму морской перевозки
        main_window = self.fun.get_sea_form()
        main_window.set_focus()
        time.sleep(1)

        # Закрываем морскую перевозку
        self.fun.click_element(main_window, self.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)

        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 12. Удалить заказ
        self.fun.click_element(main_window, self.loc.OTHER_ACTIONS, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.order_data.update({
            'del_window_sea': self.fun.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 12. Окно удаления заказа
        self.fun.click_element(main_window, self.loc.DEL_WINDOW_BUTTON, timeout=1)

        # Удаляем морскую перевозку
        self.fun.click_element(main_window, self.loc.LINE_TRANSPORTATION, timeout=2)
        self.fun.click_element(main_window, self.loc.DEL_BUTTON, timeout=2)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=2)
        self.fun.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=2)
        self.fun.order_data.update({
            'del_sea': self.fun.get_element_property(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # Создаем автоперевозку
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.TYPE_TRANSPORTATION, timeout=3)
        self.fun.click_element(main_window, self.loc.AUTO_TRANSPORTATION, timeout=3)
        keyboard.send_keys('{ENTER}')  # нажать на ОК работает если есть фокус на кнопке, могут быть проблемы

        # 5. Переключится на форму автоперевозку
        main_window = self.fun.get_auto_form()
        main_window.set_focus()
        time.sleep(1)

        # Закрываем морскую перевозку
        self.fun.click_element(main_window, self.loc.SAVE_BUTTON, timeout=2)
        time.sleep(1)
        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 12. Удалить заказ
        self.fun.click_element(main_window, self.loc.OTHER_ACTIONS, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.order_data.update({
            'del_window_auto': self.fun.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 12. Окно удаления заказа
        self.fun.click_element(main_window, self.loc.DEL_WINDOW_BUTTON, timeout=1)

        # Удаляем автоперевозку
        self.fun.click_element(main_window, self.loc.LINE_TRANSPORTATION, timeout=2)
        self.fun.click_element(main_window, self.loc.DEL_BUTTON, timeout=2)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=2)
        self.fun.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=2)
        self.fun.order_data.update({
            'del_auto': self.fun.get_element_property(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # В заказе создать Экспедирование
        # В заказе создать Груз
        # 6. Перейти во вкладку
        self.fun.click_element(main_window, self.loc.TAB_FREIGHT, timeout=2)

        # 7 Создать Bulkership
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TE, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TE1, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TYPE, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TYPE1, timeout=1)
        self.fun.set_text_field(main_window, self.loc.FREIGHT_CREATE_QUANTITY, 1, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_UOM, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_UOM1, timeout=1)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)
        time.sleep(1)

        # 12. Удалить заказ
        self.fun.click_element(main_window, self.loc.OTHER_ACTIONS, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.order_data.update({
            'del_window_bul': self.fun.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 12. Окно удаления заказа
        self.fun.click_element(main_window, self.loc.DEL_WINDOW_BUTTON, timeout=1)

        # 5. Удалить Bulkership
        self.fun.click_element(main_window, self.loc.FREIGHT_ITEM, timeout=5)
        self.fun.click_element(main_window, self.loc.DEL_BUTTON, timeout=2)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=2)
        self.fun.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=2)
        self.fun.order_data.update({
            'del_bul': self.fun.get_element_property(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # 7 Создать Container
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TE, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TE2, timeout=1)
        time.sleep(1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TYPE, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TYPE1, timeout=1)
        self.fun.set_text_field(main_window, self.loc.FREIGHT_CREATE_QUANTITY, 1, timeout=1)
        time.sleep(1)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

        # 12. Удалить заказ
        self.fun.click_element(main_window, self.loc.OTHER_ACTIONS, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.order_data.update({
            'del_window_con': self.fun.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 12. Окно удаления заказа
        self.fun.click_element(main_window, self.loc.DEL_WINDOW_BUTTON, timeout=1)

        # 5. Удалить Container
        self.fun.click_element(main_window, self.loc.LINE_TRANSPORTATION, timeout=1)
        self.fun.click_element(main_window, self.loc.DEL_BUTTON, timeout=2)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=2)
        self.fun.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=2)
        self.fun.order_data.update({
            'del_con': self.fun.get_element_property(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        # В заказе создать ГТД и удалить груз
        # 7. Перейти во вкладку груза
        self.fun.click_element(main_window, self.loc.TAB_FREIGHT, timeout=3)

        # 8 Создать Bulkership
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=5)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TE, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TE1, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TYPE, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_TYPE1, timeout=1)
        self.fun.set_text_field(main_window, self.loc.FREIGHT_CREATE_QUANTITY, 1, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_UOM, timeout=1)
        self.fun.click_element(main_window, self.loc.FREIGHT_CREATE_UOM1, timeout=1)
        keyboard.send_keys('{ENTER}')  # нажать на ОК работает если есть фокус на кнопке, могут быть проблемы
        time.sleep(1)

        # 10. Перейти во вкладку Декларирования
        self.fun.click_element(main_window, self.loc.TAB_GTD, timeout=1)
        self.fun.click_element(main_window, self.loc.ADD_BUTTON, timeout=1)
        time.sleep(2)

        # 11. Переключение на форму ГТД
        main_window = self.fun.get_gtd_form()
        main_window.set_focus()
        time.sleep(1)

        # 12. Прикрепить ТЕ
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
        self.fun.click_element(main_window, self.loc.ADD_TE, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        self.fun.click_element(main_window, self.loc.OK_BUTTON2, timeout=1)

        # 5. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 6. Перейти во вкладку груза
        self.fun.click_element(main_window, self.loc.TAB_FREIGHT, timeout=2)

        # 5. Удалить Bulkership
        self.fun.click_element(main_window, self.loc.FREIGHT_ITEM, timeout=5)
        self.fun.click_element(main_window, self.loc.DEL_BUTTON, timeout=2)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=2)
        self.fun.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=2)

        # 10. Перейти во вкладку Декларирования
        self.fun.click_element(main_window, self.loc.TAB_GTD, timeout=1)
        self.fun.click_element(main_window, self.loc.REFRESH_BUTTON, timeout=2)

        # 12. Удалить заказ
        self.fun.click_element(main_window, self.loc.OTHER_ACTIONS, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=1)
        self.fun.order_data.update({
            'del_window_gtd': self.fun.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 12. Окно удаления заказа
        self.fun.click_element(main_window, self.loc.DEL_WINDOW_BUTTON, timeout=1)

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

        # 21. Переключение на форму заказа
        main_window = self.fun.get_main_form()
        main_window.set_focus()
        time.sleep(1)

        # 12. Удалить заказ
        self.fun.click_element(main_window, self.loc.OTHER_ACTIONS, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=2)
        self.fun.order_data.update({
            'del_window_exp': self.fun.get_element_property(main_window, self.loc.DEL_WINDOW, "Name"),
        })

        # 12. Окно удаления заказа
        self.fun.click_element(main_window, self.loc.DEL_WINDOW_BUTTON, timeout=1)

        # 23. Удаляем Экспедирование
        self.fun.click_element(main_window, self.loc.LINE_TRANSPORTATION, timeout=2)
        self.fun.click_element(main_window, self.loc.DEL_BUTTON, timeout=2)
        self.fun.click_element(main_window, self.loc.YES_BUTTON, timeout=2)
        self.fun.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=2)
        self.fun.order_data.update({
            'del_exp': self.fun.get_element_property(main_window, self.loc.FREIGHT_TOTAL_RECORDS, "Value"),
        })

        return self.fun.order_data

    def close(self):
        """Завершение работы приложения"""
        self.app.kill(soft=True)
Морская

# 9. Добавить маршрут
        self.fun.click_element(main_window, self.loc.TAB_ROUTES, timeout=3)

        # 9. Преэкспедирование
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.ROUTES_WINDOWS, timeout=3)
        self.fun.click_element(main_window, self.loc.PREFORWARDING, timeout=3)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)

        # 9. Отгрузка
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.ROUTES_WINDOWS, timeout=3)
        self.fun.click_element(main_window, self.loc.SHIPMENT, timeout=3)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)

        # 9. Перевалка 1
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.ROUTES_WINDOWS, timeout=3)
        self.fun.click_element(main_window, self.loc.TRANSSHIPMENT1, timeout=3)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)

        # 9. Перевалка 2
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.ROUTES_WINDOWS, timeout=3)
        self.fun.click_element(main_window, self.loc.TRANSSHIPMENT2, timeout=3)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)

        # 9. Прибытие
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.ROUTES_WINDOWS, timeout=3)
        self.fun.click_element(main_window, self.loc.ARRIVAL, timeout=3)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)

        # 9. Порт выставление данных в маршруты
        self.fun.click_element(order_form, self.loc.PORT1, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(order_form, self.loc.PORT1, timeout=1)
        self.fun.click_element(order_form, self.loc.NAME_LINE1, timeout=1)

        time.sleep(2)
        self.fun.click_element(order_form, self.loc.PORT2, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(order_form, self.loc.PORT2, timeout=1)
        self.fun.click_element(order_form, self.loc.NAME_LINE2, timeout=1)

        self.fun.click_element(order_form, self.loc.PORT3, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(order_form, self.loc.PORT3, timeout=1)
        self.fun.click_element(order_form, self.loc.NAME_LINE3, timeout=1)

        self.fun.click_element(order_form, self.loc.PORT4, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(order_form, self.loc.PORT4, timeout=1)
        self.fun.click_element(order_form, self.loc.NAME_LINE4, timeout=1)

        self.fun.click_element(order_form, self.loc.PORT5, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(order_form, self.loc.PORT5, timeout=1)
        self.fun.click_element(order_form, self.loc.NAME_LINE5, timeout=1)

        # 9. Терминал выставление данных в маршруты
        self.fun.click_element(order_form, self.loc.TERMINAL_LINE1, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(order_form, self.loc.TERMINAL_LINE1, timeout=1)
        self.fun.click_element(order_form, self.loc.FREIGHT_CREATE_TE1, timeout=1)

        self.fun.click_element(order_form, self.loc.TERMINAL_LINE2, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(order_form, self.loc.TERMINAL_LINE2, timeout=1)
        self.fun.click_element(order_form, self.loc.FREIGHT_CREATE_TE2, timeout=1)

        self.fun.click_element(order_form, self.loc.TERMINAL_LINE3, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(order_form, self.loc.TERMINAL_LINE3, timeout=1)
        self.fun.click_element(order_form, self.loc.FREIGHT_CREATE_TE3, timeout=1)

        self.fun.click_element(order_form, self.loc.TERMINAL_LINE4, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(order_form, self.loc.TERMINAL_LINE4, timeout=1)
        self.fun.click_element(order_form, self.loc.FREIGHT_CREATE_TE4, timeout=1)

        self.fun.click_element(order_form, self.loc.TERMINAL_LINE5, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(order_form, self.loc.TERMINAL_LINE5, timeout=1)
        self.fun.click_element(order_form, self.loc.FREIGHT_CREATE_TE5, timeout=1)

        # 9. Агент выставление данных в маршруты
        self.fun.click_element(order_form, self.loc.AGENT_LINE1, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(order_form, self.loc.AGENT_LINE1, timeout=1)
        self.fun.click_element(order_form, self.loc.FREIGHT_CREATE_TE1, timeout=1)

        self.fun.click_element(order_form, self.loc.AGENT_LINE2, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(order_form, self.loc.AGENT_LINE2, timeout=1)
        self.fun.click_element(order_form, self.loc.FREIGHT_CREATE_TE2, timeout=1)

        self.fun.click_element(order_form, self.loc.AGENT_LINE3, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(order_form, self.loc.AGENT_LINE3, timeout=1)
        self.fun.click_element(order_form, self.loc.FREIGHT_CREATE_TE3, timeout=1)

        self.fun.click_element(order_form, self.loc.AGENT_LINE4, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(order_form, self.loc.AGENT_LINE4, timeout=1)
        self.fun.click_element(order_form, self.loc.FREIGHT_CREATE_TE4, timeout=1)

        self.fun.click_element(order_form, self.loc.AGENT_LINE5, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(order_form, self.loc.AGENT_LINE5, timeout=1)
        self.fun.click_element(order_form, self.loc.FREIGHT_CREATE_TE5, timeout=1)

        # 9. Судно выставление данных в маршруты
        self.fun.click_element(order_form, self.loc.SHIP_LINE2, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(order_form, self.loc.SHIP_LINE2, timeout=1)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')

        self.fun.click_element(order_form, self.loc.SHIP_LINE3, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(order_form, self.loc.SHIP_LINE3, timeout=1)
        keyboard.send_keys('{DOWN}' *2)
        keyboard.send_keys('{ENTER}')

        self.fun.click_element(order_form, self.loc.SHIP_LINE4, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(order_form, self.loc.SHIP_LINE4, timeout=1)
        keyboard.send_keys('{DOWN}' * 3)

        # 10. Плановая дата отгрузки
        self.fun.click_element(main_window, self.loc.PLAN_LOAD1, timeout=3)
        keyboard.send_keys('1')
        self.fun.click_element(main_window, self.loc.PLAN_LOAD2, timeout=3)
        keyboard.send_keys('2')
        self.fun.click_element(main_window, self.loc.PLAN_LOAD3, timeout=3)
        keyboard.send_keys('3')
        self.fun.click_element(main_window, self.loc.PLAN_LOAD4, timeout=3)
        keyboard.send_keys('4')

        # 10. Фактическая дата отгрузки
        self.fun.click_element(main_window, self.loc.FACT_LOAD1, timeout=3)
        keyboard.send_keys('5')
        self.fun.click_element(main_window, self.loc.FACT_LOAD2, timeout=3)
        keyboard.send_keys('6')
        self.fun.click_element(main_window, self.loc.FACT_LOAD3, timeout=3)
        keyboard.send_keys('7')
        self.fun.click_element(main_window, self.loc.FACT_LOAD4, timeout=3)
        keyboard.send_keys('8')

        # 10. Плановая дата прибытия
        self.fun.click_element(main_window, self.loc.PLAN_ARRIVAL3, timeout=3)
        keyboard.send_keys('9')
        self.fun.click_element(main_window, self.loc.PLAN_ARRIVAL4, timeout=3)
        keyboard.send_keys('10')
        self.fun.click_element(main_window, self.loc.PLAN_ARRIVAL5, timeout=3)
        keyboard.send_keys('11')

        # 10. Фактическая дата прибытия
        self.fun.click_element(main_window, self.loc.FACT_ARRIVAL3, timeout=3)
        keyboard.send_keys('12')
        self.fun.click_element(main_window, self.loc.FACT_ARRIVAL4, timeout=3)
        keyboard.send_keys('13')
        self.fun.click_element(main_window, self.loc.FACT_ARRIVAL5, timeout=3)
        keyboard.send_keys('14')


Авто

# Создаем автоперевозку
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.TYPE_TRANSPORTATION, timeout=3)
        self.fun.click_element(main_window, self.loc.AUTO_TRANSPORTATION, timeout=3)
        keyboard.send_keys('{ENTER}')  # нажать на ОК работает если есть фокус на кнопке, могут быть проблемы

        # 5. Переключится на форму автоперевозки
        main_window = self.fun.get_auto_form()
        main_window.set_focus()
        time.sleep(1)

        order_form = self.fun.app.window(**self.loc.AUTO_FORM)
        time.sleep(1)

        # 9. Добавить маршрут
        self.fun.click_element(main_window, self.loc.TAB_ROUTES, timeout=3)

        # 9. Отгрузка
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.ROUTES_WINDOWS, timeout=3)
        self.fun.click_element(main_window, self.loc.SHIPMENT, timeout=3)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)

        # 9. Прибытие
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.ROUTES_WINDOWS, timeout=3)
        self.fun.click_element(main_window, self.loc.ARRIVAL, timeout=3)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)

        # 9. Сдача контейнера
        self.fun.click_element(main_window, self.loc.CREATE_BUTTON, timeout=3)
        self.fun.click_element(main_window, self.loc.ROUTES_WINDOWS, timeout=3)
        self.fun.click_element(main_window, self.loc.CONTAINER_DELIVERY, timeout=3)
        self.fun.click_element(order_form, self.loc.OK_BUTTON, timeout=1)

        # 9. Адрес добавить
        self.fun.click_element(order_form, self.loc.ADDRESS1, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(order_form, self.loc.ADDRESS1, timeout=1)
        self.fun.click_element(order_form, self.loc.FREIGHT_CREATE_TE1, timeout=1)

        self.fun.click_element(order_form, self.loc.ADDRESS2, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(order_form, self.loc.ADDRESS2, timeout=1)
        self.fun.click_element(order_form, self.loc.FREIGHT_CREATE_TE2, timeout=1)

        # 9. Водитель добавить
        self.fun.click_element(order_form, self.loc.DRIVER, timeout=1)
        keyboard.send_keys('{ENTER}')
        self.fun.click_element(order_form, self.loc.DRIVER, timeout=1)
        self.fun.click_element(order_form, self.loc.NAME_LINE1, timeout=1)

        # 10. Плановая дата отгрузки
        self.fun.click_element(main_window, self.loc.PLAN_LOAD1, timeout=3)
        keyboard.send_keys('1')

        # 10. Фактическая дата отгрузки
        self.fun.click_element(main_window, self.loc.FACT_LOAD1, timeout=3)
        keyboard.send_keys('2')

        # 10. Автомобиль
        self.fun.click_element(main_window, self.loc.AUTO, timeout=3)
        keyboard.send_keys('х777хх 77 rus')
        keyboard.send_keys('{ENTER}')

        # 10. Плановая дата прибытия
        self.fun.click_element(main_window, self.loc.PLAN_ARRIVAL2, timeout=3)
        keyboard.send_keys('3')
        self.fun.click_element(main_window, self.loc.PLAN_ARRIVAL3, timeout=3)
        keyboard.send_keys('4')

        # 10. Фактическая дата прибытия
        self.fun.click_element(main_window, self.loc.FACT_ARRIVAL2, timeout=3)
        keyboard.send_keys('5')
        self.fun.click_element(main_window, self.loc.FACT_ARRIVAL3, timeout=3)
        keyboard.send_keys('6')
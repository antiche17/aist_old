def create_transportation_sea(self):
    """Создание заказа с типом Логистика и заполнение order_data"""
    # 1. Запуск приложения
    startup_window = self.start_application()
    startup_window.set_focus()

    # 2. Нажатие кнопки Запуск
    self.click_element(startup_window, self.loc.START_BUTTON, timeout=1)
    time.sleep(15)

    # 3. Переход в таблицу Морские перевозки
    main_window = self.get_main_window()
    main_window.set_focus()
    time.sleep(4)

    self.click_element(main_window, self.loc.SEA_TAB, timeout=3)
    time.sleep(3)

    # 4. Создаём морскую перевозку
    self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
    self.click_element(main_window, self.loc.CLIENT_COMBO, timeout=1)
    self.click_element(main_window, self.loc.CUSTOMER_ITEM, timeout=1)
    self.click_element(main_window, self.loc.ORDER_SELECT, timeout=1)
    self.click_element(main_window, self.loc.SEA_TAB_ORDER_NUMBER, timeout=1)

    self.order_data = {
        'sea_type': self.get_element_property(main_window, self.loc.FREIGHT_TYPE_FORM, "Value"), +
        'sea_client': self.get_element_property(main_window, self.loc.CLIENT_COMBO, "Value"),
        'sea_number': self.get_element_property(main_window, self.loc.ORDER_SELECT, "Value"),
        'sea_otv': self.get_element_property(main_window, self.loc.RESPONSIBLE_COMBO, "Value"),
    }

    keyboard.send_keys('{ENTER}')
    time.sleep(1)



    # 5. Открылась форма морская перевозка
    main_window = self.get_sea_form()
    main_window.set_focus()
    time.sleep(2)

    # 8. Проверки
    self.order_data.update({
        'sea_form': self.get_element_property(main_window, self.loc.FORM_FORM, "Name"),
        'sea_navigation': self.get_element_property(main_window, self.loc.ORDER_NUMBER, "Value"),
        'sea_type_form': self.get_element_property(main_window, self.loc.SEA_TYPE_TEXT, "Name"),+
        'sea_status_form': self.get_element_property(main_window, self.loc.STATUS_COMBO, "Value"),
        'sea_priority_form': self.get_element_property(main_window, self.loc.PRIORITY_COMBO, "Value"),
        'sea_otv_form': self.get_element_property(main_window, self.loc.RESPONSIBLE_COMBO, "Value"),

        'sea_type_freight_form': self.get_element_property(main_window, self.loc.TYPE_FREIGHT, "Value"),
        'sea_class_freight_form': self.get_element_property(main_window, self.loc.CLASS_FREIGHT, "Value"),
        'sea_loading_form': self.get_element_property(main_window, self.loc.DOWNLOAD_METHOD, "Value"),
        'sea_reference_freight_form': self.get_element_property(main_window, self.loc.REFERENCE_FREIGHT, "Value"),

        'sea_tab_info': self.get_element_property(main_window, self.loc.TAB_INFO, "Name"),
        'sea_tab_routes': self.get_element_property(main_window, self.loc.TAB_ROUTES, "Name"),
        'sea_tab_freight': self.get_element_property(main_window, self.loc.TAB_FREIGHT, "Name"),
        'sea_tab_services': self.get_element_property(main_window, self.loc.TAB_SERVICES, "Name"),
        'sea_tab_file': self.get_element_property(main_window, self.loc.TAB_FILE, "Name"),

        'sea_tab_create_date': self.get_element_property(main_window, self.loc.CREATE_DATE, "Name"),
        'sea_tab_mod_date': self.get_element_property(main_window, self.loc.MOD_DATE, "Name"),
        'sea_tab_finish': self.get_element_property(main_window, self.loc.COMPLETION_DATE, "Name"),

        'sea_tab_booking_ref': self.get_element_property(main_window, self.loc.BOOKING_REFERENCE, "Value"),
        'sea_tab_ocean_line': self.get_element_property(main_window, self.loc.OCEAN_LINE, "Value"),
        'sea_tab_ocean_kon': self.get_element_property(main_window, self.loc.OCEAN_KONOSAMENT, "Value"),
        'sea_tab_feeder_line': self.get_element_property(main_window, self.loc.FEEDER_LINE, "Value"),
        'sea_tab_feeder_kon': self.get_element_property(main_window, self.loc.FEEDER_KONOSAMENT, "Value"),

        'sea_tab_note_sea': self.get_element_property(main_window, self.loc.NOTE_SEA, "Value"),
    })

    # 7. Редактируем поля Морскую перевозку
    self.click_element(main_window, self.loc.STATUS_COMBO, timeout=1)
    self.click_element(main_window, self.loc.STATUS_COMBO_FINISH, timeout=1)
    self.click_element(main_window, self.loc.PRIORITY_COMBO, timeout=1)
    self.click_element(main_window, self.loc.PRIORITY_COMBO_HIGH, timeout=1)
    self.click_element(main_window, self.loc.TYPE_FREIGHT, timeout=1)
    self.click_element(main_window, self.loc.LINE_TRANSPORTATION, timeout=1)
    self.click_element(main_window, self.loc.CLASS_FREIGHT, timeout=1)
    self.click_element(main_window, self.loc.CLASS_FREIGHT1, timeout=1)
    self.click_element(main_window, self.loc.DOWNLOAD_METHOD, timeout=1)
    self.click_element(main_window, self.loc.DOWNLOAD_METHOD1, timeout=1)
    self.set_text_field(main_window, self.loc.REFERENCE_FREIGHT, "Привет, мир!", timeout=1)

    self.set_text_field(main_window, self.loc.BOOKING_REFERENCE, "1Привет, мир!", timeout=1)
    self.click_element(main_window, self.loc.OCEAN_LINE, timeout=1)
    self.click_element(main_window, self.loc.LINE_TRANSPORTATION, timeout=1)
    self.set_text_field(main_window, self.loc.OCEAN_KONOSAMENT, "2Привет, мир!", timeout=1)
    self.click_element(main_window, self.loc.FEEDER_LINE, timeout=1)
    self.click_element(main_window, self.loc.FEEDER_LINE1, timeout=1)
    self.set_text_field(main_window, self.loc.FEEDER_KONOSAMENT, "3Привет, мир!", timeout=1)

    self.set_text_field(main_window, self.loc.NOTE_SEA, "Привет, наш огромный дивный мир! 666 ", timeout=1)

    # 8. Перейти в вкладку Маршруты
    self.click_element(main_window, self.loc.TAB_ROUTES, timeout=1)

    # 9. Преэкспедирование
    self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
    self.click_element(main_window, self.loc.ROUTES_WINDOWS, timeout=1)
    self.click_element(main_window, self.loc.PREFORWARDING, timeout=1)
    self.click_element(main_window, self.loc.PREFORWARDING_PORT, timeout=1)
    self.click_element(main_window, self.loc.PREFORWARDING_PORT1, timeout=1)
    self.click_element(main_window, self.loc.PREFORWARDING_TERMINAL, timeout=1)
    self.click_element(main_window, self.loc.LINE_TRANSPORTATION, timeout=1)
    self.click_element(main_window, self.loc.PREFORWARDING_AGENT, timeout=1)
    self.click_element(main_window, self.loc.LINE_TRANSPORTATION, timeout=1)
    self.click_element(main_window, self.loc.PREFORWARDING_DATA, timeout=1)
    time.sleep(1)
    keyboard.send_keys('1')
    self.set_text_field(main_window, self.loc.NOTE1, "Преэкспедирование", timeout=1)

    # 10. Проверки, сбор выставленных данных
    self.order_data.update({
        'sea_dialog_preforwarding': self.get_element_property(main_window, self.loc.ROUTES_WINDOWS, "Value"),
        'sea_dialog_port': self.get_element_property(main_window, self.loc.PREFORWARDING_PORT, "Value"),
        'sea_dialog_terminal': self.get_element_property(main_window, self.loc.PREFORWARDING_TERMINAL, "Value"),
        'sea_dialog_agent': self.get_element_property(main_window, self.loc.PREFORWARDING_AGENT, "Value"),
        'sea_dialog_data': self.get_element_property(main_window, self.loc.PREFORWARDING_DATA, "Value"),
        'sea_dialog_note': self.get_element_property(main_window, self.loc.NOTE1, "Value"),
    })

    self.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

    # 11. Переключится на форму маршрута морской перевозки
    main_window = self.get_preforwarding_form()
    main_window.set_focus()
    time.sleep(1)

    # 12. Добавить фактическую дату
    self.click_element(main_window, self.loc.SHIPMENT_DATA_FACT, timeout=1)
    time.sleep(1)
    keyboard.send_keys('2')
    self.click_element(main_window, self.loc.NOTE, timeout=1)

    # 13. Взять фактическую дату
    self.order_data.update({
        'sea_fact_data': self.get_element_property(main_window, self.loc.SHIPMENT_DATA_FACT, "Value")
    })

    self.click_element(main_window, self.loc.SAVE_BUTTON, timeout=1)

    # 13. Переключится на форму морской перевозки
    main_window = self.get_sea_form()
    main_window.set_focus()
    time.sleep(1)

    # 14. Открыть Преэкспедирование
    self.click_element_double(main_window, self.loc.RECIPIENT_1, timeout=1)

    # 15. Переключится на форму маршрута морской перевозки
    main_window = self.get_preforwarding_form()
    main_window.set_focus()
    time.sleep(1)

    # 16. Проверки, сохраненные данные
    self.order_data.update({
        'sea_form_navigation': self.get_element_property(main_window, self.loc.ORDER_NUMBER, "Value"),
        'sea_form_port': self.get_element_property(main_window, self.loc.PREFORWARDING_PORT, "Value"),
        'sea_form_terminal': self.get_element_property(main_window, self.loc.PREFORWARDING_TERMINAL1, "Value"),
        'sea_form_agent': self.get_element_property(main_window, self.loc.PREFORWARDING_AGENT1, "Value"),
        'sea_form_data': self.get_element_property(main_window, self.loc.PREFORWARDING_DATA1, "Value"),
        'sea_form_fact_data': self.get_element_property(main_window, self.loc.SHIPMENT_DATA_FACT, "Value"),
        'sea_form_note': self.get_element_property(main_window, self.loc.NOTE, "Value"),
    })

    Преэкспедирование == Преэкспедирование
    порт == порт
    тесминал == терминал
    агент == агент
    пусто судно
    план дата == план дата
    факт дата == факт дата
    план дата пуст
    дата пуст
    создан дата

    # 11. Отгрузка
    self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
    self.click_element(main_window, self.loc.ROUTES_WINDOWS, timeout=1)
    self.click_element(main_window, self.loc.SHIPMENT, timeout=1)
    self.click_element(main_window, self.loc.PREFORWARDING_PORT, timeout=1)
    self.click_element(main_window, self.loc.PREFORWARDING_PORT2, timeout=1)
    self.click_element(main_window, self.loc.PREFORWARDING_TERMINAL, timeout=1)
    self.click_element(main_window, self.loc.FEEDER_LINE1, timeout=1)
    self.click_element(main_window, self.loc.PREFORWARDING_AGENT, timeout=1)
    self.click_element(main_window, self.loc.FEEDER_LINE1, timeout=1)
    self.click_element(main_window, self.loc.SHIP, timeout=1)
    self.press_down_multiple_times(1)
    keyboard.send_keys('{ENTER}')
    self.click_element(main_window, self.loc.SHIPMENT_DATA, timeout=1)
    time.sleep(1)
    keyboard.send_keys('3')
    self.click_element(main_window, self.loc.NOTE1, timeout=1)
    self.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

    # 8. Проверки
    == Маршрутоное    задание
    Преэкспедирование    взять
    Порт    взять
    терминал    взять
    Агент
    взять судно
    взять    дату
    пусто    дата

    # 9. Переключится на форму маршрута морской перевозки
    main_window = self.get_preforwarding_form()
    main_window.set_focus()
    time.sleep(1)

    self.click_element(main_window, self.loc.SHIPMENT_DATA_FACT, timeout=1)
    time.sleep(1)
    keyboard.send_keys('4')
    self.set_text_field(main_window, self.loc.NOTE, "Отгрузка", timeout=1)

    # 8. Проверки
    взять    дата

    self.click_element(main_window, self.loc.SAVE_BUTTON, timeout=1)

    # 10. Открылась форма морская перевозка
    main_window = self.get_sea_form()
    main_window.set_focus()
    time.sleep(1)

    # 8. Проверки
    Преэкспедирование == Преэкспедирование
    порт == порт
    тесминал == терминал
    агент == агент
    пусто судно
    план дата == план    дата
    факт    дата == факт    дата
    дата
    дата
    пуст дата
    пуст дата
    создан    дата

    # 8. Перевалка 1
    self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
    self.click_element(main_window, self.loc.ROUTES_WINDOWS, timeout=1)
    self.click_element(main_window, self.loc.TRANSSHIPMENT1, timeout=1)
    self.click_element(main_window, self.loc.PREFORWARDING_PORT, timeout=1)
    self.click_element(main_window, self.loc.PREFORWARDING_PORT3, timeout=1)
    self.click_element(main_window, self.loc.PREFORWARDING_TERMINAL, timeout=1)
    self.click_element(main_window, self.loc.FEEDER_LINE3, timeout=1)
    self.click_element(main_window, self.loc.PREFORWARDING_AGENT, timeout=1)
    self.click_element(main_window, self.loc.FEEDER_LINE3, timeout=1)
    self.click_element(main_window, self.loc.SHIP, timeout=1)
    self.press_down_multiple_times(2)
    keyboard.send_keys('{ENTER}')
    self.click_element(main_window, self.loc.ARRIVAL_DATA, timeout=1)
    time.sleep(1)
    keyboard.send_keys('5')
    self.click_element(main_window, self.loc.SHIPMENT_DATA, timeout=1)
    time.sleep(1)
    keyboard.send_keys('6')
    self.click_element(main_window, self.loc.NOTE1, timeout=1)
    self.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

    # 5. Переключится на форму маршрута
    main_window = self.get_preforwarding_form()
    main_window.set_focus()
    time.sleep(1)

    # 8. Проверки
    == Маршрутоное    задание
    Преэкспедирование
    взять     Порт
    взять    терминал
    взять    Агент
    взять    судно
    взять    дату
    пусто    дата
    взять    дату
    пусто3    дата

    self.click_element(main_window, self.loc.ARRIVAL_DATA_FACT, timeout=1)
    time.sleep(1)
    keyboard.send_keys('7')
    self.click_element(main_window, self.loc.SHIPMENT_DATA_FACT, timeout=1)
    time.sleep(1)
    keyboard.send_keys('8')

    # 8. Проверки
    дата
    дата

    self.set_text_field(main_window, self.loc.NOTE, "Перевалка1", timeout=1)
    self.click_element(main_window, self.loc.SAVE_BUTTON, timeout=1)

    # 8. Проверки
    Преэкспедирование == Преэкспедирование
    порт == порт
    тесминал == терминал
    агент == агент
    пусто    судно
    план    дата == план    дата
    факт    дата == факт    дата
    дата
    дата
    дата
    создандата

    # 8. Открылась форма морская перевозка
    main_window = self.get_sea_form()
    main_window.set_focus()
    time.sleep(1)

    # 8. Проверки

    # 8. Перевалка 2
    self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
    self.click_element(main_window, self.loc.ROUTES_WINDOWS, timeout=1)
    self.click_element(main_window, self.loc.TRANSSHIPMENT2, timeout=1)

    self.click_element(main_window, self.loc.PREFORWARDING_PORT, timeout=1)
    self.click_element(main_window, self.loc.PREFORWARDING_PORT4, timeout=1)
    self.click_element(main_window, self.loc.PREFORWARDING_TERMINAL, timeout=1)
    self.click_element(main_window, self.loc.FEEDER_LINE4, timeout=1)
    self.click_element(main_window, self.loc.PREFORWARDING_AGENT, timeout=1)
    self.click_element(main_window, self.loc.FEEDER_LINE4, timeout=1)
    self.click_element(main_window, self.loc.SHIP, timeout=1)
    self.press_down_multiple_times(3)
    keyboard.send_keys('{ENTER}')
    self.click_element(main_window, self.loc.ARRIVAL_DATA, timeout=1)
    time.sleep(1)
    keyboard.send_keys('9')
    self.click_element(main_window, self.loc.SHIPMENT_DATA, timeout=1)
    time.sleep(1)
    keyboard.send_keys('10')
    self.click_element(main_window, self.loc.NOTE1, timeout=1)
    self.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

    # 5. Переключится на форму маршрута
    main_window = self.get_preforwarding_form()
    main_window.set_focus()
    time.sleep(1)

    # 8.проверки
    == Маршрутоное    задание
    Преэкспедирование
    взять    Порт
    взять    терминал
    взять    Агент
    взять    судно
    взять    дату
    пусто    дата
    взять    дату
    пусто    дата


    self.click_element(main_window, self.loc.ARRIVAL_DATA_FACT, timeout=1)
    time.sleep(1)
    keyboard.send_keys('11')
    self.click_element(main_window, self.loc.SHIPMENT_DATA_FACT, timeout=1)
    time.sleep(1)
    keyboard.send_keys('12')

    дата
    дата


    self.set_text_field(main_window, self.loc.NOTE, "Перевалка1", timeout=1)
    self.click_element(main_window, self.loc.SAVE_BUTTON, timeout=1)

    # 8. Проверки

    # 8. Открылась форма морская перевозка
    main_window = self.get_sea_form()
    main_window.set_focus()
    time.sleep(1)

    # 8. Проверки
    Преэкспедирование == Преэкспедирование
    порт == порт
    тесминал == терминал
    агент == агент
    пусто
    судно
    план
    дата == план
    дата
    факт
    дата == факт
    дата
    дата
    дата
    дата
    создандата

    # 8. Прибытие
    self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)
    self.click_element(main_window, self.loc.ROUTES_WINDOWS, timeout=1)
    self.click_element(main_window, self.loc.ARRIVAL, timeout=1)
    self.click_element(main_window, self.loc.PREFORWARDING_PORT, timeout=1)
    self.click_element(main_window, self.loc.PREFORWARDING_PORT5, timeout=1)
    self.click_element(main_window, self.loc.PREFORWARDING_TERMINAL, timeout=1)
    self.click_element(main_window, self.loc.FEEDER_LINE5, timeout=1)
    self.click_element(main_window, self.loc.PREFORWARDING_AGENT, timeout=1)
    self.click_element(main_window, self.loc.FEEDER_LINE5, timeout=1)
    self.click_element(main_window, self.loc.ARRIVAL_DATA, timeout=1)
    time.sleep(1)
    keyboard.send_keys('13')
    self.click_element(main_window, self.loc.NOTE1, timeout=1)
    self.click_element(main_window, self.loc.OK_BUTTON, timeout=1)

    # 5. Переключится на форму маршрута
    main_window = self.get_preforwarding_form()
    main_window.set_focus()
    time.sleep(1)

    self.click_element(main_window, self.loc.ARRIVAL_DATA_FACT, timeout=1)
    time.sleep(1)
    keyboard.send_keys('14')
    self.click_element(main_window, self.loc.UNLOADING, timeout=1)
    time.sleep(1)
    keyboard.send_keys('15')
    self.set_text_field(main_window, self.loc.NOTE, "Отгрузка", timeout=1)
    self.click_element(main_window, self.loc.SAVE_BUTTON, timeout=1)

    # 8. Проверки

    # 8. Открылась форма морская перевозка
    main_window = self.get_sea_form()
    main_window.set_focus()
    time.sleep(1)

    # 8. Проверки

    # 9. Перейти на вкладку Грузы
    self.click_element(main_window, self.loc.TAB_FREIGHT, timeout=1)

    # 5 Создать Bulkership
    self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=2)

    self.click_element(main_window, self.loc.ADD_TE, timeout=1)
    self.click_element(main_window, self.loc.OPEN_BUTTON, timeout=1)
    self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)

    self.click_element(main_window, self.loc.FREIGHT_CREATE_TE, timeout=1)
    self.click_element(main_window, self.loc.FREIGHT_CREATE_TE1, timeout=1)
    self.click_element(main_window, self.loc.FREIGHT_CREATE_TYPE, timeout=1)
    self.click_element(main_window, self.loc.FREIGHT_CREATE_TYPE1, timeout=1)
    self.set_text_field(main_window, self.loc.FREIGHT_CREATE_QUANTITY, 1, timeout=1)
    self.click_element(main_window, self.loc.FREIGHT_CREATE_UOM, timeout=1)
    self.click_element(main_window, self.loc.FREIGHT_CREATE_UOM1, timeout=1)
    keyboard.send_keys('{ENTER}')  # нажать на ОК работает если есть фокус на кнопке, могут быть проблемы
    time.sleep(1)

    self.click_element(main_window, self.loc.ADD_TE, timeout=1)
    keyboard.send_keys('{DOWN}')
    time.sleep(1)
    keyboard.send_keys('{ENTER}')

    # 5. Удалить Bulkership
    self.click_element(main_window, self.loc.FREIGHT_ITEM, timeout=5)
    self.click_element(main_window, self.loc.DEL_BUTTON, timeout=2)
    self.click_element(main_window, self.loc.YES_BUTTON, timeout=2)
    self.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=2)

    # 5 Создать Container
    self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=2)

    self.click_element(main_window, self.loc.ADD_TE, timeout=1)
    self.click_element(main_window, self.loc.OPEN_BUTTON, timeout=1)
    self.click_element(main_window, self.loc.CREATE_BUTTON, timeout=1)

    self.click_element(main_window, self.loc.FREIGHT_CREATE_TE, timeout=1)
    self.click_element(main_window, self.loc.FREIGHT_CREATE_TE2, timeout=1)
    self.click_element(main_window, self.loc.FREIGHT_CREATE_TYPE, timeout=1)
    self.click_element(main_window, self.loc.FREIGHT_CREATE_TYPE1, timeout=1)
    self.set_text_field(main_window, self.loc.FREIGHT_CREATE_QUANTITY, 1, timeout=1)
    keyboard.send_keys('{ENTER}')  # нажать на ОК работает если есть фокус на кнопке, могут быть проблемы
    time.sleep(1)

    self.click_element(main_window, self.loc.ADD_TE, timeout=1)
    keyboard.send_keys('{DOWN}')
    time.sleep(1)
    keyboard.send_keys('{ENTER}')

    # 5. Удалить Container
    self.click_element(main_window, self.loc.FREIGHT_ITEM, timeout=5)
    self.click_element(main_window, self.loc.DEL_BUTTON, timeout=2)
    self.click_element(main_window, self.loc.YES_BUTTON, timeout=2)
    self.click_element(main_window, self.loc.REFRESH_BUTTON_ORDER, timeout=2)

    return self.order_data
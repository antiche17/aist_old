class LocOrders:
    # Основные окна
    START_WINDOW = {'auto_id': 'frmSplash'}
    MAIN_WINDOW = {'auto_id': 'frmMain'}
    ORDER_FORM = {'auto_id': 'OrderForm'}
    SEA_FORM = {'auto_id': 'SeaCarriageForm', 'control_type': "Window", 'found_index': 0}
    SEA_FORM1 = {'title': "Морская перевозка: Создание", 'auto_id': 'SeaCarriageForm', 'control_type': "Window", 'found_index': 0}
    AUTO_FORM = {'auto_id': 'CarCarriageForm'}
    FORWARDING_FROM = {'auto_id': 'ExpeditionForm'}
    FREIGHT_FROM = {'auto_id': 'CargoForm'}
    PREFORWARDING_FORM = {'auto_id': 'RouteSeaCarriageForm'}
    FORM_FORM = {'auto_id': 'TitleBar', 'control_type': "TitleBar"}

    # Кнопки и элементы управления
    START_BUTTON = {'auto_id': 'btnStart', 'title': 'Запуск', 'control_type': 'Button'}
    ORDERS_TAB = {'title': "Заказы", 'control_type': "ListItem"}
    ADD_BUTTON = {'title': "Добавить", 'control_type': "Button"}
    CREATE_BUTTON = {'title': "Создать", 'control_type': "Button"}
    OPEN_BUTTON = {'title': "Открыть", 'control_type': "Button"}

    # Элементы таблицы заказов
    REFRESH_BUTTON = {'title': "Элемент", 'control_type': "SplitButton"}
    TABLE_ORDER_NUMBER = {'title': "Заказ № строка 1", 'control_type': "DataItem"}
    TABLE_ORDER_NUMBER_2 = {'title': "Заказ № строка 2", 'control_type': "DataItem"}
    TABLE_ORDER_TYPE = {'title': "Тип заказа строка 1", 'control_type': "DataItem"}
    TABLE_STATUS = {'title': "Статус строка 1", 'control_type': "DataItem"}
    TABLE_PRIORITY = {'title': "Приоритет строка 1", 'control_type': "DataItem"}
    TABLE_CREATOR = {'title': "Кем создан строка 1", 'control_type': "DataItem"}
    TABLE_CLIENT = {'title': "Клиент строка 1", 'control_type': "DataItem"}
    TABLE_DELETE = {'title': "Удалить", 'control_type': "Button"}
    TABLE_DELETE_WINDOW = {'title': "OK", 'auto_id': "btnOK"}
    TABLE_RECIPIENT = {'title': "Получатель строка 1", 'control_type': "DataItem"}
    TABLE_DELIVERY = {'title': "Условия поставки строка 1", 'control_type': "DataItem"}
    TABLE_NOTE = {'title': "Примечание строка 1", 'control_type': "DataItem"}
    TABLE_DATE = {'title': "Создан строка 1", 'control_type': "DataItem"}

    # Форма создания заказа
    ORDER_TYPE_COMBO = {'auto_id': "orderTypeEdit", 'title': "Тип заказа:", 'control_type': "ComboBox"}
    LOGISTICS_ITEM = {'title': "Логистика", 'control_type': "ListItem"}
    LOGISTICS_ITEM_DR = {'title': "Другие услуги", 'control_type': "ListItem"}
    CUSTOMER_COMBO = {'auto_id': "customerEdit", 'title': "Клиент:", 'control_type': "ComboBox"}
    CUSTOMER_ITEM = {'title': "Наименование строка 1", 'control_type': "DataItem"}
    OK_BUTTON = {'title': "ОК", 'control_type': "Button", 'found_index': 0}
    SAVE_BUTTON = {'auto_id': "sbSave", 'control_type': "Button"}

    # Элементы информации о заказе
    ORDER_NUMBER = {'auto_id': "bceNavigation", 'control_type': "ComboBox"}
    ORDER_TYPE_TEXT = {'auto_id': "lbType", 'control_type': "Text"}
    STATUS_COMBO = {'title': "Статус:", 'control_type': "ComboBox"}
    STATUS_FINISH = {'title': "Завершено", 'control_type': "ListItem"}
    STATUS_COMBO_CANCEL = {'title': "Отменен", 'control_type': "ListItem"}
    STATUS_COMBO_FINISH = {'title': "Завершена", 'control_type': "ListItem"}
    PRIORITY_COMBO = {'title': "Приоритет:", 'control_type': "ComboBox"}
    PRIORITY_COMBO_KRIT = {'title': "Критический", 'control_type': "ListItem"}
    PRIORITY_COMBO_LOW = {'title': "Низкий", 'control_type': "ListItem"}
    PRIORITY_COMBO_HIGH = {'title': "Высокий", 'control_type': "ListItem"}
    RESPONSIBLE_COMBO = {'title': "Ответственный:", 'control_type': "ComboBox", 'found_index': 0}
    CLIENT_COMBO = {'auto_id': "sleClient", 'control_type': "ComboBox"}
    CLIENT_COMBO_3 = {'title': "Наименование строка 3", 'control_type': "DataItem"}
    SENDERS_1 = {'title': "Отправители:", 'control_type': "ComboBox"}
    RECIPIENT = {'title': "Получатель:", 'auto_id': "sleReceiver"}
    RECIPIENT_1 = {'title': "Строка 1", 'control_type': "ListItem"}
    DELIVERY_CONDITION = {'title': "Условия поставки:", 'auto_id': "leIncoterms"}
    DELIVERY_CONDITION_0 = {'title': "Строка 0", 'control_type': "Custom"}
    REFERENCE = {'title': "Референс клиента:", 'auto_id': "teClientReference"}
    NOTE = {'title': "Примечание:", 'auto_id': "meDescription"}
    NOTE1 = {'title': "Примечание:", 'auto_id': "meDecription"}
    NOTE_SEA = {'title': "Примечание:", 'auto_id': "decriptionMemoEdit"}
    MOD_DATE = {'control_type': "Text", 'auto_id': "lblModified"}
    CREATE_DATE = {'control_type': "Text", 'auto_id': "lblCreatedOn"}
    LINE_TRANSPORTATION = {'title': "Строка 1", 'control_type': "ListItem"}
    DEL_BUTTON = {'title': "Удалить", 'control_type': "Button"}
    YES_BUTTON = {'title': "Да", 'control_type': "Button"}
    REFRESH_BUTTON_ORDER = {'title': "Обновить", 'control_type': "Button"}
    COMPLETION_DATE = {'title': "...", 'control_type': "Text", 'auto_id': "lblCompletedOn"}

    # Вкладки
    TAB_INFO = {'title': "Информация", 'control_type': "TabItem"}
    TAB_ROUTES = {'title': "Маршрут", 'control_type': "TabItem"}
    TAB_CHECK = {'title': "Счета", 'control_type': "TabItem"}
    TAB_FILE = {'title': "Файлы", 'control_type': "TabItem"}
    TAB_SERVICES = {'title': "Услуги", 'control_type': "TabItem"}
    TAB_FREIGHT = {'title': "Груз", 'control_type': "TabItem"}
    TAB_TRANSPORTATION = {'title': "Перевозки", 'control_type': "TabItem"}
    TAB_FORWARDING = {'title': "Экспедирование", 'control_type': "TabItem"}
    TAB_GTD = {'title': "Декларирование", 'control_type': "TabItem"}
    TAB_TRACKING = {'title': "Отслеживание", 'control_type': "TabItem"}
    TAB_FORWARDING_FREIGHT = {'title': "Экспедируемый груз", 'control_type': "TabItem"}

    # Перевозки вкладка в заказе
    TYPE_TRANSPORTATION = {'title': "Тип перевозки:", 'control_type': "ComboBox", 'auto_id': "carriageTypeEdit"}
    SEA_TRANSPORTATION = {'title': "Морская перевозка", 'control_type': "ListItem"}
    SEA_ORDER_NAME = {'title': "Морская перевозка: Новая морская перевозка", 'control_type': "SplitButton"}
    SEA_TYPE_TEXT = {'auto_id': "labelControl1", 'control_type': "Text"}
    AUTO_TRANSPORTATION = {'title': "Автоперевозка", 'control_type': "ListItem"}
    AUTO_NAME_TRANSPORTATION = {'auto_id': "bceNavigation", 'control_type': "ComboBox"}
    AUTO_TYPE_TEXT = {'auto_id': "lbType", 'control_type': "Text"}
    TRANSPORTATION_ITEM = {'title': "Тип перевозки строка 1", 'control_type': "DataItem"}
    SEA_TAB = {'title': "Морские перевозки", 'control_type': "ListItem"}
    ORDER_SELECT = {'title': "Заказ:", 'control_type': "ComboBox"}
    SEA_TAB_ORDER_NUMBER = {'title': "Заказ строка 1", 'control_type': "DataItem", 'found_index': 0}
    TYPE_FREIGHT = {'title': "Тип груза:", 'control_type': "ComboBox", 'auto_id': "carriageCargoTypeEdit1"}
    CLASS_FREIGHT = {'title': "Класс груза:", 'control_type': "ComboBox", 'auto_id': "wareClassEdit"}
    CLASS_FREIGHT1 = {'title': "IMO Cargo", 'control_type': "ListItem"}
    DOWNLOAD_METHOD = {'title': "Способ загрузки:", 'control_type': "ComboBox"}
    DOWNLOAD_METHOD1 = {'title': "FCL", 'control_type': "ListItem"}
    REFERENCE_FREIGHT = {'control_type': "Edit", 'auto_id': "teCargoReference"}
    BOOKING_REFERENCE = {'title': "Букинг референс:", 'control_type': "Edit"}
    OCEAN_LINE = {'title': "Океанская линия:", 'control_type': "ComboBox"}
    OCEAN_KONOSAMENT = {'control_type': "Edit", 'auto_id': "oceanBillOfLadingTextBox"}
    FEEDER_LINE = {'title': "Фидерная линия:", 'control_type': "ComboBox"}
    FEEDER_LINE1 = {'title': "Строка 2", 'control_type': "ListItem"}
    FEEDER_LINE3 = {'title': "Строка 3", 'control_type': "ListItem"}
    FEEDER_LINE4 = {'title': "Строка 4", 'control_type': "ListItem"}
    FEEDER_LINE5 = {'title': "Строка 5", 'control_type': "ListItem"}
    FEEDER_KONOSAMENT = {'title': "Фидерн. коносамент:", 'control_type': "Edit"}



    ROUTES_WINDOWS = {'title': "Тип задания:", 'control_type': "ComboBox", 'auto_id': "routeAssignmentSeaCarriageEdit1"}
    PREFORWARDING = {'title': "Преэкспедирование", 'control_type': "ListItem"}
    PREFORWARDING_PORT = {'title': "Порт:", 'control_type': "ComboBox", 'auto_id': "portEdit1"}
    PREFORWARDING_PORT1 = {'title': "HAIKOU", 'control_type': "ListItem"}
    PREFORWARDING_PORT2 = {'title': "Штаде", 'control_type': "ListItem"}
    PREFORWARDING_PORT3 = {'title': "STADE, Germany", 'control_type': "ListItem"}
    PREFORWARDING_PORT4 = {'title': "Harbin", 'control_type': "ListItem"}
    PREFORWARDING_PORT5 = {'title': "Шереметьево (терминал Шереметьево-Карго)", 'control_type': "ListItem"}
    PREFORWARDING_TERMINAL = {'title': "Терминал:", 'control_type': "ComboBox", 'auto_id': "sleTerminalEdit"}
    PREFORWARDING_TERMINAL1 = {'title': "Терминал:", 'control_type': "ComboBox", 'auto_id': "sleTerminal"}
    PREFORWARDING_AGENT = {'title': "Агент:", 'control_type': "ComboBox", 'auto_id': "sleAgentEdit"}
    PREFORWARDING_AGENT1 = {'title': "Агент:", 'control_type': "ComboBox", 'auto_id': "sleAgent"}
    PREFORWARDING_DATA = {'title': "План. дата сборки:", 'control_type': "ComboBox", 'auto_id': "РlanShipments"}
    PREFORWARDING_DATA1 = {'title': "План. дата сборки:", 'control_type': "ComboBox", 'auto_id': "planShipments"}
    SHIPMENT = {'title': "Отгрузка", 'control_type': "ListItem"}
    TRANSSHIPMENT1 = {'title': "Перевалка 1", 'control_type': "ListItem"}
    TRANSSHIPMENT2 = {'title': "Перевалка 2", 'control_type': "ListItem"}
    ARRIVAL = {'title': "Прибытие", 'control_type': "ListItem"}
    SHIPMENT_DATA = {'title': "План. дата отгрузки:", 'control_type': "ComboBox", 'auto_id': "PlanShipments"}
    SHIP = {'title': "Судно:", 'control_type': "ComboBox", 'auto_id': "fShipEdit1"}
    SHIPMENT_DATA_FACT = {'title': "Факт. дата сборки:", 'control_type': "ComboBox", 'auto_id': "factShipments", 'found_index': 0}
    ARRIVAL_DATA = {'title': "План. дата прибытия:", 'control_type': "ComboBox", 'auto_id': "PlanArrivals"}
    ARRIVAL_DATA_FACT = {'title': "Факт. дата прибытия:", 'control_type': "ComboBox", 'auto_id': "factArrivals"}
    UNLOADING = {'title': "Выгрузка:", 'control_type': "ComboBox"}
    ADD_TE = {'control_type': "ComboBox", 'auto_id': "cargosEdit1"}


    # Экспедирование вкладка в заказе
    FORWARDING_TYPE_TEXT = {'auto_id': "lbType", 'control_type': "Text"}
    FORWARDING_ITEM = {'title': "Тип экспедирования строка 1", 'control_type': "DataItem"}

    FORWARDING_NUMBER = {'title': "Номер экспедирования строка 1", 'control_type': "DataItem"}
    FORWARDING_STATUS = {'title': "Статус строка 1", 'control_type': "DataItem"}
    FORWARDING_OTV = {'title': "Ответственный строка 1", 'control_type': "DataItem"}
    FORWARDING_FORWARD = {'title': "Экспедитор строка 1", 'control_type': "DataItem"}
    FORWARDING_TE = {'title': "Количество ТЕ строка 1", 'control_type': "DataItem"}
    FORWARDING_DATA_CREATE = {'title': "Дата создания строка 1", 'control_type': "DataItem"}
    FORWARDING_DATA_FINISH = {'title': "Дата завершения строка 1", 'control_type': "DataItem"}
    FORWARDING_NOTE = {'title': "Примечание строка 1", 'control_type': "DataItem"}

    FORWARDING_TYPE_DIALOG = {'title': "Тип экспедирования:", 'control_type': "ComboBox"}
    FORWARDING_FORWARDER = {'title': "Портовое", 'control_type': "ComboBox", 'found_index': 0}
    FORWARDING_TELEX = {'title': "Телекс-релиз:", 'control_type': "ComboBox"}
    FORWARDING_RECEIVING_DOC = {'title': "Получение докум.:", 'control_type': "ComboBox"}
    FORWARDING_NOMINATION = {'title': "Номинация эксп.:", 'control_type': "ComboBox"}
    FORWARDING_RECEIVING_DO = {'title': "Получение ДО/ДО1:", 'control_type': "ComboBox"}

    DATA_PANEL = {'title': "Панель данных", 'control_type': "Custom"}

    # Груз
    FREIGHT_TYPE_TEXT = {'auto_id': "lcCargoType", 'control_type': "Text"}
    FREIGHT_ITEM = {'title': "ТЕ строка 1", 'control_type': "DataItem"}
    FREIGHT_CREATE_TE = {'title': "ТЕ:", 'control_type': "ComboBox", 'auto_id': "cargoTypeEdit"}
    FREIGHT_CREATE_TE1 = {'title': "Наименование строка 1", 'control_type': "DataItem"}
    FREIGHT_CREATE_TE2 = {'title': "Наименование строка 2", 'control_type': "DataItem"}
    FREIGHT_CREATE_TYPE = {'title': "Тип ТЕ:", 'control_type': "ComboBox", 'auto_id': "cargParameterEdit1"}
    FREIGHT_CREATE_TYPE1 = {'title': "Наименование строка 1", 'control_type': "DataItem"}
    FREIGHT_CREATE_QUANTITY = {'title': "Количество:", 'control_type': "Edit", 'auto_id': "textEditQuantity"}
    FREIGHT_CREATE_UOM = {'title': "Единицы измерения:", 'control_type': "ComboBox", 'auto_id': "unitsOfMeasurementEdit1"}
    FREIGHT_CREATE_UOM1 = {'title': "Наименование строка 1", 'control_type': "DataItem"}
    FREIGHT_CREATE_ORDER = {'title': "Номер ТЕ:", 'control_type': "Edit", 'auto_id': "textEditNumber"}
    FREIGHT_TE_NUMBER = {'title': "Номер ТЕ:", 'control_type': "Edit", 'auto_id': "teCargoName"}
    FREIGHT_TE_TYPE = {'title': "Тип ТЕ:", 'control_type': "ComboBox", 'auto_id': "cargParameterEdit1"}
    FREIGHT_TE_QUANTITY = {'title': "Количество", 'control_type': "Edit", 'auto_id': "teQuantity"}
    FREIGHT_TE_UOM = {'title': "Ед. измерения:", 'control_type': "ComboBox", 'auto_id': "unitsOfMeasurementEdit1"}
    FREIGHT_TYPE_FORM = {'auto_id': "cargoTypeLabelControl", 'control_type': "Text"}
    FREIGHT_TE_NUMBER_FORM = {'title': "Номер ТЕ:", 'control_type': "Edit", 'auto_id': "cargoNameTextEdit"}
    FREIGHT_TE_QUANTITY_FORM = {'title': "Количество", 'control_type': "Edit", 'auto_id': "quantityTextEdit"}


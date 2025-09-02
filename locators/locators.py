class LocOrders:
    # Основные окна
    STARTUP_WINDOW = {'title': 'AIST ver. 4.0.2.306 Default database         автотест', 'control_type': "Window",}
    STARTUP_WINDOW1 = {'title': 'Запуск АИСТ', 'control_type': "Window", 'auto_id': 'frmStartUp', 'found_index': 0}
    MAIN_WINDOW = {'auto_id': 'frmMain'}
    ORDER_FORM = {'auto_id': 'OrderForm'}
    SEA_FORM = {'auto_id': 'SeaCarriageForm', 'control_type': "Window", 'found_index': 0}
    SEA_FORM1 = {'title': "Морская перевозка: Создание", 'auto_id': 'SeaCarriageForm', 'control_type': "Window", 'found_index': 0}
    AUTO_FORM = {'auto_id': 'CarCarriageForm'}
    FORWARDING_FROM = {'auto_id': 'ExpeditionForm'}
    FREIGHT_FROM = {'auto_id': 'CargoForm'}
    PREFORWARDING_FORM = {'auto_id': 'RouteSeaCarriageForm'}
    FORM_FORM = {'auto_id': 'TitleBar', 'control_type': "TitleBar"}
    GTD_FROM = {'auto_id': 'frmGTD', 'control_type': "Window"}
    CHECK_FROM = {'auto_id': 'frmOutboxInvoice', 'control_type': "Window"}
    CHECK_FROM_VS = {'auto_id': 'frmInboxInvoice', 'control_type': "Window"}
    CHECK_FROM_IP = {'auto_id': 'frmOutboxPayment', 'control_type': "Window"}
    CHECK_FROM_VP = {'auto_id': 'frmInboxPayment', 'control_type': "Window"}
    PRODUCT_FORM = {'auto_id': 'ProductForm', 'control_type': "Window"}
    AUTO_SHIPMENT_FORM = {'auto_id': 'RouteCarCarriageForm', 'control_type': "Window"}
    SERVICES_FORM = {'auto_id': 'frmService', 'control_type': "Window"}

    # Базы Аиста
    STAGE_EF = {'title': "(serv02)AIST_STAGE_EF", 'control_type': "ListItem"}
    AIST_EF = {'title': "(serv01)AIST_EF", 'control_type': "ListItem"}

    # Кнопки и элементы управления
    START_BUTTON = {'auto_id': 'btnStart', 'title': 'Запуск', 'control_type': 'Button'}
    ORDERS_TAB = {'title': "Заказы", 'control_type': "ListItem"}
    ADD_BUTTON = {'title': "Добавить", 'control_type': "Button", 'found_index': 0}
    ADD_BUTTON1 = {'title': "Добавить", 'control_type': "Button",  'auto_id': "7013798"}
    CREATE_BUTTON = {'title': "Создать", 'control_type': "Button", 'found_index': 0}
    OPEN_BUTTON = {'title': "Открыть", 'control_type': "Button", 'found_index': 0}
    OPEN_BUTTON1 = {'title': "Открыть", 'control_type': "Button", 'found_index': 1}
    TABLE_DELETE_WINDOW = {'title': "OK", 'auto_id': "btnOK", 'found_index': 0}
    APPLY_BUTTON = {'title': "Применить", 'auto_id': "btnApply"}
    APPLY_BUTTON1 = {'title': "Применить", 'auto_id': "sbApply", 'found_index': 0}

    # Элементы таблицы заказов
    REFRESH_BUTTON = {'title': "Элемент", 'control_type': "SplitButton"}
    TABLE_ORDER_NUMBER_FILTER = {'title': "Номер заказа вернувшийся фильтр строк", 'control_type': "DataItem"}
    TABLE_ORDER_NUMBER = {'title': "Номер заказа вернувшийся строка 1", 'control_type': "DataItem"}
    TABLE_ORDER_NUMBER2 = {'title': "Номер заказа вернувшийся строка 1", 'control_type': "DataItem"}
    TABLE_ORDER_NUMBER3 = {'title': "Заказ № строка 3", 'control_type': "DataItem"}
    TABLE_ORDER_NUMBER8 = {'title': "Номер заказа вернувшийся строка 8", 'control_type': "DataItem"}
    TABLE_ORDER_NUMBER9 = {'title': "Номер заказа вернувшийся строка 9", 'control_type': "DataItem"}
    TABLE_ORDER_NUMBER10 = {'title': "Номер заказа вернувшийся строка 10", 'control_type': "DataItem"}
    TABLE_ORDER_TYPE = {'title': "Тип заказа строка 1", 'control_type': "DataItem"}
    TABLE_STATUS = {'title': "Статус строка 1", 'control_type': "DataItem"}
    TABLE_PRIORITY = {'title': "Приоритет строка 1", 'control_type': "DataItem"}
    TABLE_CREATOR = {'title': "Кем создан строка 1", 'control_type': "DataItem"}
    TABLE_CLIENT = {'title': "Клиент строка 1", 'control_type': "DataItem"}
    TABLE_DELETE = {'title': "Удалить", 'control_type': "Button", 'found_index': 0}

    TABLE_RECIPIENT = {'title': "Получатель строка 1", 'control_type': "DataItem"}
    TABLE_DELIVERY = {'title': "Условия поставки строка 1", 'control_type': "DataItem"}
    TABLE_NOTE = {'title': "Примечание строка 1", 'control_type': "DataItem"}
    TABLE_DATE = {'title': "Дата создания строка 1", 'control_type': "DataItem"}

    # Форма создания заказа
    ORDER_TYPE_COMBO = {'title': "Тип заказа:", 'control_type': "ComboBox", 'auto_id': "orderTypeEdit"}
    LOGISTICS_ITEM = {'title': "Логистика", 'control_type': "ListItem"}
    LOGISTICS_ITEM_DR = {'title': "Другие услуги", 'control_type': "ListItem"}
    CUSTOMER_COMBO = {'title': "Клиент:", 'control_type': "ComboBox", 'auto_id': "customerEdit", 'found_index': 0}
    CUSTOMER_ITEM = {'title': "Наименование строка 1", 'control_type': "DataItem"}
    CUSTOMER_ITEM2 = {'title': "Наименование строка 2", 'control_type': "DataItem"}
    OK_BUTTON = {'title': "ОК", 'control_type': "Button", 'found_index': 0}
    OK_BUTTON1 = {'auto_id': "btnOK", 'found_index': 0}
    SAVE_BUTTON = {'auto_id': "sbSave", 'control_type': "Button"}
    AP = {'auto_id': "sbSave", 'control_type': "Button"}

    # Элементы информации о заказе
    ORDER_NUMBER = { 'control_type': "ComboBox", 'auto_id': "bceNavigation", 'found_index': 0}
    ORDER_TYPE_TEXT = {'auto_id': "lbType", 'control_type': "Text"}
    STATUS_COMBO = {'title': "Статус:", 'control_type': "ComboBox"}
    STATUS_FINISH = {'title': "Завершено", 'control_type': "ListItem"}
    STATUS_COMBO_CANCEL = {'title': "Отменен", 'control_type': "ListItem"}
    STATUS_COMBO_CANCEL2 = {'title': "Отменена", 'control_type': "ListItem"}
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
    RECIPIENT_1 = {'title': "Строка 1", 'control_type': "ListItem", 'found_index': 0}
    RECIPIENT_2 = {'title': "Строка 2", 'control_type': "ListItem", 'found_index': 0}
    RECIPIENT_3 = {'title': "Строка 3", 'control_type': "ListItem", 'found_index': 0}
    RECIPIENT_5 = {'title': "Строка 5", 'control_type': "ListItem", 'found_index': 0}
    RECIPIENT_6 = {'title': "Строка 6", 'control_type': "ListItem", 'found_index': 0}
    RECIPIENT_7 = {'title': "Строка 7", 'control_type': "ListItem", 'found_index': 0}
    RECIPIENT8 = {'title': "Строка 8", 'control_type': "ListItem", 'found_index': 0}
    RECIPIENT9 = {'title': "Строка 9", 'control_type': "ListItem", 'found_index': 0}
    RECIPIENT10 = {'title': "Строка 10", 'control_type': "ListItem", 'found_index': 0}
    DELIVERY_CONDITION = {'title': "Условия поставки:", 'auto_id': "leIncoterms"}
    DELIVERY_CONDITION_0 = {'title': "Строка 0", 'control_type': "Custom"}
    DELIVERY_CONDITION_1 = {'title': "Строка 1", 'control_type': "Custom"}
    DELIVERY_CONDITION_2 = {'title': "Строка 2", 'control_type': "Custom"}
    REFERENCE = {'title': "Референс клиента:", 'auto_id': "teClientReference"}
    NOTE = {'title': "Примечание:", 'auto_id': "meDescription"}
    NOTE1 = {'title': "Примечание:", 'auto_id': "meDecription"}
    NOTE_SEA = {'title': "Примечание:", 'auto_id': "decriptionMemoEdit"}
    NOTE_SERVICES = {'control_type': "Edit", 'auto_id': "descriptionTextEdit"}
    NOTE_CONTAINER = {'auto_id': "descriptionMemoEdit"}

    MOD_DATE = {'control_type': "Text", 'auto_id': "lblModified"}# Дата изменения
    CREATE_DATE = {'control_type': "Text", 'auto_id': "lblCreatedOn"} # Дата создания
    LINE_TRANSPORTATION = {'title': "Строка 1", 'control_type': "ListItem"}
    LINE_TRANSPORTATION10 = {'title': "Строка 10", 'control_type': "ListItem"}
    DEL_BUTTON = {'title': "Удалить", 'control_type': "Button", 'found_index': 0}
    YES_BUTTON = {'title': "Да", 'control_type': "Button"}
    REFRESH_BUTTON_ORDER = {'title': "Обновить", 'control_type': "Button", 'found_index': 0}
    COMPLETION_DATE = {'control_type': "Text", 'auto_id': "lblCompletedOn"}

    # Меню заказа
    OTHER_ACTIONS = {'title': "Другие действия", 'control_type': "MenuItem", 'found_index': 0}

    # Вкладки
    TAB_INFO = {'title': "Информация", 'control_type': "TabItem"}
    TAB_ROUTES = {'title': "Маршрут", 'control_type': "TabItem"}
    TAB_CHECK = {'title': "Счета", 'control_type': "TabItem"}
    TAB_FILE = {'title': "Файлы", 'control_type': "TabItem"}
    TAB_SERVICES = {'title': "Услуги", 'control_type': "TabItem"}
    TAB_FREIGHT = {'title': "Груз", 'control_type': "TabItem", 'found_index': 0}
    TAB_TRANSPORTATION = {'title': "Перевозки", 'control_type': "TabItem", 'found_index': 0}
    TAB_FORWARDING = {'title': "Экспедирование", 'control_type': "TabItem"}
    TAB_GTD = {'title': "Декларирование", 'control_type': "TabItem"}
    TAB_TRACKING = {'title': "Отслеживание", 'control_type': "TabItem"}
    TAB_FORWARDING_FREIGHT = {'title': "Экспедируемый груз", 'control_type': "TabItem"}
    TAB_FREIGHT_GOODS = {'title': "Товары", 'control_type': "TabItem"}

    # Перевозки вкладка в заказе
    TYPE_TRANSPORTATION = {'title': "Тип перевозки:", 'control_type': "ComboBox", 'auto_id': "carriageTypeEdit"}
    SEA_TRANSPORTATION = {'title': "Морская перевозка", 'control_type': "ListItem"}
    SEA_ORDER_NAME = {'title': "Морская перевозка: Новая морская перевозка", 'control_type': "SplitButton"}
    SEA_TYPE_TEXT = {'auto_id': "labelControl1", 'control_type': "Text"}
    AUTO_TRANSPORTATION = {'title': "Автоперевозка", 'control_type': "ListItem", 'found_index': 0}
    AUTO_TRANSPORTATION1 = {'title': "Автоперевозки", 'control_type': "ListItem", 'found_index': 0}


    AUTO_NAME_TRANSPORTATION = {'auto_id': "bceNavigation", 'control_type': "ComboBox"} # номер перевозки
    AUTO_TYPE_TEXT = {'auto_id': "lbType", 'control_type': "Text"} # тип перевозки
    TRANSPORTATION_ITEM = {'title': "Тип перевозки строка 1", 'control_type': "DataItem"}
    TRANSPORTATION_ITEM2 = {'title': "Тип перевозки строка 2", 'control_type': "DataItem"}
    TRANSPORTATION_NUMBER1 = {'title': "Номер перевозки строка 1", 'control_type': "DataItem"}
    TRANSPORTATION_NUMBER2 = {'title': "Номер перевозки строка 2", 'control_type': "DataItem"}
    SEA_TAB = {'title': "Морские перевозки", 'control_type': "ListItem"}
    ORDER_SELECT = {'title': "Заказ:", 'control_type': "ComboBox"}
    SEA_TAB_ORDER_NUMBER = {'title': "Заказ строка 1", 'control_type': "DataItem", 'found_index': 0}
    TYPE_FREIGHT = {'title': "Тип груза:", 'control_type': "ComboBox", 'auto_id': "carriageCargoTypeEdit1"}
    CLASS_FREIGHT = {'title': "Класс груза:", 'control_type': "ComboBox", 'auto_id': "wareClassEdit"}
    CLASS_FREIGHT_AUTO = {'title': "Класс груза: ", 'control_type': "ComboBox", 'auto_id': "wareClassEdit1"}
    CLASS_FREIGHT1 = {'title': "IMO Cargo", 'control_type': "ListItem"}
    CLASS_FREIGHT2 = {'title': "VER Cargo", 'control_type': "ListItem"}
    DOWNLOAD_METHOD = {'title': "Способ загрузки:", 'control_type': "ComboBox"}
    DOWNLOAD_METHOD_AUTO = {'title': "Способ загрузки: ", 'control_type': "ComboBox", 'auto_id': "carriageMethodLoadingEdit1"}
    DOWNLOAD_METHOD1 = {'title': "FCL", 'control_type': "ListItem"}
    DOWNLOAD_METHOD3 = {'title': "Break Bulk", 'control_type': "ListItem"}
    REFERENCE_FREIGHT = {'control_type': "Edit", 'auto_id': "teCargoReference"}
    BOOKING_REFERENCE = {'title': "Букинг референс:", 'control_type': "Edit"}
    OCEAN_LINE = {'title': "Океанская линия:", 'control_type': "ComboBox"}
    OCEAN_KONOS = {'control_type': "Edit", 'auto_id': "oceanBillOfLadingTextBox"}
    FEEDER_LINE = {'title': "Фидерная линия:", 'control_type': "ComboBox"}
    FEEDER_LINE1 = {'title': "Строка 2", 'control_type': "ListItem"}
    FEEDER_LINE3 = {'title': "Строка 3", 'control_type': "ListItem"}
    FEEDER_LINE4 = {'title': "Строка 4", 'control_type': "ListItem"}
    FEEDER_LINE5 = {'title': "Строка 5", 'control_type': "ListItem"}
    FEEDER_KONOS = {'title': "Фидерн. коносамент:", 'control_type': "Edit"}


    ROUTES_WINDOWS = {'title': "Тип задания:", 'control_type': "ComboBox", 'auto_id': "routeAssignmentSeaCarriageEdit1"}
    PREFORWARDING = {'title': "Преэкспедирование", 'control_type': "ListItem"}
    PREFORWARDING_PORT = {'title': "Порт:", 'control_type': "ComboBox", 'auto_id': "portEdit1"}
    PREFORWARDING_PORT1 = {'title': "HAIKOU", 'control_type': "ListItem"}
    PREFORWARDING_PORT2 = {'title': "Штаде", 'control_type': "ListItem"}
    PREFORWARDING_PORT3 = {'title': "STADE, Germany", 'control_type': "ListItem"}
    PREFORWARDING_PORT4 = {'title': "Harbin", 'control_type': "ListItem"}
    PREFORWARDING_PORT5 = {'title': "Шереметьево (терминал Шереметьево-Карго)", 'control_type': "ListItem"}
    PREFORWARDING_TERMINAL = {'title': "Терминал:", 'control_type': "ComboBox", 'auto_id': "sleTerminalEdit"}
    PREFORWARDING_TERMINAL1 = {'control_type': "ComboBox", 'auto_id': "sleTerminal", 'found_index': 0}
    PREFORWARDING_AGENT = {'title': "Агент:", 'control_type': "ComboBox", 'auto_id': "sleAgentEdit"}
    PREFORWARDING_AGENT1 = {'title': "Агент:", 'control_type': "ComboBox", 'auto_id': "sleAgent"}
    PREFORWARDING_DATA = {'title': "План. дата сборки:", 'control_type': "ComboBox", 'auto_id': "РlanShipments"}
    PREFORWARDING_DATA1 = {'title': "План. дата отгрузки:", 'control_type': "ComboBox", 'auto_id': "planShipments"}
    PREFORWARDING_FACT_DATA = {'title': "Факт. дата отгрузки:", 'control_type': "ComboBox", 'auto_id': "factShipments"}
    SHIPMENT = {'title': "Отгрузка", 'control_type': "ListItem"}
    TRANSSHIPMENT1 = {'title': "Перевалка 1", 'control_type': "ListItem"}
    TRANSSHIPMENT2 = {'title': "Перевалка 2", 'control_type': "ListItem"}
    ARRIVAL = {'title': "Прибытие", 'control_type': "ListItem"}
    SHIPMENT_DATA = {'title': "План. дата отгрузки:", 'control_type': "ComboBox", 'auto_id': "PlanShipments"}
    SHIPMENT_DATA1 = {'title': "План. дата отгрузки:", 'control_type': "ComboBox", 'auto_id': "planShipments"}
    SHIP = {'title': "Судно:", 'control_type': "ComboBox", 'auto_id': "fShipEdit1"}
    SHIPMENT_DATA_FACT = {'title': "Факт. дата сборки:", 'control_type': "ComboBox", 'auto_id': "factShipments", 'found_index': 0}

    ARRIVAL_DATA = {'title': "План. дата прибытия:", 'control_type': "ComboBox", 'auto_id': "PlanArrivals"}
    ARRIVAL_DATA1 = {'control_type': "ComboBox", 'auto_id': "planArrivals"} # Плановая
    ARRIVAL_DATA_FACT = {'control_type': "ComboBox", 'auto_id': "factArrivals"}# фактическая
    UNLOADING = {'title': "Выгрузка:", 'control_type': "ComboBox", 'found_index': 0}
    ADD_TE = {'control_type': "ComboBox", 'auto_id': "cargosEdit1"}


    # Автоперевозка
    AUTO_CARRIER = {'title': "Перевозчик:", 'control_type': "ComboBox", 'auto_id': "sleClient"}
    AUTO_CMR = {'title': "Номер CMR:", 'control_type': "Edit", 'auto_id': "teCMR"}
    AUTO_CMR_POR = {'title': "Номер CMR порожн.:", 'control_type': "Edit", 'auto_id': "teCMRporozhn"}
    CONTAINER_DELIVERY = {'title': "Сдача контейнера", 'control_type': "ListItem"}
    TERMINAL_CHANGE = {'title': "Терминал сдачи:", 'control_type': "ComboBox"}

    # Морская перевозка таблица в заказе
    PORT1 = {'title': "Порт строка 1", 'control_type': "DataItem"}
    PORT2 = {'title': "Порт строка 2", 'control_type': "DataItem"}
    PORT3 = {'title': "Порт строка 3", 'control_type': "DataItem"}
    PORT4 = {'title': "Порт строка 4", 'control_type': "DataItem"}
    PORT5 = {'title': "Порт строка 5", 'control_type': "DataItem"}

    NAME_LINE1 = {'title': "Имя строка 1", 'control_type': "DataItem"}
    NAME_LINE2 = {'title': "Имя строка 2", 'control_type': "DataItem"}
    NAME_LINE3 = {'title': "Имя строка 3", 'control_type': "DataItem"}
    NAME_LINE4 = {'title': "Имя строка 4", 'control_type': "DataItem"}
    NAME_LINE5 = {'title': "Имя строка 5", 'control_type': "DataItem"}

    TERMINAL_LINE1 = {'title': "Терминал строка 1", 'control_type': "DataItem"}
    TERMINAL_LINE2 = {'title': "Терминал строка 2", 'control_type': "DataItem"}
    TERMINAL_LINE3 = {'title': "Терминал строка 3", 'control_type': "DataItem"}
    TERMINAL_LINE4 = {'title': "Терминал строка 4", 'control_type': "DataItem"}
    TERMINAL_LINE5 = {'title': "Терминал строка 5", 'control_type': "DataItem"}

    AGENT_LINE1 = {'title': "Агент строка 1", 'control_type': "DataItem"}
    AGENT_LINE2 = {'title': "Агент строка 2", 'control_type': "DataItem"}
    AGENT_LINE3 = {'title': "Агент строка 3", 'control_type': "DataItem"}
    AGENT_LINE4 = {'title': "Агент строка 4", 'control_type': "DataItem"}
    AGENT_LINE5 = {'title': "Агент строка 5", 'control_type': "DataItem"}

    SHIP_LINE1 = {'title': "Судно строка 1", 'control_type': "DataItem"}
    SHIP_LINE2 = {'title': "Судно строка 2", 'control_type': "DataItem"}
    SHIP_LINE3 = {'title': "Судно строка 3", 'control_type': "DataItem"}
    SHIP_LINE4 = {'title': "Судно строка 4", 'control_type': "DataItem"}

    PLAN_LOAD1 = {'title': "План. отгрузки строка 1", 'control_type': "DataItem"}
    PLAN_LOAD2 = {'title': "План. отгрузки строка 2", 'control_type': "DataItem"}
    PLAN_LOAD3 = {'title': "План. отгрузки строка 3", 'control_type': "DataItem"}
    PLAN_LOAD4 = {'title': "План. отгрузки строка 4", 'control_type': "DataItem"}

    FACT_LOAD1 = {'title': "Факт. отгрузки строка 1", 'control_type': "DataItem"}
    FACT_LOAD2 = {'title': "Факт. отгрузки строка 2", 'control_type': "DataItem"}
    FACT_LOAD3 = {'title': "Факт. отгрузки строка 3", 'control_type': "DataItem"}
    FACT_LOAD4 = {'title': "Факт. отгрузки строка 4", 'control_type': "DataItem"}

    PLAN_ARRIVAL1 = {'title': "План. прибытия строка 1", 'control_type': "DataItem"}
    PLAN_ARRIVAL2 = {'title': "План. прибытия строка 2", 'control_type': "DataItem"}
    PLAN_ARRIVAL3 = {'title': "План. прибытия строка 3", 'control_type': "DataItem"}
    PLAN_ARRIVAL4 = {'title': "План. прибытия строка 4", 'control_type': "DataItem"}
    PLAN_ARRIVAL5 = {'title': "План. прибытия строка 5", 'control_type': "DataItem"}

    FACT_ARRIVAL1 = {'title': "Факт. прибытия строка 1", 'control_type': "DataItem"}
    FACT_ARRIVAL2 = {'title': "Факт. прибытия строка 2", 'control_type': "DataItem"}
    FACT_ARRIVAL3 = {'title': "Факт. прибытия строка 3", 'control_type': "DataItem"}
    FACT_ARRIVAL4 = {'title': "Факт. прибытия строка 4", 'control_type': "DataItem"}
    FACT_ARRIVAL5 = {'title': "Факт. прибытия строка 5", 'control_type': "DataItem"}

    # Автоперевозка в заказе
    ADDRESS1 = {'title': "Адрес строка 1", 'control_type': "DataItem"}
    ADDRESS2 = {'title': "Адрес строка 2", 'control_type': "DataItem"}
    DRIVER = {'title': "Водитель строка 1", 'control_type': "DataItem"}
    AUTO = {'title': "Автомобиль строка 1", 'control_type': "DataItem"}
    AUTO_FORM1 = {'title': "Автомобиль:", 'control_type': "ComboBox", 'auto_id': "lueCar"}

    # Автоперевозка таблица
    AUTO_TABLE = {'title': "Сдача контейнера", 'control_type': "ListItem"}
    AUTO_ADDRESS = {'title': "Адрес:", 'control_type': "ComboBox", 'auto_id': "sleTerminal"}
    AUTO_DRIVER = {'title': "Водитель:", 'control_type': "ComboBox", 'auto_id': "driversEdit1"}

    STATUS_TABLE1 = {"title": "Статус строка 1", "control_type": "DataItem", 'found_index': 0}
    PRIORITY_TABLE1 = {"title": "Приоритет строка 1", "control_type": "DataItem", 'found_index': 0}
    RESPONSIBLE_TABLE1 = {"title": "Ответственный строка 1", "control_type": "DataItem", 'found_index': 0}
    CARRIER_TABLE1 = {"title": "Перевозчик строка 1", "control_type": "DataItem"}
    CARGO_CLASS_TABLE1 = {"title": "Класс груза строка 1", "control_type": "DataItem"}
    LOADING_METHOD_TABLE1 = {"title": "Способ загрузки строка 1", "control_type": "DataItem"}
    CMR_NUMBER_TABLE1 = {"title": "Номер CMR строка 1", "control_type": "DataItem"}
    CREATED_BY_TABLE1 = {"title": "Кем создан строка 1", "control_type": "DataItem", 'found_index': 0}
    CREATION_DATE_TABLE1 = {"title": "Дата создания строка 1", "control_type": "DataItem"}
    MODIFICATION_DATE_TABLE1 = {"title": "Дата изменения строка 1", "control_type": "DataItem"}
    COMPLETION_DATE_TABLE1 = {"title": "Дата завершения строка 1", "control_type": "DataItem"}
    CARGO_TYPE_TABLE1 = {"title": "Тип груза строка 1", "control_type": "DataItem"}

    SHIPMENT1 = {"title": "Маршрутное задание строка 1", "control_type": "DataItem"}
    SHIPMENT2 = {"title": "Маршрутное задание строка 2", "control_type": "DataItem"}
    SHIPMENT3 = {"title": "Маршрутное задание строка 3", "control_type": "DataItem"}

    PLAN_ARRIVAL_DATA1 = {"title": "План. прибытия строка 1", "control_type": "DataItem"}
    PLAN_ARRIVAL_DATA2 = {"title": "План. прибытия строка 2", "control_type": "DataItem"}
    PLAN_ARRIVAL_DATA3 = {"title": "План. прибытия строка 3", "control_type": "DataItem"}

    FACT_ARRIVAL_DATA1 = {"title": "План. прибытия строка 1", "control_type": "DataItem"}
    FACT_ARRIVAL_DATA2 = {"title": "План. прибытия строка 2", "control_type": "DataItem"}
    FACT_ARRIVAL_DATA3 = {"title": "План. прибытия строка 3", "control_type": "DataItem"}


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

    # Экспедируемый груз
    FORWARDING_FID_KONS1 = {'title': "Фид. коносамент строка 1", 'control_type': "DataItem"}
    FORWARDING_PLAN_ARRIVAL1 = {'title': "План. приб. строка 1", 'control_type': "DataItem"}
    FORWARDING_FACT_ARRIVAL1 = {'title': "Факт. приб. строка 1", 'control_type': "DataItem"}
    FORWARDING_FID_LINE1 = {'title': "Фид. Линия строка 1", 'control_type': "DataItem"}
    FORWARDING_PORT1 = {'title': "Порт строка 1", 'control_type': "DataItem"}
    FORWARDING_TERMINAL1 = {'title': "Терминал строка 1", 'control_type': "DataItem"}
    FORWARDING_TE1 = {'title': "ТЕ строка 1", 'control_type': "DataItem"}
    FORWARDING_TE_TYPE1 = {'title': "Тип ТЕ строка 1", 'control_type': "DataItem"}
    FORWARDING_TE_NUMBER1 = {'title': "Номер ТЕ строка 1", 'control_type': "DataItem"}
    FORWARDING_RELEASE1 = {'title': "Релиз строка 1", 'control_type': "DataItem"}
    FORWARDING_DOC1 = {'title': "Документы строка 1", 'control_type': "DataItem"}
    FORWARDING_NOMINATION1 = {'title': "Номинация строка 1", 'control_type': "DataItem"}
    FORWARDING_DO_DO1 = {'title': "ДО/ДО1 строка 1", 'control_type': "DataItem"}
    FORWARDING_NOTE1 = {'title': "Примечание строка 1", 'control_type': "DataItem"}

    # Груз
    FREIGHT_TYPE_TEXT = {'auto_id': "lcCargoType", 'control_type': "Text"}
    FREIGHT_ITEM = {'title': "ТЕ строка 1", 'control_type': "DataItem"}
    FREIGHT_ITEM2 = {'title': "ТЕ строка 2", 'control_type': "DataItem"}
    FREIGHT_TABLE_TYPE_TE = {'title': "Тип ТЕ строка 1", 'control_type': "DataItem"}
    FREIGHT_TABLE_NUMBER_TE = {'title': "Тип ТЕ строка 1", 'control_type': "DataItem"}
    FREIGHT_CREATE_TE = {'title': "ТЕ:", 'control_type': "ComboBox", 'auto_id': "cargoTypeEdit"}
    FREIGHT_CREATE_TE1 = {'title': "Наименование строка 1", 'control_type': "DataItem"}
    FREIGHT_CREATE_TE2 = {'title': "Наименование строка 2", 'control_type': "DataItem"}
    FREIGHT_CREATE_TE3 = {'title': "Наименование строка 3", 'control_type': "DataItem"}
    FREIGHT_CREATE_TE4 = {'title': "Наименование строка 4", 'control_type': "DataItem"}
    FREIGHT_CREATE_TE5 = {'title': "Наименование строка 5", 'control_type': "DataItem"}
    FREIGHT_CREATE_TYPE = {'title': "Тип ТЕ:", 'control_type': "ComboBox", 'auto_id': "cargParameterEdit1"}
    FREIGHT_CREATE_TYPE1 = {'title': "Наименование строка 1", 'control_type': "DataItem"}
    FREIGHT_CREATE_QUANTITY = {'title': "Количество:", 'control_type': "Edit", 'auto_id': "textEditQuantity"}
    FREIGHT_QUANTITY_APPLY = {'control_type': "Edit", 'auto_id': "teQuantity"}
    FREIGHT_CREATE_UOM = {'title': "Единицы измерения:", 'control_type': "ComboBox", 'auto_id': "unitsOfMeasurementEdit1"}
    FREIGHT_CREATE_UOM_SAVE = {'title': "Ед. измерения:", 'control_type': "ComboBox", 'auto_id': "unitsOfMeasurementEdit1"}
    FREIGHT_CREATE_UOM1 = {'title': "Наименование строка 1", 'control_type': "DataItem"}
    FREIGHT_CREATE_ORDER = {'title': "Номер ТЕ:", 'control_type': "Edit", 'auto_id': "textEditNumber"}
    FREIGHT_TE_NUMBER = {'title': "Номер ТЕ:", 'control_type': "Edit", 'auto_id': "teCargoName"}
    FREIGHT_TE_TYPE = {'title': "Тип ТЕ:", 'control_type': "ComboBox", 'auto_id': "cargParameterEdit1"}
    FREIGHT_TE_QUANTITY = {'title': "Количество", 'control_type': "Edit", 'auto_id': "teQuantity"}
    FREIGHT_TE_UOM = {'title': "Ед. измерения:", 'control_type': "ComboBox", 'auto_id': "unitsOfMeasurementEdit1"}
    FREIGHT_TYPE_FORM = {'auto_id': "lcCargoType", 'control_type': "Text"}
    FREIGHT_TE_NUMBER_FORM = {'title': "Номер ТЕ:", 'control_type': "Edit", 'auto_id': "teCargoName"}
    FREIGHT_TE_QUANTITY_FORM = {'title': "Количество", 'control_type': "Edit", 'auto_id': "teQuantity"}
    FREIGHT_NET_WEIGHT_FORM = {'title': "-", 'control_type': "Text", 'auto_id': "netWeightLableControl"}
    FREIGHT_GROSS_WEIGHT_FORM = {'title': "-", 'control_type': "Text", 'auto_id': "grossWeightLableControl"}
    FREIGHT_NUMBER_SEAL_FORM = {'title': "Номер пломбы:", 'control_type': "Edit", 'auto_id': "cargoSealTextEdit"}
    FREIGHT_NUMBER_GTD_FORM = {'title': "Bulkership", 'control_type': "Edit", 'auto_id': "cargoGTDNumberTextEdit"}
    FREIGHT_MODE_TO_FORM = {'title': "Режим ТО:", 'control_type': "ComboBox", 'auto_id': "lueInspectionType"}
    FREIGHT_DATA_TO_FORM = {'control_type': "ComboBox", 'auto_id': "deReviewDate"}
    FREIGHT_CREATE_FORM = {'control_type': "Text", 'auto_id': "lcCreatedOn"}
    FREIGHT_MOD_FORM = {'control_type': "Text", 'auto_id': "lcModified"}
    FREIGHT_TOTAL_RECORDS = {'title': "Статический", 'control_type': "Text", 'found_index': 0}
    FREIGHT_LINE_3 = {'title': "Строка 3", 'control_type': "ListItem"}
    FREIGHT_LINE_7 = {'title': "Строка 7", 'control_type': "ListItem"}
    FREIGHT = {'title': "Грузы", 'control_type': "ListItem"}
    FREIGHT_ORDER_TABLE = {'title': "Заказ фильтр строк", 'control_type': "DataItem"}
    FREIGHT_ORDER_W = {'title': "Заказ:", 'control_type': "ComboBox", 'auto_id': "orderEdit", 'found_index': 0}
    FREIGHT_ORDER_CREATE = {'title': "Создать", 'control_type': "Button", 'auto_id': "CreateOrderButton"}

    # Таблица Грузы
    FREIGHT_RESP_FOR_TABLE = {'title': "Ответственный (Экспедирование) фильтр строк", 'control_type': "DataItem"}

    OTV_FOR_TABLE1 = {'title': "Ответственный (Экспедирование) строка 1", 'control_type': "DataItem"}
    OTV_FOR_TABLE2 = {'title': "Ответственный (Экспедирование) строка 2", 'control_type': "DataItem"}
    STATUS_AUTO_TABLE1 = {'title': "Статус (Автоперевозка) строка 1", 'control_type': "DataItem"}
    STATUS_AUTO_TABLE2 = {'title': "Статус (Автоперевозка) строка 2", 'control_type': "DataItem"}
    RECIPIENT_TABLE1 = {'title': "Получатель строка 1", 'control_type': "DataItem"}
    RECIPIENT_TABLE2 = {'title': "Получатель строка 2", 'control_type': "DataItem"}
    CLIENT_FOR_TABLE1 = {'title': "Клиент строка 1", 'control_type': "DataItem"}
    CLIENT_FOR_TABLE2 = {'title': "Клиент строка 2", 'control_type': "DataItem"}
    NUM_TE_TABLE1 = {'title': "Номер ТЕ строка 1", 'control_type': "DataItem"}
    NUM_TE_TABLE2 = {'title': "Номер ТЕ строка 2", 'control_type': "DataItem"}
    TE_TABLE1 = {'title': "ТЕ строка 1", 'control_type': "DataItem"}
    TE_TABLE2 = {'title': "ТЕ строка 2", 'control_type': "DataItem"}
    TYPE_TE_TABLE1 = {'title': "Тип ТЕ строка 1", 'control_type': "DataItem"}
    TYPE_TE_TABLE2 = {'title': "Тип ТЕ строка 2", 'control_type': "DataItem"}
    FREIGHT_GROSS_TABLE1 = {'title': "Вес брутто, кг строка 1", 'control_type': "DataItem"}
    FREIGHT_GROSS_TABLE2 = {'title': "Вес брутто, кг строка 2", 'control_type': "DataItem"}
    SEAL_NUMBER_TABLE1 = {'title': "Номер пломбы строка 1", 'control_type': "DataItem"}
    SEAL_NUMBER_TABLE2 = {'title': "Номер пломбы строка 2", 'control_type': "DataItem"}
    TERMINAL_TABLE1 = {'title': "Терминал строка 1", 'control_type': "DataItem"}
    TERMINAL_TABLE2 = {'title': "Терминал строка 2", 'control_type': "DataItem"}
    PORT_TABLE1 = {'title': "Порт строка 1", 'control_type': "DataItem"}
    PORT_TABLE2 = {'title': "Порт строка 2", 'control_type': "DataItem"}
    PLAN_ARRIVAL_TABLE1 = {'title': "План. дата прибытия в порт строка 1", 'control_type': "DataItem"}
    PLAN_ARRIVAL_TABLE2 = {'title': "План. дата прибытия в порт строка 2", 'control_type': "DataItem"}
    FACT_ARRIVAL_TABLE1 = {'title': "Факт. дата прибытия в порт строка 1", 'control_type': "DataItem"}
    FACT_ARRIVAL_TABLE2 = {'title': "Факт. дата прибытия в порт строка 2", 'control_type': "DataItem"}
    FACT_UNLOADING_TABLE1 = {'title': "Факт. дата выгрузки строка 1", 'control_type': "DataItem"}
    FACT_UNLOADING_TABLE2 = {'title': "Факт. дата выгрузки строка 2", 'control_type': "DataItem"}
    DO_TABLE1 = {'title': "ДО/ДО1 строка 1", 'control_type': "DataItem"}
    DO_TABLE2 = {'title': "ДО/ДО1 строка 2", 'control_type': "DataItem"}
    DOC_TABLE1 = {'title': "Получение документов строка 1", 'control_type': "DataItem"}
    DOC_TABLE2 = {'title': "Получение документов строка 2", 'control_type': "DataItem"}
    NOMINATION_TABLE1 = {'title': "Номинация строка 1", 'control_type': "DataItem"}
    NOMINATION_TABLE2 = {'title': "Номинация строка 2", 'control_type': "DataItem"}
    REGIMEN_TABLE1 = {'title': "Режим ТО строка 1", 'control_type': "DataItem"}
    REGIMEN_TABLE2 = {'title': "Режим ТО строка 2", 'control_type': "DataItem"}
    TELEX_TABLE1 = {'title': "Телекс-релиз строка 1", 'control_type': "DataItem"}
    TELEX_TABLE2 = {'title': "Телекс-релиз строка 2", 'control_type': "DataItem"}
    DATA_TO_TABLE1 = {'title': "Дата ТО строка 1", 'control_type': "DataItem"}
    DATA_TO_TABLE2 = {'title': "Дата ТО строка 2", 'control_type': "DataItem"}
    FEEDER_SHIP_TABLE1 = {'title': "Фидерное судно строка 1", 'control_type': "DataItem"}
    FEEDER_SHIP_TABLE2 = {'title': "Фидерное судно строка 2", 'control_type': "DataItem"}
    FEEDER_LINE_TABLE1 = {'title': "Фидерная линия строка 1", 'control_type': "DataItem"}
    FEEDER_LINE_TABLE2 = {'title': "Фидерная линия строка 2", 'control_type': "DataItem"}
    FEEDER_PORT_TABLE1 = {'title': "Фидерное судно строка 1", 'control_type': "DataItem"}
    FEEDER_PORT_TABLE2 = {'title': "Фидерное судно строка 2", 'control_type': "DataItem"}
    NOMINATION_TABLE = {'title': "Номинация", 'control_type': "DataItem"}
    OCEAN_LINE_TABLE1 = {'title': "Океанская линия строка 1", 'control_type': "DataItem"}
    OCEAN_LINE_TABLE2 = {'title': "Океанская линия строка 2", 'control_type': "DataItem"}
    OCEAN_SHIP_TABLE1 = {'title': "Океанское судно строка 1", 'control_type': "DataItem"}
    OCEAN_SHIP_TABLE2 = {'title': "Океанское судно строка 2", 'control_type': "DataItem"}
    OCEAN_KONOS_TABLE1 = {'title': "Океанский коносамент строка 1", 'control_type': "DataItem"}
    OCEAN_KONOS_TABLE2 = {'title': "Океанский коносамент строка 2", 'control_type': "DataItem"}
    FEEDER_KONOS_TABLE1 = {'title': "Фидерный коносамент строка 1", 'control_type': "DataItem"}
    FEEDER_KONOS_TABLE2 = {'title': "Фидерный коносамент строка 2", 'control_type': "DataItem"}
    TRANSPORT_TABLE1 = {'title': "Перевозка строка 1", 'control_type': "DataItem"}
    TRANSPORT_TABLE2 = {'title': "Перевозка строка 2", 'control_type': "DataItem"}
    ORDER_TABLE1 = {'title': "Заказ строка 1", 'control_type': "DataItem"}
    ORDER_TABLE2 = {'title': "Заказ строка 2", 'control_type': "DataItem"}
    RESPONSIBLE_ORDER_TABLE1 = {'title': "Ответственный (Заказ) строка 1", 'control_type': "DataItem"}
    RESPONSIBLE_ORDER_TABLE2 = {'title': "Ответственный (Заказ) строка 2", 'control_type': "DataItem"}
    EXPEDITION_TABLE1 = {'title': "Экспедирование строка 1", 'control_type': "DataItem"}
    EXPEDITION_TABLE2 = {'title': "Экспедирование строка 2", 'control_type': "DataItem"}
    CAR_TABLE1 = {'title': "Автомобиль строка 1", 'control_type': "DataItem"}
    CAR_TABLE2 = {'title': "Автомобиль строка 2", 'control_type': "DataItem"}
    CAR_TABLE3 = {'title': "Автомобиль строка 2", 'control_type': "DataItem"}
    ADDRESS_TABLE1 = {'title': "Адрес строка 1", 'control_type': "DataItem"}
    ADDRESS_TABLE2 = {'title': "Адрес строка 2", 'control_type': "DataItem"}
    ADDRESS_TABLE3 = {'title': "Адрес строка 3", 'control_type': "DataItem"}

    WEIGHT_NETTO_TABLE1 = {'title': "Вес нетто, кг строка 1", 'control_type': "DataItem"}
    WEIGHT_NETTO_TABLE2 = {'title': "Вес нетто, кг строка 2", 'control_type': "DataItem"}
    DRIVER_TABLE1 = {'title': "Водитель строка 1", 'control_type': "DataItem"}
    DRIVER_TABLE2 = {'title': "Водитель строка 2", 'control_type': "DataItem"}
    DRIVER_TABLE3 = {'title': "Водитель строка 3", 'control_type': "DataItem"}
    DATE_CHANGED_TABLE1 = {'title': "Дата изменения строка 1", 'control_type': "DataItem"}
    DATE_CHANGED_TABLE2 = {'title': "Дата изменения строка 2", 'control_type': "DataItem"}
    DATE_CREATED_TABLE1 = {'title': "Дата создания строка 1", 'control_type': "DataItem"}
    DATE_CREATED_TABLE2 = {'title': "Дата создания строка 2", 'control_type': "DataItem"}
    MEASUREMENT_UNIT_TABLE1 = {'title': "Ед. измерения строка 1", 'control_type': "DataItem"}
    MEASUREMENT_UNIT_TABLE2 = {'title': "Ед. измерения строка 2", 'control_type': "DataItem"}
    CHANGED_BY_TABLE1 = {'title': "Кем изменен строка 1", 'control_type': "DataItem"}
    CHANGED_BY_TABLE2 = {'title': "Кем изменен строка 2", 'control_type': "DataItem"}
    CREATED_TE_TABLE1 = {'title': "Кем создан (ТЕ) строка 1", 'control_type': "DataItem"}
    CREATED_TE_TABLE2 = {'title': "Кем создан (ТЕ) строка 2", 'control_type': "DataItem"}
    QUANTITY_TABLE1 = {'title': "Количество строка 1", 'control_type': "DataItem"}
    QUANTITY_TABLE2 = {'title': "Количество строка 2", 'control_type': "DataItem"}
    VERSION_TABLE1 = {'title': "Новая версия строка 1", 'control_type': "DataItem"}
    VERSION_TABLE2 = {'title': "Новая версия строка 2", 'control_type': "DataItem"}
    GTD_NUMBER_TABLE1 = {'title': "Номер ГТД строка 1", 'control_type': "DataItem"}
    GTD_NUMBER_TABLE2 = {'title': "Номер ГТД строка 2", 'control_type': "DataItem"}
    OTV_AUTO_TABLE1 = {'title': "Ответственный (Автоперевозка) строка 1", 'control_type': "DataItem"}
    OTV_AUTO_TABLE2 = {'title': "Ответственный (Автоперевозка) строка 2", 'control_type': "DataItem"}
    DELIVERY_DATE_PLAN_TABLE1 = {'title': "План. дата доставки строка 1", 'control_type': "DataItem"}
    DELIVERY_DATE_PLAN_TABLE2 = {'title': "План. дата доставки строка 2", 'control_type': "DataItem"}
    NOTE_TE_TABLE1 = {'title': "Примечание (ТЕ) строка 1", 'control_type': "DataItem"}
    NOTE_TE_TABLE2 = {'title': "Примечание (ТЕ) строка 2", 'control_type': "DataItem"}


    # Форма контейнера
    # FREIGHT_NUMBER_SEAL_FORM_CONTAINER =
    FREIGHT_NUMBER_GTD_FORM_CONTAINER = {'title': "Container", 'control_type': "Edit", 'auto_id': "cargoGTDNumberTextEdit"}

    # ГТД
    GTD_CLIENT = {'title': "Клиент:", 'control_type': "ComboBox", 'auto_id': "leClientId"}
    GTD_ORDER = {'control_type': "ComboBox", 'auto_id': "orderEdit1", 'found_index': 0}
    GTD_PROCEDURE = {'title': "Процедура:", 'control_type': "ComboBox", 'auto_id': "icGTDType"}
    GTD_TE_NOT = {'title': "Коносаментная партия должна содержать хотя бы один контейнер", 'control_type': "Text"}
    GTD_TE = {'title': "Номер ТЕ строка 1", 'control_type': "DataItem"}
    GTD_TE_LINE  = {'title': "Контейнеры строка 1", 'control_type': "DataItem"}

    # Счета радио кнопки
    IS_CREATE_ORDER = {'title': "Исходящий счет", 'control_type': "RadioButton"}
    VS_CREATE_ORDER = {'title': "Входящий счет", 'control_type': "RadioButton"}
    IP_CREATE_ORDER = {'title': "Исходящий платеж", 'control_type': "RadioButton"}
    VP_CREATE_ORDER = {'title': "Входящий платеж", 'control_type': "RadioButton"}
    BS_CREATE_ORDER = {'title': "Букинг-счет", 'control_type': "RadioButton"}

    # Исходящий счет
    #IS_NAME_FORM = {'control_type': "TitleBar", 'auto_id': "TitleBar", 'found_index': 1} не находит
    IS_ORDER = {'control_type': "ComboBox", 'auto_id': "orderEdit1", 'found_index': 0}
    IS_DATE = {'title': "Дата:", 'control_type': "ComboBox", 'auto_id': "deInvoiceDate"}
    IS_LIST = {'control_type': "ComboBox", 'auto_id': "icOutboxInvoiceType"}
    IS_FREIGHT = {'title': "Товарный", 'control_type': "ListItem"}
    IS_FREIGHT1 = {'title': "Фрахтовый", 'control_type': "ListItem"}
    IS_FREIGHT2 = {'title': "Экспедиторский", 'control_type': "ListItem"}
    IS_FREIGHT3 = {'title': "Таможенный", 'control_type': "ListItem"}
    IS_SUPPLIER = {'title': "Поставщик:", 'control_type': "ComboBox", 'auto_id': "leSellerId"}
    IS_BUYER = {'title': "Покупатель:", 'control_type': "ComboBox", 'auto_id': "leBuyerId"}
    IS_TYPE_CHECK = {'title': "Тип счета строка 1", 'control_type': "DataItem"}
    IS_NUMBER = {'title': "Счет №:", 'control_type': "Edit", 'auto_id': "nameTextEdit"}
    IS_NUMBER_TABLE = {'title': "Счет № строка 1", 'control_type': "DataItem"}
    IS_DATE_TABLE = {'title': "Дата строка 1", 'control_type': "DataItem"}
    IS_SUPPLIER_TABLE = {'title': "Поставщик строка 1", 'control_type': "DataItem"}
    IS_BUYER_TABLE = {'title': "Покупатель строка 1", 'control_type': "DataItem"}
    IS_CURRENCY = {'title': "Валюта строка 1", 'control_type': "DataItem"}
    IS_SUM_TABLE = {'title': "Сумма строка 1", 'control_type': "DataItem"}
    IS_CLOSED_TABLE = {'title': "Закрыто строка 1", 'control_type': "DataItem"}
    IS_NCLOSED_TABLE = {'title': "Незакрыто строка 1", 'control_type': "DataItem"}
    IS_NINCLUDED_TABLE = {'title': "Неразнесено строка 1", 'control_type': "DataItem"}
    IS_APPOINTMENT_TABLE = {'title': "Назначение строка 1", 'control_type': "DataItem"}

    # Входящий счет
    VS_CONTRACTOR = {'title': "Подрядчик:", 'control_type': "ComboBox", 'auto_id': "leContractorId"}
    VS_ORDER = {'title': "Заказ:", 'control_type': "ComboBox", 'auto_id': "orderEdit1"}

    # Входящий платеж
    VP_NUMBER = {'title': "Счет:", 'control_type': "Edit", 'auto_id': "nameTextEdit"}
    VP_ORDER = {'title': "Заказ: ", 'control_type': "ComboBox", 'auto_id': "orderEdit1"}

    # Удаление
    DEL_WINDOW = {'control_type': "Text", 'auto_id': "lblDescription"}
    DEL_WINDOW_BUTTON = {'title': "Закрыть", 'control_type': "Button", 'found_index': 0}

    # Файлы
    FILE_SELECT = {'control_type': "Выбрать файлы", 'auto_id': "btnAdd"}

    # Товары
    NAME_TOV_RU = {'title': "Наименование (ru):", 'control_type': "Edit", 'auto_id': "NameRuEdit"}
    NAME_TOV_EN = {'title': "Наименование (en):", 'control_type': "Edit", 'auto_id': "NameEnEdit"}
    NAME_NOTE = {'title': "Примечание:", 'control_type': "Edit", 'auto_id': "DescriptionEdit"}
    NET_WEIGHT = {'title': "Вес нетто, кг:", 'control_type': "Edit", 'auto_id': "teNetto"}
    GROSS_WEIGHT = {'title': "Вес брутто, кг:", 'control_type': "Edit", 'auto_id': "teBrutto"}

    #Заголовки полей таблиц
    OTV_TABLE = {'title': "Ответственный (Экспедирование)", 'control_type': "Header", 'found_index': 0}
    SELECT_SPEAKERS = {'title': "Выбор колонок", 'control_type': "Button", 'found_index': 0}
    ORDER_TABLE = {'title': "Заказ", 'control_type': "Header", 'found_index': 0}

    #Спрятанные колонки
    ADDRESS_TABLE = {'title': "Адрес", 'control_type': "ListItem"}
    AUTO_TABLE = {'title': "Автомобиль", 'control_type': "ListItem"}
    NET_WEIGHT_TABLE = {'title': "Вес нетто, кг", 'control_type': "ListItem"}
    DRIVER_TABLE = {'title': "Водитель", 'control_type': "ListItem"}
    DATA_MOD_TABLE = {'title': "Дата изменения", 'control_type': "ListItem"}
    DATA_CREATE_TABLE = {'title': "Дата создания", 'control_type': "ListItem"}
    MEAS_TABLE = {'title': "Ед. измерения", 'control_type': "ListItem"}
    CHANGED_TABLE = {'title': "Кем изменен", 'control_type': "ListItem"}
    CREATED_TE_TABLE = {'title': "Кем создан (ТЕ)", 'control_type': "ListItem"}
    QUANTITY_TABLE = {'title': "Количество", 'control_type': "ListItem"}
    NEW_TABLE = {'title': "Новая версия", 'control_type': "ListItem"}
    NUMBER_GTD_TABLE = {'title': "Номер ГТД", 'control_type': "ListItem"}
    OTV_AUTO_TABLE = {'title': "Ответственный (Автоперевозка)", 'control_type': "ListItem"}
    PLAN_TABLE = {'title': "План. дата доставки", 'control_type': "ListItem"}
    NOTE_TABLE = {'title': "Примечание (ТЕ)", 'control_type': "ListItem"}
    QUANTITY_TE_TABLE = {'title': "Количество ТЕ", 'control_type': "ListItem"}
    NUMBER_FORWARDING_TABLE = {'title': "Номер экспедирования", 'control_type': "ListItem"}

    # Экспедирование форма
    OTV_FORWARDING = {'title': "Ответственный:", 'control_type': "ComboBox", 'auto_id': "sleResponsible"}
    CARGO_RECEIVED = {'title': "Получен груз", 'control_type': "ListItem"}

    # Экспедирование таблица
    FORWARDING = {'title': "Заявки на экспедирование", 'control_type': "ListItem", 'found_index': 0}

    TYPE_TABLE1 = {'title': "Тип строка 1", 'control_type': "DataItem"}
    EXPEDITOR_TABLE1 = {'title': "Экспедитор строка 1", 'control_type': "DataItem"}
    TELEX_RELEASE_TABLE1 = {'title': "Телекс-релиз строка 1", 'control_type': "DataItem"}
    RECEIVE_DOC_TABLE1 = {'title': "Получение докум. строка 1", 'control_type': "DataItem"}
    NOTE_TABLE1 = {'title': "Примечание строка 1", 'control_type': "DataItem", 'found_index': 0}
    CREATED_DATE_TABLE1 = {'title': "Дата создания строка 1", 'control_type': "DataItem", 'found_index': 0}
    UPDATED_DATE_TABLE1 = {'title': "Дата изменения строка 1", 'control_type': "DataItem", 'found_index': 0}
    FINISHED_DATE_TABLE1 = {'title': "Дата завершения строка 1", 'control_type': "DataItem", 'found_index': 0}
    FORWARDING_NUMBER_HEADER = {'title': "Номер экспедирования строка 1", 'control_type': "DataItem", 'found_index': 0}
    TE_COUNT_HEADER = {'title': "Количество ТЕ строка 1", 'control_type': "DataItem", 'found_index': 0}

    # Добавление Файла
    ADD_FILE = {'title': "Выбрать файлы", 'control_type': "Button", 'auto_id': "btnAdd"}
    TEST_FILE = {'title': "test.xls", 'control_type': "ListItem"}
    FILE_1 = {'title': "Файл строка 1", 'control_type': "DataItem", 'found_index': 0}

    # Услуги
    SERVICES_ADD = {'title': "Услуга:", 'control_type': "ComboBox", 'auto_id': "serviceTypeEdit1"}

    #Финансы
    FINANCE = {'title': "Финансы", 'control_type': "Button"}
    OUTGOING_INVOICES = {'title': "Исходящие счета", 'control_type': "ListItem"}
    INCOMING_PAYMENTS = {'title': "Вх. платежи", 'control_type': "TabItem"}
    INCOMING_INVOICES = {'title': "Входящие счета", 'control_type': "ListItem"}
    OUTGOING_PAYMENTS = {'title': "Исходящие платежи", 'control_type': "ListItem"}
    ORG_ACCOUNT_TRANSFERS = {'title': "Переводы (Орг. счета)", 'control_type': "ListItem"}
    SERVICES_SERVICES = {'control_type': "ComboBox", 'auto_id': "leServiceTypeId"}
    SERVICES_BET = {'control_type': "Edit", 'auto_id': "txtChargeValue"}
    SERVICES_CURRENCY = {'control_type': "ComboBox", 'auto_id': "icCurrencyCode"}
    CONNECT_VP = {'title': "Связь с вх. платежами", 'control_type': "Button"}
    CONNECT_TRANSFERS = {'title': "Связь с вх. переводами", 'control_type': "Button"}
    CONNECT_INVOICES = {'title': "Связь с вх. счетами", 'control_type': "Button"}
    SERVICES_OPTIONS = {'control_type': "Button", 'auto_id': "btnOptions"}
    LOOK_SERVICES = {'title': "Показать все счета", 'control_type': "Button", 'found_index': 0}
    ADD_SERVICES = {'control_type': "Button", 'auto_id': "btnAdd"}
    EXPAND = {'title': "Свернуть", 'control_type': "Button", 'found_index': 0}

    # Владки счета
    INCOMING_PAYMENTS = {'title': "Вх. платежи", 'control_type': "TabItem"}
    INCOMING_TRANSFERS = {'title': "Вх. переводы", 'control_type': "TabItem"}
    INCOMING_INVOICES = {'title': "Вх. счета", 'control_type': "TabItem"}
    DIRECT_CLIENT_INVOICES = {'title': "Прямые счета на клиента", 'control_type': "TabItem"}
    OFFSETS = {'title': "Взаимозачеты с вх. счетами", 'control_type': "TabItem"}
    RELATIONS = {'title': "Связи с исх. платежами", 'control_type': "TabItem"}
    PENALTY_INVOICES = {'title': "Пени-счета", 'control_type': "TabItem"}
    FILES = {'title': "Файлы", 'control_type': "TabItem"}
    ADD_FROM_ORDER_BUTTON = {'title': "Добавить из заказа", 'control_type': "Button"}
    QUICK_CREATE_MENU = {'title': "Быстрое создание", 'control_type': "MenuItem"}


    # Валюта
    USD = {'title': "USD", 'control_type': "ListItem"}


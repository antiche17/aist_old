# Автотесты для программы AIST

## Программы и библиотеки
- python 3.11
- pywinauto
- allure
- [остальное](https://gitlab.smartlink.lan/qa/qa/-/blob/main/requirements.txt)

## Проверки 
- [ ] Заказ
  - [x] Создание с типом:
    - [x] Логистика
    - [x] Другие услуги
  - [x] Редактирование (полей заказа)
  - [x] Удаление(без сущностей)
  - [ ] Создание в заказе
    - [x] ТЕ (Bulkership, Container)
    - [x] Перевозки
    - [x] Экспедирование
    - [x] ГТД
    - [ ] Счета(ИС, ВС, ИП, ВП)
  - [ ] Удаление
    - [ ] С одним (те, перевозкой, экспедированием, ГТД, счетом, файл)
    - [ ] Множественное (от 4), в одном заказе (те, перевозкой, экспедированием, ГТД, счетом, файл)
    - [x] Удаление одиночное(без сущностей)
    - [x] Удаление множественное(без сущностей)
- Перевозки
  - [ ] Морская перевозка с маршрутами
  - [ ] Автоперевозка с маршрутами

## Команды для запуска тестов

**Подготовка**:
В командной строке поочерёдно ввести команды:\
`cd /d C:\qa\AIST`\
`call .\.venv1\Scripts\activate`\
Можно запустить bat в C:\qa\AIST файл - `запуск_тестов.bat`

Запуск всех тестов - `pytest --alluredir=./allure-results`

Запуск тестов по отдельным командам:
  - Заказ:
    - Создание с типом "Логистика" - `pytest tests_orders/test_order.py --alluredir=./allure-results`
    - Создание типом "Другие услуги" - `pytest tests_orders/test_2order_dr.py --alluredir=./allure-results`
    - Редактирование полей заказа - `pytest tests_orders/test_order_update.py --alluredir=./allure-results`
    - Удаление заказа и удаление двух заказов - `pytest tests_orders/test_1order_del.py --alluredir=./allure-results`
    - Создание и удаление "Экспедирование" - `pytest tests_orders/test_order_forwarding.py --alluredir=./allure-results`
    - Создание и удаление "Груз" - `pytest tests_orders/test_order_freight.py --alluredir=./allure-results`
    - Создание и удаление "ГТД" - `pytest tests_orders/test_order_gtd.py --alluredir=./allure-results`
    - Создание и удаление "Перевозки" - `pytest tests_orders/test_order_transportation.py --alluredir=./allure-results`
  - Запуск отчета - `allure serve allure-results --lang ru`
  - Удаление истории - `allure generate allure-results --clean`
# Автотесты для программы AIST

## Программы и библиотеки
- python 3.11
- pywinauto
- allure
- [остальное](https://gitlab.smartlink.lan/qa/qa/-/blob/main/requirements.txt)

## Проверки 
- [x] Заказ
  - [x] Создание с типом:
    - [x] Логистика
    - [x] Другие услуги
  - [x] Редактирование (полей заказа)
  - [x] Создание в заказе
    - [x] ТЕ (Bulkership, Container)
    - [x] Перевозки
    - [x] Экспедирование
    - [x] ГТД
    - [x] Счета(ИС, ВС, ИП, ВП)
  - [x] Удаление
    - [x] С одним (те, перевозкой, экспедированием, ГТД, счетом, файл)
    - [x] Множественное (от 4), в одном заказе (те, перевозкой, экспедированием, ГТД, счетом, файл)
    - [x] Удаление одиночное(без сущностей)
    - [x] Удаление множественное(без сущностей)
- Перевозки
  - [ ] Морская перевозка с маршрутами
  - [ ] Автоперевозка с маршрутами
- Таблица Грузы
  - [x] Создание ТЕ из таблицы Грузы
  - [x] Открыть заказ из поля Заказ
  - [x] Выставление данных для отображения в таблице на [основании](https://jira.smartlink.lan/browse/AIST-711)
  - [x] Редактирование полей

## Команды для запуска тестов

**Подготовка**:
Зайти на 192.168.47.177:
    логин auto_test
    пароль 123qweR

Открыть на рабочем столе "запуск_тестов" ПКМ выбрать -> Выполнить с помощью PowerShell
Ввести выбранную ниже команду нажать Enter
После окончания теста
Ввести команду "Запуск отчета" - откроется браузер с отчетами
В поле Тест сюиты нажать "Показать все"
Открыть дерево тестов и найти ранее запущенный тест

ВНИМАНИЕ частые ошибки:
1. Может запустить без выбора базы - выдаст отказано в доступе
    Решение: перезапустить тест заново
2. Не "кликает" в течении 1мин
    Обьяснение: ошибка в коде или ошибка в программе, написать тестировщику какую команду запускали

Запуск тестов по отдельным командам:
  - Заказ:
    - Создание и редактирование с типом "Логистика" - `pytest tests_orders/test_order.py --alluredir=./allure-results`
    - Создание типом "Другие услуги" - `pytest tests_orders/test_2order_dr.py --alluredir=./allure-results`
    - Удаление заказа и удаление двух заказов без сущностей - `pytest tests_orders/test_1order_del.py --alluredir=./allure-results`
    - Создание и удаление "Экспедирование" - `pytest tests_orders/test_order_forwarding.py --alluredir=./allure-results`
    - Создание и удаление "ГТД" - `pytest tests_orders/test_order_gtd.py --alluredir=./allure-results`
    - Создание и удаление "Исходящего счета" - `pytest tests_orders/test_order_finance_is.py --alluredir=./allure-results`
    - Создание и удаление "Исходящего платежа" - `pytest tests_orders/test_order_finance_ip.py --alluredir=./allure-results`
    - Создание и удаление "Входящего платежа" - `pytest tests_orders/test_order_finance_vp.py --alluredir=./allure-results`
    - Создание и удаление "Входящего счета" - `pytest tests_orders/test_order_finance_vs.py --alluredir=./allure-results`
    - Удаление заказ с сущностями - `pytest tests_orders/test_order_del2.py --alluredir=./allure-results`
    - Создание и удаление "Перевозки" - `pytest tests_orders/test_order_transportation.py --alluredir=./allure-results`
    - Создание и удаление "Bulkership" - `pytest tests_orders/test_order_freight_bulkership.py --alluredir=./allure-results`
    - Создание и удаление "Container" - `pytest tests_orders/test_order_freight_container.py --alluredir=./allure-results`
  - Грузы:
    - Создание данных и проверка отображения в таблице Грузы, редактирование данных в таблице. `pytest tests_freight/test_freight.py --alluredir=./allure-results` 
  - Запуск отчета - `allure serve allure-results --lang ru`
  - Удаление истории - `allure generate allure-results --clean`
  - Запуск всех тестов - `pytest --alluredir=./allure-results`
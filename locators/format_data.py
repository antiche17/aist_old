import re
import locale
from datetime import datetime
import pytest_check as check  # если ты используешь pytest-check

MONTHS_RU_EN = {
    'января': 'January', 'февраля': 'February', 'марта': 'March',
    'апреля': 'April', 'мая': 'May', 'июня': 'June',
    'июля': 'July', 'августа': 'August', 'сентября': 'September',
    'октября': 'October', 'ноября': 'November', 'декабря': 'December'
}


def normalize_date(date_str):
    """Приводит дату в строке к объекту datetime.date"""
    if not date_str:
        raise ValueError("Пустая строка — дата не указана")

    # 🧹 Убираем "г." и скобки
    date_str = re.sub(r"\(.*?\)", "", date_str)
    date_str = date_str.replace("г.", "").strip()

    # 🔤 Перевод русских месяцев в английские
    for ru, en in MONTHS_RU_EN.items():
        if ru in date_str.lower():
            date_str = re.sub(ru, en, date_str, flags=re.IGNORECASE)
            break

    # 🧩 Если формат dd.mm.yy — дополняем до dd.mm.20yy
    if re.match(r"^\d{2}\.\d{2}\.\d{2}$", date_str):
        d, m, y = date_str.split(".")
        date_str = f"{d}.{m}.20{y}"

    # ⚙️ Безопасная локаль
    try:
        locale.setlocale(locale.LC_TIME, "C")
    except locale.Error:
        pass

    # 📅 Возможные форматы
    formats = [
        "%d-%m-%Y %H:%M:%S",
        "%d.%m.%Y %H:%M:%S",
        "%d/%m/%Y %H:%M:%S",
        "%d %B %Y %H:%M:%S",

        "%d-%m-%Y %H:%M",
        "%d.%m.%Y %H:%M",
        "%d/%m/%Y %H:%M",
        "%d %B %Y %H:%M",

        "%d.%m.%Y",
        "%d-%m-%Y",
        "%d %B %Y",

        "%d.%m.%y",
        "%d-%м-%y",
        "%d/%m/%y",
    ]

    # 🔍 Пробуем все форматы
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue

    raise ValueError(f"Не удалось распознать формат даты: {date_str}")


def compare_dates(date1, date2, error_message):
    """Жёсткое сравнение дат — если разные, падаем"""
    assert normalize_date(date1) == normalize_date(date2), error_message


def check_equal_dates(value1, value2, field_name):
    """Мягкая проверка дат — не останавливает тест"""
    normalized1 = normalize_date(value1)
    normalized2 = normalize_date(value2)
    check.equal(normalized1, normalized2, f"❌ ФР: Не одинаковый {field_name}")

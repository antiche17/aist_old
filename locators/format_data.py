import locale
from datetime import datetime
import pytest_check as check

MONTHS_RU_EN = {
    'января': 'January', 'февраля': 'February', 'марта': 'March',
    'апреля': 'April', 'мая': 'May', 'июня': 'June',
    'июля': 'July', 'августа': 'August', 'сентября': 'September',
    'октября': 'October', 'ноября': 'November', 'декабря': 'December'
}

def normalize_date(date_str):
    date_str = date_str.replace("г.", "").strip()
    if not date_str:
        raise ValueError("Пустая строка — дата не указана")
    # Преобразуем только если месяц на русском
    for ru, en in MONTHS_RU_EN.items():
        if ru in date_str:
            date_str = date_str.replace(ru, en)
            break
    # Устанавливаем английскую локаль временно
    locale.setlocale(locale.LC_TIME, 'C')
    formats = [
        "%d %B %Y",
        "%d.%m.%Y",
        "%d.%m.%y",
        "%d.%m.%Y %H:%M:%S",
        "%d %B %Y %H:%M:%S"
    ]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Не удалось распознать формат даты: {date_str}")

def compare_dates(date1, date2, error_message):
    assert normalize_date(date1) == normalize_date(date2), error_message

def check_equal_dates(value1, value2, field_name):
    normalized1 = normalize_date(value1)
    normalized2 = normalize_date(value2)
    check.equal(normalized1, normalized2, f"❌ ФР: Не одинаковый {field_name}")
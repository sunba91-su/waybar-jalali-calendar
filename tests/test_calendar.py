import jdatetime

from waybar_jalaly_calendar.holidays import (
    days_to_nowruz,
    get_all_holidays,
    get_hijri_holidays,
    get_jalali_holidays,
)
from waybar_jalaly_calendar.persian_utils import (
    is_iran_weekend,
    to_persian_digits,
)


def test_persian_digits_int():
    assert to_persian_digits(1403) == "۱۴۰۳"


def test_persian_digits_str():
    assert to_persian_digits("15") == "۱۵"


def test_persian_digits_mixed():
    result = to_persian_digits("15 خرداد 1403")
    assert result == "۱۵ خرداد ۱۴۰۳"


def test_friday_is_weekend():
    friday = jdatetime.date(1405, 1, 7)
    assert is_iran_weekend(friday)


def test_saturday_not_weekend():
    saturday = jdatetime.date(1405, 1, 2)
    assert not is_iran_weekend(saturday)


def test_monday_not_weekend():
    monday = jdatetime.date(1405, 1, 4)
    assert not is_iran_weekend(monday)


def test_nowruz_first_day():
    nowruz = jdatetime.date(1405, 1, 1)
    holidays = get_jalali_holidays(nowruz)
    assert "نوروز" in holidays


def test_nowruz_four_days():
    for day in range(1, 5):
        d = jdatetime.date(1405, 1, day)
        assert "نوروز" in get_jalali_holidays(d)


def test_revolution_day():
    revolution = jdatetime.date(1405, 11, 22)
    holidays = get_jalali_holidays(revolution)
    assert "پیروزی انقلاب" in holidays


def test_non_holiday():
    d = jdatetime.date(1405, 3, 16)
    assert get_jalali_holidays(d) == []


def test_get_all_holidays_nowruz():
    d = jdatetime.date(1405, 1, 1)
    all_h = get_all_holidays(d)
    assert "نوروز" in all_h


def test_days_to_nowruz_last_day():
    last_day = jdatetime.date(1404, 12, 29)
    nd = days_to_nowruz(last_day)
    assert nd == 1


def test_days_to_nowruz_first_day():
    nowruz = jdatetime.date(1405, 1, 1)
    nd = days_to_nowruz(nowruz)
    assert nd == 0


def test_days_to_nowruz_farvardin_second():
    d = jdatetime.date(1405, 1, 2)
    nd = days_to_nowruz(d)
    assert nd > 300

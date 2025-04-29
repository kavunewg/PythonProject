import pytest
from .masks import get_mask_card_number, get_mask_account


# Тесты для функции mask_card_or_chet
def test_mask_card():
    assert get_mask_card_number("Карта 1234 5678 9012 3456") == "Карта 1234 ** **** 3456"
    assert get_mask_card_number("Карта 1234 5678 9012") == "Карта 1234 ** **** 9012"
    assert get_mask_card_number("Карта 1234567890123456") == "Карта 1234 ** **** 3456"
    assert get_mask_card_number("Карта 123456") == "Карта 123456"
    assert get_mask_card_number("Карта") == "Карта "


def test_mask_account():
    assert get_mask_card_number("Счет 123456789012") == "Счет ********** 012"
    assert get_mask_card_number("Счет 12") == "Счет **"
    assert get_mask_card_number("Счет") == "Счет "


# Тесты для функции get_date
def test_get_date():
    assert get_mask_account("2023-10-01T12:00:00Z") == "01.10.2023"
    assert get_mask_account("2023-01-15T08:30:00Z") == "15.01.2023"
    assert get_mask_account("2020-02-29T00:00:00Z") == "29.02.2020"  # Високосный год
    assert get_mask_account("invalid-date-string") == "Некорректная дата"


if __name__ == "__main__":
    pytest.main()

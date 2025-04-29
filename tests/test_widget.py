import pytest
from .widget import mask_card_or_chet, get_date


# Параметризованные тесты для функции mask_card_or_chet
@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("Карта 1234 5678 9012 3456", "Карта 1234 ** **** 3456"),
        ("Карта 1234 5678 9012", "Карта 1234 ** **** 9012"),
        ("Карта 1234567890123456", "Карта 1234 ** **** 3456"),
        ("Счет 123456789012", "Счет ********** 012"),
        ("Счет 12", "Счет **"),
        ("Счет", "Счет "),
        ("Карта", "Карта "),
    ],
)
def test_mask_card_or_account(input_data, expected_output):
    assert mask_card_or_chet(input_data) == expected_output


# Тесты для функции get_date
@pytest.mark.parametrize(
    "date_string, expected_output",
    [
        ("2023-10-01T12:00:00Z", "01.10.2023"),
        ("2023-01-15T08:30:00Z", "15.01.2023"),
        ("2020-02-29T00:00:00Z", "29.02.2020"),  # Високосный год
        ("invalid-date-string", "Некорректная дата"),
        ("2023-10-32T12:00:00Z", "Некорректная дата"),  # Некорректная дата
        ("2023-13-01T12:00:00Z", "Некорректная дата"),  # Некорректный месяц
        ("2023-10-T12:00:00Z", "Некорректная дата"),  # Некорректный день
    ],
)
def test_get_date(date_string, expected_output):
    assert get_date(date_string) == expected_output


if __name__ == "__main__":
    pytest.main()

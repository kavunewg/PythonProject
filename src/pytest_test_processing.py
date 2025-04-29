import pytest
from processing import filter_by_state, sort_by_date


# Тесты для функции filter_by_state
@pytest.mark.parametrize(
    "input_data, state, expected_output",
    [
        (
            [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "PENDING"}, {"id": 3, "state": "EXECUTED"}],
            "EXECUTED",
            [{"id": 1, "state": "EXECUTED"}, {"id": 3, "state": "EXECUTED"}],
        ),
        (
            [{"id": 1, "state": "PENDING"}, {"id": 2, "state": "PENDING"}],
            "EXECUTED",
            [],
        ),  # Нет элементов с состоянием EXECUTED
        ([], "EXECUTED", []),  # Пустой список
    ],
)
def test_filter_by_state(input_data, state, expected_output):
    assert filter_by_state(input_data, state) == expected_output


# Тесты для функции sort_by_date
def test_sort_by_date():
    input_data = [
        {"id": 1, "date": "2023-10-01T12:00:00"},
        {"id": 2, "date": "2023-09-30T08:30:00"},
        {"id": 3, "date": "2023-10-01T08:30:00"},  # Одинаковая дата с разным временем
    ]

    expected_descending = [
        {"id": 1, "date": "2023-10-01T12:00:00"},
        {"id": 3, "date": "2023-10-01T08:30:00"},
        {"id": 2, "date": "2023-09-30T08:30:00"},
    ]

    expected_ascending = [
        {"id": 2, "date": "2023-09-30T08:30:00"},
        {"id": 3, "date": "2023-10-01T08:30:00"},
        {"id": 1, "date": "2023-10-01T12:00:00"},
    ]

    assert sort_by_date(input_data) == expected_descending
    assert sort_by_date(input_data, descending=False) == expected_ascending


# Тесты на некорректные форматы дат
def test_sort_by_date_invalid_format():
    input_data = [{"id": 1, "date": "invalid-date"}, {"id": 2, "date": None}, {"id": 3}]

    with pytest.raises(ValueError):
        sort_by_date(input_data)


if __name__ == "__main__":
    pytest.main()

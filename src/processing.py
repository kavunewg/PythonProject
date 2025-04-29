from datetime import datetime
from typing import Dict, List


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data: Список словарей для фильтрации.
    :param state: Значение ключа 'state', по которому будет производиться фильтрация (по умолчанию 'EXECUTED').
    :return: Новый список словарей, соответствующих указанному значению ключа 'state'.
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по значению ключа 'date'.

    :param data: Список словарей для сортировки.
    :param descending: Параметр, указывающий порядок сортировки (по умолчанию True - убывание).
    :return: Новый список словарей, отсортированный по дате.
    """
    return sorted(data, key=lambda x: datetime.fromisoformat(x["date"]), reverse=descending)

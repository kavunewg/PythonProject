def filter_by_state(data, state='EXECUTED'):
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data: Список словарей для фильтрации.
    :param state: Значение ключа 'state', по которому будет производиться фильтрация (по умолчанию 'EXECUTED').
    :return: Новый список словарей, соответствующих указанному значению ключа 'state'.
    """
    return [item for item in data if item.get('state') == state]


from datetime import datetime
def sort_by_date(data, descending=True):
    """
    Сортирует список словарей по значению ключа 'date'.

    :param data: Список словарей для сортировки.
    :param descending: Параметр, указывающий порядок сортировки (по умолчанию True - убывание).
    :return: Новый список словарей, отсортированный по дате.
    """
    return sorted(data, key=lambda x: datetime.fromisoformat(x['date']), reverse=descending)

def filter_by_state(data, state='EXECUTED'):
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data: Список словарей для фильтрации.
    :param state: Значение ключа 'state', по которому будет производиться фильтрация (по умолчанию 'EXECUTED').
    :return: Новый список словарей, соответствующих указанному значению ключа 'state'.
    """
    return [item for item in data if item.get('state') == state]

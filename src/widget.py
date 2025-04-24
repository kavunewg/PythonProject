def mask_card_or_chet(card_number_or_chet_number: int | str) -> str:
    """Маскирует номер карты или номер счета"""
    card_number_or_chet_number = str(card_number_or_chet_number)


    card_mask = card_number[0:7] + "*" * 6 + card_number[12:]
    card_mask = card_mask[0:5] + " " + card_mask[5:9] + " " + card_mask[9:13] + " " + card_mask[13:17]

    return card_mask


def get_date(date: int | str) -> str:
    pass
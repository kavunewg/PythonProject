def get_mask_card_number(card_number: int | str) -> str:
    """Маскирует номер карты"""
    card_number = str(card_number)
    card_number = card_number.replace(" ", "")

    card_mask = card_number[0:7] + "*" * 6 + card_number[12:]
    card_mask = card_mask[0:5] + " " + card_mask[5:9] + " " + card_mask[9:13] + " " + card_mask[13:17]

    return card_mask


def get_mask_account(account: int | str) -> str:
    """Маскирует номер счета"""
    mask_account = str(account)
    mask_account = mask_account.replace(" ", "")

    chet_mask_account = "**" + mask_account[16:21]

    return chet_mask_account

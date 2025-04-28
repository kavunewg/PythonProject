def mask_card_or_chet(card_or_chet_number: int | str) -> str:
    """Маскирует номер карты или номер счета"""
    parts = card_or_chet_number.split()
    name = ' '.join(parts[:-1])
    number = parts[-1]

    if name.lower().startswith("счет"):
        # Если это счет, зашифровываем последние 4 цифры
        encrypted_number = '**' + number[-4:]
    else:
        # Если это карта, зашифровываем все, кроме первых 6 и последних 4 цифр
        encrypted_number = number[:4] + ' ' + number[5:7] + '**' + ' ' + '****' + ' ' + number[-4:]

    return f"{name} {encrypted_number}"


def get_date(date_string):
    # Разделяем строку по символу 'T' и берем первую часть (дату)
    date_part = date_string.split('T')[0]

    # Разделяем дату на год, месяц и день
    year, month, day = date_part.split('-')

    # Формируем строку в нужном формате
    formatted_date = f"{day}.{month}.{year}"

    return formatted_date

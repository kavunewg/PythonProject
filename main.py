from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_card_or_chet, get_date

if __name__ == "__main__":
    # Проверка домашки 9.1 Poetry. Оформление кода
    print()
    print("Домашнее задание 9.1 Poetry. Оформление кода")
    print(get_mask_card_number("1234 1234 1234 1234"))
    print(get_mask_account("1234 56789 9876 543 2 10 1"))
    print(get_mask_card_number(111 ))
    # Проверка домашки 9.2 Основы Git
    print()
    print("Домашнее задание 9.2 Основы Git")
    print(mask_card_or_chet("Maestro 1596837868705199"))
    print(mask_card_or_chet("Счет 64686473678894779589"))
    print(mask_card_or_chet("MasterCard 7158300734726758"))
    print(mask_card_or_chet("Счет 35383033474447895560"))
    print(mask_card_or_chet("Visa Classic 6831982476737658"))
    print(mask_card_or_chet("Visa Platinum 8990922113665229"))
    print(mask_card_or_chet("Visa Gold 5999414228426353"))
    print(mask_card_or_chet("Счет 73654108430135874305"))
    print()
    print(get_date("2024-03-11T02:26:18.671407"))
    print(get_date("2023-12-25T15:30:00.000000"))

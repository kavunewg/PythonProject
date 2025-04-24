from src.masks import get_mask_card_number, get_mask_account

if __name__ == "__main__":
    print(get_mask_card_number("1234 1234 1234 1234"))
    print(get_mask_account("1234 56789 9876 543 2 10 1"))

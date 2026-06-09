def get_mask_card_number(card_number: str) -> str:
    """
    Принимает на вход номер карты и возвращает ее маску. Видны первые 6 цифр и последние 4 цифры,
    остальные символы отображаются звездочками,
    номер разбит по блокам по 4 цифры, разделенным пробелами.
    """
    if len(card_number) != 16:
        raise ValueError("Длина номера карты - 16 символов.")

    split_number = " ".join(card_number[i : i + 4] for i in range(0, len(card_number), 4))
    mask_number = split_number[:7] + "** ****" + split_number[-5:]
    return mask_number


def get_mask_account(account_id: str) -> str:
    """
    Принимает на вход номер счета и возвращает его маску. Номер счета замаскирован,
    видны только последние 4 цифры номера, а перед ними — две звездочки.
    """
    if len(account_id) < 4:
        raise ValueError("Длина номера счета должна быть больше 4-х символов.")

    return "**" + account_id[-4:]

"""Содержит новые функции приложения"""

from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_type_and_number: str) -> str:
    """Маскирует номер карты"""
    parts = card_type_and_number.split()
    if len(parts) < 2:
        raise ValueError("Некорректные входные данные")
    card_type = " ".join(parts[:-1])
    card_number = parts[-1]
    digits = "".join(filter(str.isdigit, card_number))  # Проверка на числовое значение

    # Определение категорий по содержимому: карта или счет
    keywords_card = ["visa", "visa classic", "visa platinum", "visa gold", "mastercard", "maestro"]
    keywords_account = ["счет", "счёт"]

    def is_type(keywords):
        return any(keyword in card_type.lower() for keyword in keywords)

    if is_type(keywords_account):
        # Маскируем счет
        if len(digits) < 4:
            raise ValueError("Длина номера счета должна быть больше 4-х цифр.")
        masked_number = get_mask_account(digits)
        return f"Счет {masked_number}"

    elif is_type(keywords_card):
        # Маскируем карту
        if len(digits) != 16:
            raise ValueError("Длина номера карты должна быть 16 цифр.")
        masked_number = get_mask_card_number(digits)
        return f"{card_type} {masked_number}"

    else:
        raise ValueError(
            f"Неизвестный тип данных. Введите один из следующих вариантов: "
            f"{', '.join(keywords_card).title()} или {keywords_account[0]}."
        )


print(mask_account_card("Viski 6468647367889477"))

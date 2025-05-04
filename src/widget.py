from datetime import datetime

from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_type_and_number: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от того, что на входе функции.
    """
    parts = card_type_and_number.split()
    if len(parts) < 2:
        raise ValueError("Некорректные входные данные: строка должна содержать тип и номер.")
    card_type = " ".join(parts[:-1])
    card_number = parts[-1]
    digits = "".join(filter(str.isdigit, card_number))  # Извлечение цифр из строки card_number

    # Определение категорий по содержимому: карта или счет
    keywords_card = ["visa", "visa classic", "visa platinum", "visa gold", "mastercard", "maestro"]
    keywords_account = ["счет", "счёт"]

    def is_type(keywords: list) -> bool:
        """
        Определяет, что содержит строка: карту или счет.
        """
        return any(keyword in card_type.lower() for keyword in keywords)

    if is_type(keywords_account):
        # Маскируем счет
        masked_number = get_mask_account(digits)
        return f"Счет {masked_number}"

    elif is_type(keywords_card):
        # Маскируем карту
        masked_number = get_mask_card_number(digits)
        return f"{card_type} {masked_number}"

    else:
        raise ValueError(
            f"Неизвестный тип данных. Введите один из следующих вариантов: "
            f"{', '.join(keywords_card).title()} или {keywords_account[0]}."
        )


def get_date(date: str) -> str:
    """
    Принимает на вход строку (например "2024-03-11T02:26:18.671407") и возвращает строку с датой в формате:
    'ДД.ММ.ГГГГ'
    """
    converted_date = datetime.fromisoformat(date)
    return converted_date.strftime("%d.%m.%Y")

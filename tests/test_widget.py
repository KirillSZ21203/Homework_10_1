import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("input_str, output_str", [("Счет 312312385505", "Счет **5505")])
def test_mask_account_card(
    test_number_1: str,
    test_number_3: str,
    test_number_6: int,
    test_number_7: int,
    empty_string: str,
    input_str: str,
    output_str: str,
) -> None:
    assert mask_account_card(input_str) == output_str
    assert mask_account_card(f"Visa Platinum {test_number_6}") == "Visa Platinum 1234 56** **** 3456"
    assert mask_account_card(f"Visa Classic {test_number_6}") == "Visa Classic 1234 56** **** 3456"
    assert mask_account_card(f"Visa {test_number_6}") == "Visa 1234 56** **** 3456"
    assert mask_account_card(f"Maestro {test_number_6}") == "Maestro 1234 56** **** 3456"
    assert mask_account_card(f"Mastercard {test_number_6}") == "Mastercard 1234 56** **** 3456"
    assert mask_account_card(f"Счет {test_number_7}") == "Счет **3368"
    assert mask_account_card(f"Счёт {test_number_7}") == "Счет **3368"

    with pytest.raises(ValueError) as exc_info:
        mask_account_card(empty_string)
    assert str(exc_info.value) == "Некорректные входные данные: строка должна содержать тип и номер."

    with pytest.raises(ValueError) as exc_info:
        mask_account_card(test_number_1)
    assert str(exc_info.value) == "Некорректные входные данные: строка должна содержать тип и номер."

    with pytest.raises(ValueError) as exc_info:
        mask_account_card(f"{test_number_3} Mastercard")
    assert str(exc_info.value) == (
        "Неизвестный тип данных. Введите один из следующих вариантов: Visa, Visa Classic, Visa Platinum, "
        "Visa Gold, Mastercard, Maestro или счет."
    )

    with pytest.raises(ValueError) as exc_info:
        mask_account_card("MIR 1515248365699782")
    assert str(exc_info.value) == (
        "Неизвестный тип данных. Введите один из следующих вариантов: Visa, Visa Classic, Visa Platinum, "
        "Visa Gold, Mastercard, Maestro или счет."
    )


@pytest.mark.parametrize("input_date, output_date", [("2029-05-10T02:26:18.671407", "10.05.2029")])
def test_get_date(empty_string: str, input_date: str, output_date: str) -> None:
    assert get_date(input_date) == output_date
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2025-05-07T09:02:18.971407") == "07.05.2025"
    assert get_date("9999-12-31T09:02:18.771407") == "31.12.9999"
    assert get_date("9999-12-31T23:59:59.999999") == "31.12.9999"
    assert get_date("0001-01-01T09:02:18.771407") == "01.01.0001"
    assert get_date("0001-01-01T01:01:01.01") == "01.01.0001"

    with pytest.raises(ValueError) as exc_info:
        get_date(empty_string)
    assert str(exc_info.value) == "Введенная дата не должна быть пустой"

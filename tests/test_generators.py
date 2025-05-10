import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions: list, another_transaction: list, empty_list: list, dict_transaction_1: dict, dict_transaction_2: dict) -> None:
    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == dict_transaction_1
    assert next(generator) == dict_transaction_2

    with pytest.raises(ValueError) as exc_info:
        new_generator = filter_by_currency(another_transaction, "USD")
        print(next(new_generator))
    assert str(exc_info.value) == "Такой валюты нет в списке транзакций"

    with pytest.raises(ValueError) as exc_info:
        new_generator = filter_by_currency(empty_list, "USD")
        print(next(new_generator))
    assert str(exc_info.value) == "Пустой список транзакций"


def test_transaction_descriptions(
    transactions: list, another_transaction: list, transaction_statuses: list, empty_list: list
) -> None:
    generator = transaction_descriptions(transactions)
    assert next(generator) == transaction_statuses[0]
    assert next(generator) == transaction_statuses[1]

    new_generator = transaction_descriptions(another_transaction)
    assert next(new_generator) == transaction_statuses[2]

    with pytest.raises(ValueError) as exc_info:
        new_generator = transaction_descriptions(empty_list)
        print(next(new_generator))
    assert str(exc_info.value) == "Пустой список транзакций"


def test_card_number_generator(card_numbers: list, extreme_values: list, empty_list: list, id_list: list) -> None:
    generator = card_number_generator(1, 10)
    assert next(generator) == card_numbers[0]
    assert next(generator) == card_numbers[1]
    assert next(generator) == card_numbers[2]

    with pytest.raises(ValueError) as exc_info:
        new_generator = card_number_generator(extreme_values[0], extreme_values[1])
        print(next(new_generator))
    assert str(exc_info.value) == "Некорректный диапазон чисел"

    with pytest.raises(ValueError) as exc_info:
        new_generator = card_number_generator(empty_list, id_list)
        print(next(new_generator))
    assert str(exc_info.value) == "Некорректный тип данных"

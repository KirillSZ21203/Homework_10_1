import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, masked_card_number", [("8888888888888888", "8888 88** **** 8888")])
def test_mask_card_number(
    test_number_3: str, test_number_2: str, card_number: str, masked_card_number: str, empty_string: str
) -> None:
    assert get_mask_card_number(test_number_3) == "1234 56** **** 3456"
    assert get_mask_card_number(test_number_2) == "6543 21** **** 4321"
    assert get_mask_card_number(card_number) == masked_card_number
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(empty_string)
    assert str(exc_info.value) == "Длина номера карты - 16 символов."
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(test_number_3[:-1])
    assert str(exc_info.value) == "Длина номера карты - 16 символов."
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(test_number_3 + "7")
    assert str(exc_info.value) == "Длина номера карты - 16 символов."


@pytest.mark.parametrize("account, mask_account", [("10915", "**0915")])
def test_mask_account(test_number_1: str, empty_string: str, account: str, mask_account: str) -> None:
    assert get_mask_account(test_number_1) == "**3535"
    assert get_mask_account(account) == mask_account
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(empty_string)
    assert str(exc_info.value) == "Длина номера счета должна быть больше 4-х символов."
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("123")
    assert str(exc_info.value) == "Длина номера счета должна быть больше 4-х символов."

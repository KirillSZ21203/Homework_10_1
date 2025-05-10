import pytest


@pytest.fixture
def test_number_1() -> str:
    return "88005553535"


@pytest.fixture
def test_number_2() -> str:
    return "6543210987654321"


@pytest.fixture
def test_number_3() -> str:
    return "1234567890123456"


@pytest.fixture
def test_number_4() -> str:
    return "123456789012345"


@pytest.fixture
def test_number_5() -> str:
    return "1234567890"


@pytest.fixture
def test_number_6() -> int:
    return 1234567890123456


@pytest.fixture
def test_number_7() -> int:
    return 5323368


@pytest.fixture
def id_list() -> list:
    return [41428829, 939719570, 594226727, 615064591]


@pytest.fixture
def empty_string() -> str:
    return ""


@pytest.fixture
def empty_list() -> list:
    return []


@pytest.fixture
def transactions() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


@pytest.fixture
def another_transaction() -> list:
    return [
        {
            "id": 123456789,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        }
    ]


@pytest.fixture
def transaction_statuses() -> list:
    return ["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет"]


@pytest.fixture
def card_numbers() -> list:
    return ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]


@pytest.fixture
def extreme_values() -> list:
    return [int(-123e123), 9999999999999999 + 1]


@pytest.fixture
def dict_transaction_1() -> dict:
    return {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


@pytest.fixture
def dict_transaction_2() -> dict:
    return {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
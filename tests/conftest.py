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

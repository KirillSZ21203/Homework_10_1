import pytest

from src.proccessing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "input_list, output_list",
    [
        (
            [
                {"id": 14328829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 679719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 14328829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 679719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
    ],
)
def test_filter_by_state(id_list: list, empty_list: list, input_list: list, output_list: list) -> None:
    assert filter_by_state(input_list) == output_list
    assert (
        filter_by_state(
            [
                {"id": id_list[0], "state": "COMPLETED", "date": "2020-05-15T14:22:10.123456"},
                {"id": id_list[1], "state": "FAILED", "date": "2019-11-23T09:45:30.654321"},
                {"id": id_list[2], "state": "PROCESSING", "date": "2021-01-10T12:00:00.000000"},
                {"id": id_list[3], "state": "CANCELLED", "date": "2018-08-05T20:15:45.789012"},
            ]
        )
        == empty_list
    )
    assert filter_by_state(
        [
            {"id": id_list[0], "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": id_list[1], "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": id_list[2], "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": id_list[3], "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    ) == [
        {"id": id_list[0], "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": id_list[1], "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert filter_by_state(empty_list) == empty_list


@pytest.mark.parametrize(
    "input_list, output_list",
    [
        (
            [
                {"id": 14328829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 679719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 14328829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 679719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
    ],
)
def test_sort_by_date(
    id_list: list, empty_list: list, test_number_5: str, input_list: list, output_list: list
) -> None:
    assert sort_by_date(
        [
            {"id": id_list[0], "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": id_list[1], "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": id_list[2], "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": id_list[3], "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    ) == [
        {"id": id_list[0], "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": id_list[3], "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": id_list[2], "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": id_list[1], "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert sort_by_date(input_list) == output_list

    with pytest.raises(KeyError) as exc_info:
        sort_by_date(empty_list)
    assert str(exc_info.value) == "'Нет ключей с именем \"date\"'"

    with pytest.raises(KeyError) as exc_info:
        sort_by_date(
            [
                {"id": int(test_number_5), "state": "EXECUTED", "data": "2019-07-03T18:35:29.512364"},
                {"id": int(test_number_5), "state": "EXECUTED", "data": "2018-06-30T02:08:58.425572"},
            ]
        )
    assert str(exc_info.value) == "'Нет ключей с именем \"date\"'"

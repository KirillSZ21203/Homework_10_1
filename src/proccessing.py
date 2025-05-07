def filter_by_state(dict_list: list, state: str = "EXECUTED") -> list:
    """Принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""
    new_list = []
    for dictionary in dict_list:
        if dictionary["state"] == state:
            new_list.append(dictionary)
    return new_list


def sort_by_date(dict_list: list, reverse_sort_order: bool = True) -> list:
    """Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (date)"""
    if not any("date" in dictionary for dictionary in dict_list):
        raise KeyError('Нет ключей с именем "date"')
    return sorted(dict_list, key=lambda x: x["date"], reverse=reverse_sort_order)

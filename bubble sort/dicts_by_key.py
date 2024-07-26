def sorting_dictionaries(dict_list: list) -> list:
    len_dict_list = len(dict_list)
    for i in range(0, len_dict_list):
        swapped = False
        for j in range(0, len_dict_list - i - 1):
            if dict_list[j]['score'] > dict_list[j+1]['score']:
                dict_list[j], dict_list[j+1] = dict_list[j+1], dict_list[j]
                swapped = True
        if not swapped:
            break
    return dict_list


students = [
    {"name": "John", "score": 88},
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 74},
    {"name": "Daisy", "score": 85},
    {"name": "Charlie", "score": 78}
]

print(sorting_dictionaries(students))
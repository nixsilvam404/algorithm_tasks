def sorting_mixed_datatypes (mixed_data_types: list) -> list:
    l = len(mixed_data_types)
    for itr in range(0, l):
        swapped = False
        for cmp in range(0, l-1-itr):
            if int(mixed_data_types[cmp]) > int(mixed_data_types[cmp + 1]):
                mixed_data_types[cmp], mixed_data_types[cmp + 1] = mixed_data_types[cmp + 1], mixed_data_types[cmp]
                swapped = True
        if not swapped:
            break
    return mixed_data_types


mixed_list = mixed_list = [3, "10", 1, "20", 2, "15", 5]
print(sorting_mixed_datatypes(mixed_list))

mixed_list2 = [2, "1", 3, "4", 5, "6", 7]
print(sorting_mixed_datatypes(mixed_list2))



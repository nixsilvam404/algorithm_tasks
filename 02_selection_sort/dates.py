def sorting_dates(arr: list) -> list:
    l = len(arr)
    for i in range(l):
        min_index = i
        for j in range(i + 1, l):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

dates = ["2022-12-01", "2021-05-15", "2023-03-23", "2020-11-11", "2022-01-01"]
sorted_arr = sorting_dates(dates)
print("Sorted array is:", sorted_arr)
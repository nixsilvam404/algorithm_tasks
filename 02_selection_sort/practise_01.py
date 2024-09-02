def selection_sort(arr: list) -> list:
    l = len(arr)
    for i in range(l):
        min_index = i
        for j in range(i + 1, l):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


words = ["apple", "banana", "fig", "grape", "cherry"]
print(selection_sort(words))
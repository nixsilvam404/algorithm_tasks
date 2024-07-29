def sorting_tuples(arr: list) -> list:
    l = len(arr)
    for i in range(l):
        min_index = i
        for j in range(0 + i, l):
            if arr[j][1] < arr[min_index][1]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

students = [
    ("John", 88),
    ("Alice", 92),
    ("Bob", 74),
    ("Daisy", 85),
    ("Charlie", 78)
]
print(sorting_tuples(students))

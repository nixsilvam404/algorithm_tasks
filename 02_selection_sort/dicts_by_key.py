def sorting_dictionaries(arr: list) -> list:
    l = len(arr)
    for i in range(l):
        min_index = i
        for j in range(i+1, l):
            if arr[min_index]["name"] > arr[j]["name"]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


students = [
    {"name": "John", "score": 88},
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 74},
    {"name": "Daisy", "score": 85},
    {"name": "Charlie", "score": 78}
]
print(sorting_dictionaries(students))
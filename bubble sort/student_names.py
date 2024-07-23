def alphabetically (names: list):
    n = len(names)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if names[j].lower() > names[j+1].lower():
                names[j], names[j+1] = names[j+1], names[j]
                swapped = True
        if not swapped:
            break
    return names


names = ["John", "Alice", "Bob", "Daisy", "Charlie"]
sorted_names = alphabetically(names)
print(sorted_names)

names_2 = ["john", "Alice", "bob", "DAISY", "charlie"]
sorted_names_2 = alphabetically(names_2)
print(sorted_names_2)

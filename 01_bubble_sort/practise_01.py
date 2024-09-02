def bubble_sort(num_list: list) -> list:
    l = len(num_list)
    for i in range(l):
        swapped = False
        for j in range(0, l-i-1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
                swapped = True
        if not swapped:
            break
    return num_list

numbers = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(numbers))
                
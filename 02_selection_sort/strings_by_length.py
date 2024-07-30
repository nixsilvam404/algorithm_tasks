from typing import List

def sorting_strings(arr: List[str]) -> List[str]:
    """Sorting a List of Strings by Their Length using Selection Sort

    Args:
        arr (List[str]): a list of strings

    Returns:
        List[str]: a list of strings ordered by lenght
    """
    l = len(arr)
    for i in range(l):
        min_index = i
        for j in range(i + 1, l):
            if len(arr[j]) < len(arr[min_index]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
print(sorting_strings(words))

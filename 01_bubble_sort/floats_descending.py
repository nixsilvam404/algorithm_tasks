from typing import List

def sortnig_floats_desc(arr: List[float]) -> List[float]:
    """Sorting a List of Floats in Descending Order using Bubble Sort

    Args:
        arr (List[float]): a list of floats

    Returns:
        List[float]: list of floats in descending order
    """
    l = len(arr)
    for i in range(0, l):
        swapped = False
        for j in range(0, l - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

float_numbers = [3.14, 2.71, 1.41, 1.73, 0.58, 4.67]
print(sortnig_floats_desc(float_numbers))

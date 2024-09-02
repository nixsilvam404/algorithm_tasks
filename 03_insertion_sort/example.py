def insertion_sort(arr: list) -> list:
    """
    Insertion Sort Algorithm

    Summary:
    Insertion Sort is a simple comparison-based sorting algorithm. It builds the final sorted array (or list) 
    one item at a time. It is much less efficient on large lists than more advanced algorithms such as Quick Sort, 
    Heap Sort, or Merge Sort. However, it performs well on small or nearly sorted lists.

    Advantages:
    - Simple to Understand: Easy to implement and reason about, making it great for educational purposes.
    - Adaptive: Efficient for data that is already substantially sorted; it has a best-case time complexity of O(n).
    - Stable: Preserves the relative order of equal elements.
    - In-Place Sorting: Requires only a constant amount of additional memory (O(1)).

    Disadvantages:
    - Inefficient for Large Datasets: Has a time complexity of O(n^2) in the average and worst cases, making it impractical for large lists.
    - Slow: Compared to more advanced algorithms like Quick Sort or Merge Sort, Insertion Sort is generally slower on average-sized lists.
    - Not Optimal for Random Data: While it excels with nearly sorted data, it is not as efficient with data that is in a random order.

    Parameters:
    - arr: List of elements to be sorted

    Returns:
    - Sorted list of elements
    """
    len_arr = len(arr)  # Get the length of the array
    for index in range(1, len_arr):
        key = arr[index]  # Current element to be placed
        prev_index = index - 1

        # Move elements of arr[0..index-1], that are greater than key,
        # to one position ahead of their current position
        while prev_index >= 0 and key < arr[prev_index]:
            arr[prev_index + 1] = arr[prev_index]
            prev_index -= 1

        # Place the key after the element just smaller than it
        arr[prev_index + 1] = key

    return arr  # Return the sorted array

# Example usage
numbers = [12, 11, 13, 5, 6]
sorted_numbers = insertion_sort(numbers)
print("Sorted array is:", sorted_numbers)

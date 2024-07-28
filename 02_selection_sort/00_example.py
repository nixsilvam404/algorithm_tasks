def selection_sort(arr):
    """
    Selection Sort Algorithm

    Summary:
    Selection Sort is a simple comparison-based sorting algorithm. It works by repeatedly finding the minimum 
    element from the unsorted portion of the list and swapping it with the first unsorted element. The process 
    continues until the entire list is sorted.

    Advantages:
    - Simple to Understand: Easy to grasp and implement, making it suitable for educational purposes.
    - Minimal Additional Memory: In-place sorting algorithm that requires only a constant amount of additional memory (O(1)).
    - Predictable Number of Swaps: Always performs exactly (n-1) swaps, which can be beneficial in scenarios where write operations are costly.

    Disadvantages:
    - Inefficient for Large Datasets: Has a time complexity of O(n^2) for both the worst and average cases, making it impractical for large lists.
    - Slow: Generally slower compared to more advanced algorithms like Quick Sort or Merge Sort due to its quadratic time complexity.
    - Redundant Comparisons: Continues to compare elements even if the array is already sorted.
    - Unscalable: Not suitable for large lists due to its inefficiency and high number of comparisons.

    Parameters:
    - arr: List of elements to be sorted

    Returns:
    - Sorted list of elements
    """
    n = len(arr)  # Get the length of the array
    for i in range(n):
        # Assume the minimum is the first element of the unsorted part
        min_index = i
        # Test against elements after i to find the smallest element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Update min_index if a smaller element is found
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr  # Return the sorted array

# Example usage
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array is:", sorted_arr)


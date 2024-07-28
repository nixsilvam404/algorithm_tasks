def bubble_sort(arr):
    """
    Bubble Sort Algorithm

    Summary:
    While Bubble Sort is a great educational tool and can be useful 
    for small or nearly sorted datasets, it is generally not suitable for large 
    datasets due to its inefficiency. For larger datasets, algorithms like Quick 
    Sort, Merge Sort, or Timsort (used by Python's built-in sort) are preferred.

    Advantages:
    - Simple to understand and implement.
    - Minimal additional memory required.
    - Stable sorting algorithm.
    - Adaptive for nearly sorted data with early termination.

    Disadvantages:
    - Inefficient for large datasets due to O(n^2) time complexity.
    - Slow compared to more advanced sorting algorithms.
    - Performs redundant comparisons.
    - High number of swaps.

    Parameters:
    - arr: List of elements to be sorted

    Returns:
    - Sorted list of elements
    """
    n = len(arr)  # Get the length of the array
    for i in range(n):  # Outer loop to go through each element
        swapped = False  # Initialize swapped to False at the start of each pass
        for j in range(0, n-i-1):  # Inner loop to compare adjacent elements
            if arr[j] > arr[j+1]:  # If the current element is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap the elements
                swapped = True  # Set swapped to True if a swap is made
        print(f"Array after pass {i+1}: {arr}")  # Print the array after each pass for visualization
        if not swapped:  # If no swaps were made during the inner loop, the array is sorted
            break  # Break out of the loop early
    return arr  # Return the sorted array

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Final sorted array is:", sorted_arr)

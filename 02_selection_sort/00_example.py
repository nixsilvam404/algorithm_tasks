def selection_sort(arr):
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

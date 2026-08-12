# Define a function to implement the merge sort algorithm
def mergesort(arr):
    # Base case: if the array has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Find the middle index of the array to split it into two halves
    mid = len(arr) // 2
    
    # Split the array into left and right halves
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort the left and right halves
    left = mergesort(left)
    right = mergesort(right)

    # Merge the sorted left and right halves back into the original array
    i = j = k = 0  # Initialize indices for left, right, and original arrays
    while i < len(left) and j < len(right):
        # Compare elements from left and right, and place the smaller one in the original array
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1  # Move to the next position in the original array

    # If there are remaining elements in the left half, append them to the original array
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    # If there are remaining elements in the right half, append them to the original array
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    
    # Return the sorted array
    return arr

# Test the merge sort function with the example array
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(mergesort(arr))
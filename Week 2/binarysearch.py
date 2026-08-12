def binsearch(arr, key):
    low = 0
    high = len(arr)-1
    
    while low <= high:
        mid = low + (high - low) // 2
        if key == arr[mid]:
            return mid
        elif key > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return - 1

arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

arr.sort()
print(binsearch(arr, 2))
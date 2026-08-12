def selectionsort(arr):
    for i in range(0, len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(selectionsort(arr))
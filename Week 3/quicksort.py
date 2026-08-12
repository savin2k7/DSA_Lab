def quickSort(arr, low, high):
    if low >= high:
        return

    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]

    quickSort(arr, low, i - 1)
    quickSort(arr, i + 1, high)

    return arr


arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(quickSort(arr, 0, len(arr) - 1))
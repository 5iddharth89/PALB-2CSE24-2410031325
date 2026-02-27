def threeWayPartition(arr, a, b):
    start, i, end = 0, 0, len(arr) - 1

    while i <= end:
        if arr[i] < a:
            arr[i], arr[start] = arr[start], arr[i]
            start += 1
            i += 1
        elif arr[i] > b:
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1
        else:
            i += 1

    return arr


print(threeWayPartition([1,4,3,6,2,1], 1, 3))

def reverse_array(arr):
    i, j = 0, len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr

# Example
arr = [1, 4, 3, 2, 6, 5]
print(reverse_array(arr))

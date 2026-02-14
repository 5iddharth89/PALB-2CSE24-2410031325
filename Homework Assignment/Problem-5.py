def largest_element(arr):
    largest = arr[0]
    for x in arr:
        if x > largest:
            largest = x
    return largest

# Example
arr = [1, 8, 7, 56, 90]
print(largest_element(arr))

def get_min_max(arr):
    minimum = maximum = arr[0]
    for x in arr:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    return minimum, maximum

# Example
arr = [1, 4, 3, 5, 8, 6]
print(get_min_max(arr))

def minChocolateDiff(arr, m):
    n = len(arr)
    if m > n:
        return 0

    arr.sort()
    diff = float('inf')

    for i in range(n - m + 1):
        diff = min(diff, arr[i + m - 1] - arr[i])

    return diff


# Example
print(minChocolateDiff([3,4,1,9,56,7,9,12], 5))

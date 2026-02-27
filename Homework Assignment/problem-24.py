def minSwaps(arr, k):
    good = sum(1 for x in arr if x <= k)

    bad = sum(1 for x in arr[:good] if x > k)

    ans = bad
    left = 0

    for right in range(good, len(arr)):
        if arr[left] > k:
            bad -= 1
        if arr[right] > k:
            bad += 1

        ans = min(ans, bad)
        left += 1

    return ans


print(minSwaps([2,1,5,6,3], 3))

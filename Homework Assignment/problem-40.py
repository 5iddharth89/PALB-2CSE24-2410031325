def subsets(nums):
    res = [[]]

    for num in nums:
        res += [curr + [num] for curr in res]

    return res


print(subsets([1,2,3]))

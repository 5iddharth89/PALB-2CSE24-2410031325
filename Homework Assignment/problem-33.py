def combinationSum2(candidates, target):
    candidates.sort()
    res = []

    def backtrack(start, path, total):
        if total == target:
            res.append(path[:])
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            if total + candidates[i] > target:
                break
            backtrack(i+1, path + [candidates[i]], total + candidates[i])

    backtrack(0, [], 0)
    return res


print(combinationSum2([10,1,2,7,6,1,5], 8))

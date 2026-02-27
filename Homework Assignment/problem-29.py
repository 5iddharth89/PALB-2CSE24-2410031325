import bisect

def matrixMedian(mat):
    r, c = len(mat), len(mat[0])
    low, high = 1, 10**9

    desired = (r*c + 1)//2

    while low < high:
        mid = (low + high)//2
        count = 0

        for row in mat:
            count += bisect.bisect_right(row, mid)

        if count < desired:
            low = mid + 1
        else:
            high = mid

    return low


print(matrixMedian([[1,3,5],[2,6,9],[3,6,9]]))

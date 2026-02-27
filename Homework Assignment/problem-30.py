def rowWithMax1s(arr):
    max_row = -1
    max_count = 0

    for i, row in enumerate(arr):
        count = sum(row)
        if count > max_count:
            max_count = count
            max_row = i

    return max_row


print(rowWithMax1s([[0,1,1,1],[0,0,1,1],[1,1,1,1]]))

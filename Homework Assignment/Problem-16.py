def mergeIntervals(intervals):
    intervals.sort()
    merged = [intervals[0]]
    
    for i in intervals[1:]:
        if merged[-1][1] >= i[0]:
            merged[-1][1] = max(merged[-1][1], i[1])
        else:
            merged.append(i)
    
    return merged

# Example
print(mergeIntervals([[1,3],[2,6],[8,10],[15,18]]))

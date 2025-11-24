# why it works:
#   - first we need to sort intervals to place them in order of "start"
#   - we initiate result with first interval from list
#   - then we simply iterate over the rest intervals 
#          and if current interval overlaps with previous (start <= previous interval's end), 
#              then we update the resulting (previous) interval 
#              otherwise we add new interval to resulting array

def mergeIntervals(intervals: list[list[int]]) -> list[int]:
    intervals.sort(key=lambda i: i[0])
    res = [intervals[0]]
    for i in intervals[1:]:
        if i[0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], i[1])
        else:
            res.append(i)

    return res

input = [[12,15], [4,10], [2,5]]
res = mergeIntervals(input)
print(res)

def mostWater(heights: list[int]) -> list[int]:
    left, right = 0, len(heights)-1
    sq = 0
    res = []
    while left < right:
        curSq = max(heights[left], heights[right]) * (right - left)
        if curSq > sq:
            res = [ left, right ]
        
        if left < right:
            left += 1
        else:
            right -= 1
    return res

arr = [ 1, 8, 6, 2, 5, 4, 8, 3, 7 ]
print(mostWater(arr))


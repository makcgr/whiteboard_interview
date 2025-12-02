def squaresOfSortedArr(nums: list[int]) -> list[int]:
    res = []
    l, r = 0, len(nums)-1
    while l <= r:
        if nums[l] ** 2 > nums[r] ** 2:
            res.append(nums[l] ** 2)
            l += 1
        else:
            res.append(nums[r] ** 2)
            r -= 1
    
    return res[::-1]

print(squaresOfSortedArr([-4,-1,0,3,10]))

# why this works:
# squares are non-negative, so sort order might be compromised
# though if we use two pointers to  go from hypothetical zero to edges, the problem is solved
# the cleaner solution would be to go from edges to the middle (in the opposite way),
# instead of going from the "middle" value of array to the edges

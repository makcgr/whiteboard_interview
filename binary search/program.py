def binarySearch(nums: list[int], target: int) -> int:
    l, r = 0, len(nums)-1
    while l <= r:
        i = l + (r - l) // 2
        if nums[i] == target:
            return i
        elif nums[i] < target:
            l = i + 1
        else: # nums[i] > target:
            r = i - 1
    return -1

print(binarySearch([-1,0,3,5,9,12], 9))
print(binarySearch([-1,0,3,5,9,12], 2))

# why it works
# - since input array is sorted:
#    - we start with start index (0) and end index of array (len(nums) - 1)
#    - while l <= r: 
#            (NOTE: <= is important, think of an array where there is a single element [ 1 ]
#             if we had l < r: here, the cycle body would never execute (wrong)
#    - dividing by 2 (l + (r-l)), we get a "middle index" which is located roughly in the mid of arr
#    - if value at this index
#           - is our target: we return this index (SUCCESS)
#           - is less than our target: i does not fit,  we search on the RIGHT of this index: l = i+1 
#           - is greater than our target: i does not fit, we search on the LEFT of this index: r = i-1
# return -1 if not found until now


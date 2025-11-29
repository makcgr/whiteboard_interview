def fourSum(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    quad, res = [], []
    rSet = set() 

    def kSum(k: int, start: int, target: int):
        if k != 2:
            for i in range(len(nums) - k + 1):
                if i > start and nums[i-1] == nums[i]:
                    continue
                quad.append(nums[i])
                kSum(k - 1, i + 1, target - nums[i])
                quad.pop()
        else:
            # base two-sum
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    arr = quad + [nums[l],  nums[r]]
                    arr.sort()
                    if tuple(arr) not in rSet:
                        res.append(arr)
                        rSet.add(tuple(arr))
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
    kSum(4, 0, target)
    return res


res = fourSum([3,2,3,-3,1,0], 3)
for arr in res:
    print(arr)

# why this works:
# we simulate for cycles in kSum recursive methods
#   NOTE: first we APPEND the current num to build the quad list
#         then we call recursive func with (k - 1, i + 1, updated target)i
#         finally we CLEAN UP after the call with POP (since we have other iterations of for cycleto go after it)
#   once we end up with 2sum, it's base case (2 pointers)
# do not forget to 
#   1) SORT the input array (otherwise it won' work)
#   2) handle the same values (skip them)



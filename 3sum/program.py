class Solution(object):
  def threeSum(self, nums):
    nums.sort()
    LEN = len(nums)
    res = []
    for a in range(LEN):
        if a > 0 and nums[a] == nums[a-1]:
            continue
        
        l, r = a + 1, LEN - 1
        while l < r:
            sum = nums[a] + nums[l] + nums[r]
            if sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            elif sum == 0:
                res.append([nums[a], nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
    return res

# Test Program
nums = [1, -2, -2, 1, 0,  0, 5, 1]
print(Solution().threeSum(nums))
# [[-2, 1, 1]]

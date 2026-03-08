# Solution:
# We use backtracking with recursive function
# On each step we check if the i hits the length of array
#   If yes: stop processing and return total
#   If no:
#       we add two variants to the total XOR sum:
#           - total XORed with current element  
#           - and total with skipped current element
#   NOTE: what defines each subset: we either INCLUDE the current element or NOT
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, total):
            if i == len(nums):
                return total
            return dfs(i+1, total ^ nums[i]) + dfs(i+1, total)
        return dfs(0, 0)

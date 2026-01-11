class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack(path)
                path.pop()

        backtrack([])
        return result

# why it works. let's imagine we have input [1, 2, 3]
# path is our dynamic "backtracking path". 
# calling backtrack([]) we go like this:
#   from [] 
#   -> [1] -> [1,2] -> [1,2,3]* -> [1,2] -> [1] -> [1,3] -> [1,3,2]* -> [1,3] -> [1] -> [] ->
#   -> [2] -> [2,1] -> [2,1,3]* -> [2,1] -> [2] -> [2,3] -> [2,3,1]* -> [2,3] -> [2] -> [] -> 
#   -> [3] -> [3,1] -> [3,1,2]* -> [3,1] -> [3] -> [3,2] -> [3,2,1]* -> [3,2] -> [3] -> [] 

# backtracking approach = always 4 steps in the backtrack() func:
# 1. base case. our: len(path) == len(nums), add copy of path to result arr
# 2. choice constraints. our: any num in nums, except the ones already in path
# 3. make choice. our: append num to path
#    -- call backtrack() function here
# 4. undo choice. our: pop num from path

print(Solution().permute([1, 2, 3]))

'''
    Explanation

    We have a decision tree here
    We dive into a Depth First Search exploring the tree,
    starting with first element of input set (i=0)
    On each step/iteration we have 2 viable decisions:
    - to include current element nums[i] into a subset
    - to not include current element into a subset
    Each decision passes its own variant further into a DFS func

    E.g. Input = [1,2,3]
                  ^
                  i=0

    ... process the decisions recursively starting from first node,
        forming the subsets and overall result array
        (see decision tree below)

    IMPORTANT:
        We add the subset to result only when the i exceeds len(nums)
        (when we know we reached the farthest leaf of the tree)
'''

#    DECISION TREE
#    LEGEND: ti=to include ni=to not include
#i=0               1
#         ti   /       \ ni
#          [1]             []
#i=1        2               2
#      ti /   \ ni     ti /   \ ni
#       [1,2] [1]      [2]      [] 
#i=2   3        3       3         3 
#   ti/ \ni  ti/ \ni ti/ \ni   ti/ \ni    
#[1,2,3][1,2][1,3][1][2,3][3] [3]   []   <-- HERE WE ADD TO RESULT
#

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # decision 1. INCLUDE the node value
            subset.append(nums[i])
            dfs(i+1)

            # decision 2. NOT INCLUDE the node value
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res

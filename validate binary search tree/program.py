from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node: return True
            
            return (
                dfs(node.left) 
                and dfs(node.right)
                and (node.left is None or node.left.val < node.val)
                and (node.right is None or node.right.val > node.val))
        
        return dfs(root)

'''
  2
 / \
1   3

  1
 / \
2   3
'''

root = TreeNode(2, TreeNode(1), TreeNode(3))
print(Solution().isValidBST(root))

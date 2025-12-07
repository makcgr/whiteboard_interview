class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetricTree(root):
    def dfs(left, right):
        if left is None and right is None:
            return True
        if not left or not right:
            return False
        return (left.val == right.val 
                and dfs(left.right, right.left)
                and dfs(right.right, left.left))

    return dfs(root.left, root.right)

root = Node(1, Node(2,Node(3), Node(4)), Node(2,Node(4),Node(3)))
print(isSymmetricTree(root))

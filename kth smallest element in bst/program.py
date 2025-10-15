class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kThSmallest(root, k):
    cnt = 0
    val = None 
    def dfs(node):
        nonlocal cnt, val
        if not node:
            return
        dfs(node.left)
        cnt += 1
        if cnt == k:
            val = node.val
            return
        dfs(node.right)

    dfs(root)
    return val

root = Node(4)
root.left = Node(3, Node(2), None)
root.right = Node(5)

print(kThSmallest(root,4))

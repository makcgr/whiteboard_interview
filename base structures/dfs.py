class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive in-order
def dfs(node):
    if not node:
        return
    dfs(node.left)
    print(node.val, end=' ')
    dfs(node.right)

# iterative pre-order
def dfsIter(root):
    stack = [ root ]
    while stack:
        cur = stack.pop()
        if not cur:
            continue
        stack.append(cur.right)
        print(cur.val, end=' ')
        stack.append(cur.left)

# iiterative in-order 
def dfsIterInOrder(root):
    stack = []
    cur = root
    while stack or cur:
        # phase 1. go the most left
        while cur:
            stack.append(cur)
            cur = cur.left
        # phase 2. pop and process node
        cur = stack.pop()
        print(cur.val, end=' ')
        cur = cur.right


root = Node(4)
root.left = Node(2,Node(1), Node(3))
root.right = Node(6, Node(5), Node(7))
dfs(root)
print("\n")
dfsIter(root)
print("\n")
dfsIterInOrder(root)
print("\n")


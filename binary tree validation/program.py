from collections import deque

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


# Why this works
#   - For each node we pass the low and high restriction for value
#   - We update the restriction for each child node accordingly
def validate_bst(root):
    queue = deque([( root, float('-inf'), float('inf'))])
    while len(queue) > 0:
        (node, low, high) = queue.popleft()
        if not node:
            continue
        if not (low < node.value < high):
            return False
        queue.append((node.left, low, node.value))
        queue.append((node.right, node.value, high))
    return True


node = Node(5)
node.left = Node(1)
node.right = Node(4)
node.right.left = Node(3)
node.right.right = Node(6)
print(validate_bst(node))

node = Node(2)
node.left = Node(1)
node.right = Node(3)
print(validate_bst(node))

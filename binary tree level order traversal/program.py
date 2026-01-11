from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def level_order(root):
    q = deque([root])
    result = []
    while q:
        qLen = len(q)
        node = q.popleft()
        if node:
           result.append(node.value)
           q.append(node.left)
           q.append(node.right)
    return result

node = Node(9)
node.left = Node(7, Node(5), Node(10))
node.right = Node(20, Node(15), Node(22))
print(level_order(node))

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
        level = []
        qLen = len(q)
        for _ in range(qLen):
            node = q.popleft()
            if node:
                level.append(node.value)
                q.append(node.left)
                q.append(node.right)
        if level:
            result.append(level)
    return result

node = Node(9)
node.left = Node(7)
node.right = Node(20, Node(15), Node(22))
print(level_order(node))

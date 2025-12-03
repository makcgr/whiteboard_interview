from collections import deque

# 1. define Node class
# 2. define bfs function (accepting root Node parameter)
# 3. In bfs(root):
#    define queue (FIFO storage) 
#    define visited dictionary (hash set)
#    define result accumulating variable 
#    
#    add root node to queue
#    while queue contains elements:
#       pop node from queue
#        process element
#        if node has children:
#            add all children to queue

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def bfs(root):
    queue = [ root ]
    visited = set()
    res = 0
    while len(queue) > 0:
        node = queue.pop()
        if node not in visited: 
            res += node.value
            visited.add(node)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(5)
res = bfs(root)
print(res)

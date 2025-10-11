class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#      8
#    /  \
#   5    10
#  / \   / \
# 4   7 9  13

def searchBST(node, val):
    if node is None:
        return False

    if node.val == val:
        return True
    elif node.val < val:
        return searchBST(node.right, val)
    elif node.val > val:
        return searchBST(node.left, val)


root = Node(7, Node(5, Node(4), Node(7)), Node (10, Node(9), Node(13)))
for val in [5, 9, 15]:
    print(searchBST(root, val))



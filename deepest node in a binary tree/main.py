# You are given the root of a binary tree. Return the deepest node (the furthest node from the root).
#
# Example:
#     a
#    / \
#   b   c
#  /
# d
#
# The deepest node in this tree is d at depth 3.


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return self.val

class NodeDepth(object):
    def __init__(self, node, depth):
        self.node = node
        self.depth = depth

def getDepth(node, cur_depth):
    if node is None or cur_depth < 0:
        return NodeDepth(None, -1)

    cur_depth+=1

    curND = None if node.left is not None and node.right is not None else NodeDepth(node, cur_depth)

    leftND = getDepth(node.left, cur_depth) if node.left is not None else curND
    rightND = getDepth(node.right, cur_depth) if node.right is not None else curND
    return leftND if leftND.depth > rightND.depth else rightND

def getDeepestNode(node):
    # 1. We will use recursion to pass current depth into children
    # 2. Separate method will be used for recursion, returning depth of node
    # 3. Recursive method will be called for each non-null Node
    # 4. Each time recursive method is called, the depth parameter is increased
    # 5. If there are left or right nodes, the depth parameter will be defined,
    #    based on for which node the biggest depth was returned.
    # 6. We need not only to pass upstairs the biggest depth, but also the node name.
    #    Better to return the Node itself.
    return getDepth(node, 0)

myNode1 = Node("a")

myNode1.left = Node("b")
myNode1.left.left = Node("d")

myNode1.right = Node("c")

res = getDeepestNode(myNode1)
print("The deepest node is %s with depth %s" % (res.node, res.depth) )

# self-test
# 1) None OK
# 2) Actual case
# (current depth)
#    a (1)
#    a.left (2)
#    a.left.left (3)
#    a.right (2)
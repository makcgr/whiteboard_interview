class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return self.val


class Solution:
    def EvaluateExpression(self, root):
        return Solution().EvaluateNodeRecursive(root)

    def IsOperationSymbol(self, val):
        if val == '*' or val == '/' or val == '+' or val == '-' : 
            return True
        elif not isinstance(val, int):
            raise ValueError("Wrong value %s: only operations and integers are supported as value" % val)
        return False

    def EvaluateNodeRecursive(self, node):
        if Solution().IsOperationSymbol(node.val):
            leftVal = Solution().EvaluateNodeRecursive(node.left)
            rightVal = Solution().EvaluateNodeRecursive(node.right)
            if node.val == '*':
                return leftVal * rightVal
            elif node.val == '/':
                return leftVal / rightVal
            elif node.val == '+':
                return leftVal + rightVal
            elif node.val == '-':
                return leftVal - rightVal
            else:
                raise ValueError("Not known operation...")
        else:
            return node.val

root = Node('*')
root.left = Node('+')
root.left.left = Node(3.0)
root.left.right = Node(2)
root.right = Node('+')
root.right.left = Node(4)
root.right.right = Node(5)

result = Solution().EvaluateExpression(root)
print(result)

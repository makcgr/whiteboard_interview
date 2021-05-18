# Reverse the given linked list.
# E.g. of values (1) -> (3) -> (5)

class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class MySolution:
    def printLL(self, the_list):
        while(the_list is not None):
            print(f"{the_list.val} ", end="")
            the_list = the_list.next
        print("")


    def reverseLL(self, the_list):
        # TODO: reverse the linked list
        print("Will reverse the linked list:")
        self.printLL(the_list)
        cur_node = the_list
        rev_list = None
        rev_stack = []

        while cur_node is not None:
            rev_stack.append(cur_node)
            cur_node = cur_node.next

        cur_node = rev_stack.pop() if len(rev_stack) != 0 else None
        rev_list = cur_node
        while cur_node is not None:       
            node_next = rev_stack.pop() if len(rev_stack) != 0 else None
            cur_node.next = node_next
            cur_node = node_next

        print("Reversed list:")
        self.printLL(rev_list)


list = Node(1)
list.next = Node(3)
list.next.next = Node(5)

MySolution().reverseLL(list)

# Spatial complexity will be O(N*2), basically O(N)
# Time complexity will be O(N) also

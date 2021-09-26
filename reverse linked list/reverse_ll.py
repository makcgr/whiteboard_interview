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
        cur_node_prev = None

        while cur_node is not None:
            next = cur_node.next
            cur_node.next = cur_node_prev
            cur_node_prev = cur_node
            cur_node = next

        print("Reversed list:")
        self.printLL(cur_node_prev)


list = Node(1)
list.next = Node(3)
list.next.next = Node(5)

MySolution().reverseLL(list)

# Spatial complexity will be O(N)
# Time complexity will be O(N) also

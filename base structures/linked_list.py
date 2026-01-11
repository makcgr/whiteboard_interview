class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

#   None  a->b->c->d->
#   |     |
#   prev  cur

# why it works: 
#   cur and prev, this is the node
#   - temp to store the next
#   - reverse cur 
#   - update prev (to cur)
#   - update cur  (to saved next)

def reverse(head): 
    cur = head
    prev = None
    while cur is not None:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

def reverseRec(head):
    if not head:
        return None
    def reverseRecHelper(prev, node):
        next = node.next
        if not next:
            return node
        node.next = prev
        return reverseRecHelper(node, next)

    return reverseRecHelper(None, head)


def print_list(node):
    while node is not None:
        print(node.value, "->", end="")
        node = node.next
    print()


node = Node(1)
node2 = node.next = Node(2)
node3 = node.next.next = Node(3)
print_list(node)
reverse(node)
print_list(node3)


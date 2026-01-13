class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
#   p1 -> a(1) -> b(3) -> c(5) ->
#   p2 -> d(2) -> e(4)
# dummy -> a(1)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next 

        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next

def printList(head: ListNode):
    while head is not None:
        print(head.val, end=' ')
        head = head.next
    print()

l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4))

res = Solution().mergeTwoLists(l1, l2)
printList(res)


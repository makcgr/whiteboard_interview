class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None
                res = self.mergeTwoLists(l1, l2)
                mergedLists.append(res)
            lists = mergedLists
        return lists[0]

    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        dummy = ListNode()
        cur = dummy
        while l1 is not None  and l2 is not None:
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
l2 = ListNode(2, ListNode(6))
l3 = ListNode(4, ListNode(7, ListNode(7)))

res = Solution().mergeKLists([l1, l2, l3])
printList(res)

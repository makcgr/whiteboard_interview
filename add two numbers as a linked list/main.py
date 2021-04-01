# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        print(f"Will add two numbers {l1.val} and {l2.val}. Capacitor var is {c}")
        sum = l1.val + l2.val + c
        if sum >= 10:
            l1.val = sum % 10
            c = 1
        else:
            l1.val = sum
            c = 0

        if l1.next or l2.next or c == 1:
            if l1.next is None:
                l1.next = ListNode(0)
            if l2.next is None:
                l2.next = ListNode(0)
            self.addTwoNumbers(l1.next, l2.next, c)

            return l1

        lr = ListNode(0)
        lr.next = ListNode(0)
        lr.next.next = ListNode(0)
        return lr
    # Fill this in.


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val, end="")
    result = result.next
    # Should be: 708

print("\n")

l1 = ListNode(8)
l1.next = ListNode(7)
l1.next.next = ListNode(6)

l2 = ListNode(9)
l2.next = ListNode(8)
l2.next.next = ListNode(7)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val, end="")
    result = result.next
    # Should be: 7641

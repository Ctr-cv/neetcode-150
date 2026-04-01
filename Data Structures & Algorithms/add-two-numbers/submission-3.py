# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        add = 0
        cur1, cur2 = l1, l2
        prev = None
        while cur1 and cur2:
            sum = cur1.val + cur2.val + add
            add = 0
            if sum >= 10:
                add = 1
                sum %= 10
            cur1.val = sum
            prev = cur1
            cur1 = cur1.next
            cur2 = cur2.next
        while cur1:
            cur1.val += add
            if cur1.val < 10:
                add = 0
                break
            cur1.val %= 10
            prev = cur1
            cur1 = cur1.next
        if cur2: prev.next = cur2
        while cur2:
            cur2.val += add
            if cur2.val + add < 10:
                add = 0
                break
            cur2.val %= 10
            prev = cur2
            cur2 = cur2.next

        if add == 1:
            prev.next = ListNode(1, None)
        return l1
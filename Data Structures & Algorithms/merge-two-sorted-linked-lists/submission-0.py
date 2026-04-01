# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = list1, list2
        if cur1 is None: return cur2
        if cur2 is None: return cur1
        if cur1.val <= cur2.val:
            head = cur1
            cur1 = cur1.next
        else:
            head = cur2
            cur2 = cur2.next
        result = head
        while cur1 is not None and cur2 is not None:
            if cur1.val <= cur2.val:
                head.next = cur1
                cur1 = cur1.next
                head = head.next
            else:
                head.next = cur2
                cur2 = cur2.next
                head = head.next
        if cur1 is not None:
            head.next = cur1
        else:
            head.next = cur2

        return result
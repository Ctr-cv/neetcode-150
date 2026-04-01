# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None
        cur = head
        if head: nextNode = head.next
        while cur is not None:
            cur.next = dummy
            dummy = cur
            cur = nextNode
            if nextNode is not None:
                nextNode = nextNode.next
        return dummy
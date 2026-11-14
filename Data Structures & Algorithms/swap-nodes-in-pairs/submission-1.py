# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        prev, front = None, head
        while front is not None:
            back = front.next
            if back is None: return head
            last = back.next

            if prev: prev.next = back
            back.next = front
            if front == head: head = back
            front.next = last

            prev = front
            front = last
        return head

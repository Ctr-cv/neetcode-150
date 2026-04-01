# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        front, back = head, head
        for i in range(n - 1):
            front = front.next
        prev = None
        while front.next:
            prev = back
            back = back.next
            front = front.next
        tmp = back.next
        if not prev and front == back: return None
        if not prev: return tmp
        prev.next = tmp
        return head
        

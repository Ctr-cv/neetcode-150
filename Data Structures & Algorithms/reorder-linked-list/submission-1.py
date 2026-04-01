# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid, fast = head, head
        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next
        # head, __, ..., mid, ..., end
        if not mid.next:
            return None
        prev = mid  # prev, mid, tmp, .....
        cur = mid.next  # mid, prev, tmp ....
        mid.next = None
        while cur:  # mid, tmp, ...
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        # head, __, ..., mid, __, ..., prev, after mid has been reversed
        cur = head
        while cur != prev and cur.next != prev:
            nxt_cur = cur.next
            nxt_prev = prev.next
            cur.next = prev
            prev.next = nxt_cur
            cur = nxt_cur
            prev = nxt_prev
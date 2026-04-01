# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # use slow, back, ..., front, fast, where there are k notes in between back and front inclusive
    # 1. Initialize the nodes in necessary position. If front is null return
    # 2. Begin reverse starting with back in a loop.
    # 2.0 Initially: slow = null, back = head, front = head->next (ktimes + while !null), fast = front->next
    # If front is ever null, return
    # 2.1 Condition: while front != null. init prev = fast.
    # 2.1.1 Inner loop cond: while itr < k:
    # 2.1.2 Iterate: nxt = back->next; back->next = prev; prev = back; back = nxt; itr += 1
    # 2.2. After finishing inner loop, should look like this: slow, (disconnected) front, ..., back, (dc), fast
    # 2.3. slow->next = front, back->next = fast. Then, revert with slow = back, back = front = fast = back->next

        slow = None
        back, front, fast = head, head, head
        first = True
        while front:
            # 2.0
            for i in range(k - 1):
                front = front.next
                if not front: return head
            fast = front.next
            # 2.1
            front = back  # front after changes will be the new back
            prev = fast
            for i in range(k - 1):
                nxt = back.next
                back.next = prev
                prev = back
                back = nxt
            back.next = prev
            if first:
                head = back
                first = False
            else:
                slow.next = back
            front.next = fast
            slow = front
            back, front = fast, fast
        return head

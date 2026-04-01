# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import itertools

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        hp = []
        counter = itertools.count()
        for l in lists:
            if not l: continue
            hp.append((l.val, next(counter), l))
        heapq.heapify(hp)
        head, cur = None, None
        while len(hp) != 0:
            value, _, node = heapq.heappop(hp)
            if not head:
                head = node
                cur = node
            else:
                cur.next = node
                cur = node
            add = node.next
            if add:
                heapq.heappush(hp, (add.val, next(counter), add))
        return head

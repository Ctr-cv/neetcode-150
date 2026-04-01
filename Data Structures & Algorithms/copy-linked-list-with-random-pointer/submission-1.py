"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original = {}
        cur, idx = head, 0
        if not head: return None
        while cur:
            original[cur] = idx
            idx += 1
            cur = cur.next
        match = [-1] * idx      # list to track random matches. 0 -> 3 means 3 stored in 0.
        for node, i in original.items():
            if node.random:
                match[i] = original[node.random]
            else:
                match[i] = -1
        cur = head
        prev = None
        new_list = [] * idx
        while cur:
            new_node = Node(cur.val, cur.next)
            new_list.append(new_node)
            if prev is not None: prev.next = new_node
            prev = new_node
            cur = cur.next
        for i in range(len(match)):
            if match[i] != -1:
                new_list[i].random = new_list[match[i]]
            else: new_list[i].random = None
        return new_list[0]



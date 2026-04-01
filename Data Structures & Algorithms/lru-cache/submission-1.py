class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dt = {} # Map key to Node
        
        # Initialize Dummy Nodes
        self.head = ListNode()
        self.tail = ListNode()
        
        # Connect them to each other
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dt:
            node = self.dt[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dt:
            self._remove(self.dt[key])
        
        new_node = ListNode(key, value)
        self._add(new_node)
        self.dt[key] = new_node
        
        if len(self.dt) > self.capacity:
            # The LRU node is the one right before the dummy tail
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.dt[lru_node.key]

    # --- Helper Methods ---
    
    def _add(self, node):
        """Always adds the node right after the dummy head (MRU position)."""
        after_head = self.head.next
        
        node.next = after_head
        node.prev = self.head
        
        self.head.next = node
        after_head.prev = node

    def _remove(self, node):
        """Removes a node from the linked list by connecting its neighbors."""
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node

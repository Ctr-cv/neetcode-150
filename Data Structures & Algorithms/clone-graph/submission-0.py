"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None: return None
        def dfs(node: Optional['Node'], created: dict):
            if node in created: return created[node]
            newNode = Node(node.val)
            created[node] = newNode
            for neighbor in node.neighbors:
                newNode.neighbors.append(dfs(neighbor, created))
            return newNode
        return dfs(node, {})
            
            
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
    
        def find(x):
            if x == parent[x]:
                return x
            else: 
                return find(parent[x])

        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return False
            parent[py] = px
            return True

        for u, v in edges:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v

        for u, v in edges:
            if not union(u, v):
                return [u, v]
            

            
        
        
        
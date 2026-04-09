class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Kruskal's using DSU
        parent = list(range(len(points)))
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False

        # Initialize edges
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        edges.sort()
        # Run Kruskal
        ans, num_edges = 0, 0
        for weight, i, j in edges:
            if union(i, j):
                ans += weight
                num_edges += 1
            if num_edges == len(points) - 1:
                break
        return ans

        


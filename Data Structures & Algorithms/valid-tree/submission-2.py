class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = {}
        graph = {i: [] for i in range(n)}
        for i in range(len(edges)):
            node1, node2 = edges[i][0], edges[i][1]
            graph[node1].append(node2), graph[node2].append(node1)

        def dfs(node, parent, visited):
            if node in visited: return False
            visited[node] = 1
            for neighbor in graph[node]:
                if neighbor == parent: continue
                if not dfs(neighbor, node, visited): return False
            return True

        if not dfs(0, -1, visited): return False
        if len(visited) != n: return False
        return True

            
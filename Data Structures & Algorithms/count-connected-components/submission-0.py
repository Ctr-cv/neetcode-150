class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for [n1, n2] in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        visited = {}
        def dfs(node):
            if node in visited: return
            visited[node] = 1
            for neighbor in graph[node]:
                dfs(neighbor)
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count
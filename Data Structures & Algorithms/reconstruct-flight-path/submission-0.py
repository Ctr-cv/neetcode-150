class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        steps = len(tickets)
        graph = {}
        for [source, dest] in tickets:
            if source not in graph: graph[source] = []
            graph[source].append(dest)
        for k, v in graph.items():
            v.sort() # Lexicographically smallest
        
        node = "JFK"
        ans = ["JFK"]
        def dfs(node):
            if len(ans) == steps + 1: return ans
            if node not in graph: return None
            for i, neighbor in enumerate(graph[node][:]):
                neighbor = graph[node][i]
                ans.append(neighbor)
                graph[node].pop(i)

                res = dfs(neighbor)
                if res is not None: return res
                graph[node].insert(i, neighbor)
                ans.pop()
            return None

        return dfs(node)
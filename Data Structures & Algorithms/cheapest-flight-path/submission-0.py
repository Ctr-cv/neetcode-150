class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        node = [100000001] * n
        node[src] = 0
        k += 1
        for i in range(k):
            tmp = list(node)
            for i in range(len(flights)):
                u, v, wt = flights[i]
                if node[u] + wt < tmp[v]:
                    tmp[v] = node[u] + wt
            node = tmp
        if node[dst] != 100000001:
            return node[dst]
        return -1
                
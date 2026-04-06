class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for ui, vi, ti in times:
            if ui not in graph: graph[ui] = []
            graph[ui].append((ti, vi))

        pq = [(0, k)]
        result = [float('inf')] * (n+1)
        while len(pq) > 0:
            ti, ui = heapq.heappop(pq)
            if ti >= result[ui]: continue
            result[ui] = ti
            if ui in graph:
                for t, v in graph[ui]:
                    heapq.heappush(pq, (t + ti, v))
        ans = -1
        for i in range(1, len(result)):
            if ans < result[i]: ans = result[i]
        if ans == float('inf'): return -1
        return int(ans)

            
        

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q, hp = deque([(".", 0)] * n), []
        dt = {}
        for t in tasks:
            dt[t] = dt.get(t, 0) + 1
        for key, val in dt.items():
            hp.append((-val, key))
        heapq.heapify(hp)
        count = 0
        while hp or any(freq != 0 for _, freq in q):
            if len(hp) > 0:
                freq, task = heapq.heappop(hp)
                freq = -freq - 1    # execute task
            else:
                freq, task = 0, "."

            timeout_task, timeout_freq = q.pop()
            if timeout_freq != 0:
                heapq.heappush(hp, (-timeout_freq, timeout_task))

            q.appendleft((task, freq))
            count += 1
        return count
        
            

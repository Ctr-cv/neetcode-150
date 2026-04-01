class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for i, num in enumerate(stones):
            heapq.heappush(pq, -num)
        while len(pq) > 1:
            stone1 = -heapq.heappop(pq)
            stone2 = -heapq.heappop(pq)
            if stone1 > stone2:
                heapq.heappush(pq, -(stone1-stone2))
            elif stone2 > stone1:
                heapq.heappush(pq, -(stone2-stone1))
        if len(pq) == 0: return 0
        return -pq[0]
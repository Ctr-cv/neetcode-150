class KthLargest:
    pq = []
    k = 0
    def __init__(self, k: int, nums: List[int]):
        copy = 0
        self.pq = []
        self.k = k
        for i, num in enumerate(nums):
            heapq.heappush(self.pq, num)
            copy += 1
            if copy > k:
                heapq.heappop(self.pq)

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)
        if len(self.pq) > self.k: heapq.heappop(self.pq)
        return self.pq[0]
        

class MedianFinder:

    def __init__(self):
        self.front = []
        self.back = []
        self.front_size, self.back_size = 0, 0

    def addNum(self, num: int) -> None:
        f = -self.front[0] if self.front else float('-inf')
        b = self.back[0] if self.back else float('inf')
        if f < num:     # Go into self.back
            heapq.heappush(self.back, num)
            self.back_size += 1
            while self.back_size - self.front_size >= 2:
                item = heapq.heappop(self.back)
                heapq.heappush(self.front, -item)
                self.back_size -= 1
                self.front_size += 1
        else:
            heapq.heappush(self.front, -num)
            self.front_size += 1
            while self.front_size - self.back_size >= 2:
                item = heapq.heappop(self.front)
                heapq.heappush(self.back, -item)
                self.back_size += 1
                self.front_size -= 1

    def findMedian(self) -> float:
        if self.front_size == self.back_size:
            f, b = -self.front[0], self.back[0]
            result = (f + b) / 2        
            return result
        else:
            return -self.front[0] if self.front_size > self.back_size else self.back[0]
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for i in range(len(points)):
            distance = math.sqrt(points[i][0] ** 2 + points[i][1] ** 2)
            heapq.heappush(dist, (distance, points[i][0], points[i][1]))
        result = []
        for i in range(k):
            d, x, y = heapq.heappop(dist)
            result.append([x, y])
        return result
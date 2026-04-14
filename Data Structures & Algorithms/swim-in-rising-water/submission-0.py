class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Track the minimum "max-height" seen so far for each cell
        weights = [[float('inf')] * n for _ in range(n)]
        pq = [(grid[0][0], 0, 0)]
        while pq:
            height, i, j = heapq.heappop(pq)
            # Check neighbors
            if i == len(grid) - 1 and j == len(grid[0]) - 1: return height
            if height > weights[i][j]: continue
            for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(grid) and 0 <= newj < len(grid[0]):
                    bottleneck = max(height, grid[newi][newj])
                    if bottleneck < weights[newi][newj]:
                        weights[newi][newj] = bottleneck
                        heapq.heappush(pq, (bottleneck, newi, newj))

        return -1


                
                

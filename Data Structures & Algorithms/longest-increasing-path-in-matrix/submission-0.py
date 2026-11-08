class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        longest_path = -1
        dp = [[0] * m for _ in range(n)]
        def iter(i, j):
            ans = 1
            if dp[i][j] != 0: return dp[i][j]
            for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                x, y = i + di, j + dj
                if x < 0 or x >= n or y < 0 or y >= m: continue
                if matrix[x][y] <= matrix[i][j]: continue
                ans = max(iter(x, y) + 1, ans)
            dp[i][j] = ans
            return ans
                
        for i in range(n):
            for j in range(m):  
                longest_path = max(iter(i, j), longest_path)
        return longest_path
                   
        
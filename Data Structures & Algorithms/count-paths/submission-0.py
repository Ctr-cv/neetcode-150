class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: dp[i][j] = 1
                elif i == 0: dp[0][j] = dp[0][j-1]
                elif j == 0: dp[i][0] = dp[i-1][0]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
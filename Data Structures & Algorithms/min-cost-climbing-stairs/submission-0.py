class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        elif len(cost) == 2:
            return min(cost[0], cost[1])
        dp = [0, 0]
        for i in range(2, len(cost)+1):
            dp.append(min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]))
        return dp[len(cost)]



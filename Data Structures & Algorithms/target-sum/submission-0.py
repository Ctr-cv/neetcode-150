class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if total < target: return 0
        if (total + target) % 2 != 0 or total + target < 0: return 0
        subset_target = (total + target) // 2 
        dp = [0] * (subset_target + 1)
        dp[0] = 1
        for num in nums:
            for j in range(subset_target, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[-1]


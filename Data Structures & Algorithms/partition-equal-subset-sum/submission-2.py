class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2: return False
        goal = total_sum // 2

        dp = [False] * (goal + 1)
        dp[0] = True

        for i in range(len(nums)):
            for j in range(goal, nums[i] - 1, -1):
                if dp[j - nums[i]]: dp[j] = True

        return dp[goal]



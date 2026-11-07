class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        dp = [float('inf')] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            jump = nums[i]
            dist = i
            while dist < len(nums) and dist <= i + jump:
                dp[dist] = min(dp[dist], dp[i] + 1)
                dist += 1
        return dp[-1]


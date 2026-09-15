class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        ans = 0
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            j = i - 1
            prior = 0 # max dp value for entries that are SMALLER than nums[i]
            while j >= 0:
                if nums[j] < nums[i]: prior = max(prior, dp[j])
                j = j - 1
            dp[i] = prior + 1
            ans = max(ans, dp[i])
        return ans
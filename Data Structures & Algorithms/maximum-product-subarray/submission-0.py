class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 0: max, 1: min
        dp = [[0, 0] for _ in range(len(nums))]
        dp[0] = [nums[0], nums[0]]
        ans = nums[0]

        for i in range(1, len(nums)):
            v1, v2, v3 = nums[i], dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i]
            first = max(v1, v2, v3)
            sec = min(v1, v2, v3)
            dp[i][0] = first
            dp[i][1] = sec
            ans = max(ans, first)

        return ans

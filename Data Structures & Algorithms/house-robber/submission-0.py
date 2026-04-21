class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        ans = [0] * len(nums)
        ans[0], ans[1] = nums[0], max(nums[0], nums[1])
        result = 0
        for i in range(2, len(nums)):
            ans[i] = max(ans[i-2] + nums[i], ans[i-1])
            result = max(result, ans[i])
        return result

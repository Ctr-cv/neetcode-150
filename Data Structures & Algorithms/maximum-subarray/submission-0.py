class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result, running = nums[0], 0
        for i in range(len(nums)):
            running += nums[i]
            if result < running: result = running
            if running < 0: running = 0
        return result
        
        
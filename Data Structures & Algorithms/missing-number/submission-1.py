class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) + 1):
            res ^= i
        for i, num in enumerate(nums):
            res ^= num
        return res
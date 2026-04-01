class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1] * len(nums)
        suffix_prod = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefix_prod[0] = nums[0]
                suffix_prod[len(nums) - 1] = nums[len(nums) - 1]
            else:
                prefix_prod[i] = prefix_prod[i-1] * nums[i]
                suffix_prod[len(nums) - 1 - i] = suffix_prod[len(nums) - i] * nums[len(nums) - 1 - i]
        res = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                res[i] = suffix_prod[i+1]
            elif i == len(nums) - 1:
                res[i] = prefix_prod[i-1]
            else:
                res[i] = prefix_prod[i-1] * suffix_prod[i+1]
        return res
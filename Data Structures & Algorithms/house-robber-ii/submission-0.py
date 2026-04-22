class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = 0
        first = [0] * len(nums)
        notfirst = [0] * len(nums)
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        first[0], notfirst[0] = nums[0], 0
        first[1], notfirst[1] = max(nums[0], nums[1]), nums[1]
        for i in range(2, len(nums)):
            if i != len(nums) - 1:
                first[i] = max(first[i-2] + nums[i], first[i-1])
            else:
                first[i] = first[i-1]
            notfirst[i] = max(notfirst[i-2] + nums[i], notfirst[i-1])
            cur = max(first[i], notfirst[i])
            ans = max(cur, ans)
        return ans
            

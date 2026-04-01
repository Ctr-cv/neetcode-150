class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq, res = {}, 1
        if len(nums) == 0: return 0
        for num in nums:
            seq[num] = False
        for k in seq:
            if k-1 not in seq:
                i = k
                while i in seq: i += 1
                res = max(res, i - k)
        return res
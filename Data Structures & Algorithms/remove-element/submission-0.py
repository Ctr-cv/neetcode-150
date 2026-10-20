class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = len(nums)
        idx = 0
        while idx < i:
            if nums[idx] == val:
                i -= 1
                nums[idx] = nums[i]
            else:
                idx += 1
        return i
            
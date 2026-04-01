class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        nums.sort()
        i = len(nums) - 1
        while i >= 0:
            count = 1
            while i > 0 and nums[i-1] == nums[i]:
                i -= 1
                count += 1
            tmp = list(result)
            for j in range(count):
                for arr in tmp:
                    new_arr = list(arr)
                    for _ in range(j+1):
                        new_arr.append(nums[i])
                    result.append(new_arr)
            i -= 1
        return result
            
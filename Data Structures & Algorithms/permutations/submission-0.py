class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def recur(cur: List[int]):
            if len(nums) == 0:
                result.append(list(cur))
                return
            for i in range(len(nums)):
                num = nums[i]
                cur.append(num)
                nums.pop(i)
                recur(cur)
                cur.remove(num)
                nums.insert(i, num)
        recur([])
        return result
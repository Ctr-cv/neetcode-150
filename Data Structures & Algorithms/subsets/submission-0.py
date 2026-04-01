class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def backtrack(start: int, cur: List[int]):
            result.append(list(cur))
            for i in range(start, len(nums)):
                num = nums[i]
                cur.append(num)
                backtrack(i+1, cur)
                cur.pop()
            return result
        backtrack(0, [])
        return result
                
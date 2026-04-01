class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def recur(start: int, sum: int, cur: List[int]):
            if sum > target or start >= len(nums): return
            if sum == target: 
                result.append(list(cur))
                return
            for i in range(start, len(nums)):
                cur.append(nums[i])
                recur(i, sum + nums[i], cur)
                cur.pop()
        recur(0, 0, [])
        return result
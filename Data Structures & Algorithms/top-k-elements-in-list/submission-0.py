class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        d = {}
        for num in nums:
            d[num] = 1 + d.get(num, 0)
        for key, value in d.items():
            freq[value].append(key)
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = 0
        while l < r:
            k = l + (r - l) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours > h:
                l = k + 1
            else:
                r = k
        return l
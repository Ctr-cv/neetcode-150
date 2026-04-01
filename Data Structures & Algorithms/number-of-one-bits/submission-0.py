class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            res += 0b1 & n
            n >>= 1 
        return res
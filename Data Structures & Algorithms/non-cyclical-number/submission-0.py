class Solution:
    def isHappy(self, n: int) -> bool:
        dit = {}
        while not n in dit:
            if n == 1: return True
            dit[n] = 1
            n = self.getSquareSum(n)
        return False

    def getSquareSum(self, n: int) -> bool:
        res = 0
        while n > 0:
            res += ((n % 10) ** 2)
            n //= 10
        return res

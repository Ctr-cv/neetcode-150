class Solution:
    def countBits(self, n: int) -> List[int]:
        length = 1
        i = 1
        res = [0] * (n+1)
        while i <= n:
            for j in range(length):
                if i > n: break
                res[i] = res[i - length] + 1
                i += 1
            length *= 2
        return res
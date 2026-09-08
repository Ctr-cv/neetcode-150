class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0
        if len(s) == 1: return 1
        res = [0] * len(s)          # of ways to map so far. Start at index 1
        # Check first two index
        num = int(s[:2])
        if num > 26 and num % 10 == 0: return 0
        res[0] = 1
        res[1] = 2
        if num == 10 or num == 20 or num > 26: res[1] = 1

        last = int(s[1])
        #Start at index 3
        for i in range(2, len(s)):
            n = int(s[i])
            num = 10 * last + n
            if (last == 0 or last > 2) and n == 0:
                return 0
            if 10 <= num <= 26:
                if n != 0:
                    res[i] = res[i-2] + res[i-1]
                else:
                    res[i] = res[i-2]
            else:
                res[i] = res[i-1]

            last = n
            

        return res[-1]
            
                
            
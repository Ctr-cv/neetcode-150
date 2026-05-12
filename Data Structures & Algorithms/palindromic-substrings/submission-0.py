class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            # odd
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] != s[r]: break
                l -= 1
                r += 1
                count += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]: break
                l -= 1
                r += 1
                count += 1
            # even
        return count
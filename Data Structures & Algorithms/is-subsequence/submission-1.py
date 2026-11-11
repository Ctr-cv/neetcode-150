class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        for i in range(len(t)):
            if idx == len(s): return True
            if s[idx] == t[i]: idx += 1
        return idx == len(s)
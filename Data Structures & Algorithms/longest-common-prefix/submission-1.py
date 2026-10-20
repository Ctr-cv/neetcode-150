class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        same = True
        i = 0
        while same:
            if i >= len(strs[0]): return ans
            c = strs[0][i]
            for s in strs:
                if i >= len(s) or s[i] != c: return ans
            ans += c
            i += 1
        return ans
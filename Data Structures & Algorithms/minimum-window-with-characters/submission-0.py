class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        ds, dt = {}, {}
        l, r = 0, 0
        ans = None
        for c in t: dt[c] = dt.get(c, 0) + 1
        while r < len(s):
            ds[s[r]] = ds.get(s[r], 0) + 1
            last, valid = "", False
            while all(ds.get(k, 0) >= v for k, v in dt.items()):
                last, valid = s[l], True
                ds[s[l]] -= 1
                if ds[s[l]] == 0: ds.pop(s[l])
                l += 1
            if last != "":
                ds[last] = ds.get(last, 0) + 1
                l -= 1
            if valid and (ans is None or r - l + 1 < len(ans)):
                ans = s[l:r+1]
            r += 1
        if ans: return ans
        else: return ""
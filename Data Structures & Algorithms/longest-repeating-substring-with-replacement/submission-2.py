class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        count = 0
        l, res = 0, 0
        for i, c in enumerate(s):
            mp[c] = mp.get(c, 0) + 1
            count = max(mp[c], count)

            if i - l + 1 - count > k:
                mp[s[l]] -= 1
                l += 1
            res = max(res, i - l + 1)
        return res

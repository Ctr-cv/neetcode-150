class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0
        res = 1
        l = 0
        seen = deque()
        di = set()
        for r in range (len(s)):
            while s[r] in di:
                node = seen.popleft()
                di.remove(node)
                l += 1
            seen.append(s[r])
            di.add(s[r])
            r += 1
            res = max(res, r - l)
        return res
            
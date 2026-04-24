class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            # Check odd
            l, r = i - 1, i + 1
            while l > 0 and r < len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1

            if l < 0 or r >= len(s) or s[l] != s[r]:
                l += 1
                r -= 1
            
            if r - l + 1 > len(result): result = s[l:r+1]
            
            l, r = i, i + 1
            # Check even
            while l > 0 and r < len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1

            if l < 0 or r >= len(s) or s[l] != s[r]:
                l += 1
                r -= 1
            
            if r - l + 1 > len(result): result = s[l:r+1]

        return result
            
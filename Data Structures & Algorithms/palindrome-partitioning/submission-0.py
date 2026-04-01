class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(s: str) -> bool:
            return s == s[::-1]

        def recur(cur: List[str], idx: int):
            if idx == len(s):
                res.append(list(cur))
                return
            for end in range(idx, len(s)):
                sub = s[idx:end + 1]  # next substring
                if isPalindrome(sub):
                    cur.append(sub)
                    recur(cur, end + 1)
                    cur.pop()

        recur([], 0)
        return res
            
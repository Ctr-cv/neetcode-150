class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        arr1, arr2 = [0] * 26, [0] * 26
        for c in s1:
            arr1[ord(c) - 97] += 1
        l, r = 0, 0
        while r < len(s2):
            if r - l == len(s1): 
                arr2[ord(s2[l]) - 97] -= 1
                l += 1
            arr2[ord(s2[r]) - 97] += 1
            r += 1
            if arr1 == arr2: return True
        return False


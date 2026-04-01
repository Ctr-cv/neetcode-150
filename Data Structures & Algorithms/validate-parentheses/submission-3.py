class Solution:
    def isValid(self, s: str) -> bool:
        di = {'(': ')', '{': '}', '[':']'}
        st = []
        if len(s) % 2 != 0: return False
        for i, char in enumerate(s):
            if char in di:
                st.append(char)
            else:
                if len(st) == 0: return False
                match = st.pop()
                if di[match] != char:
                    return False
        if len(st) == 0: return True
        else: return False
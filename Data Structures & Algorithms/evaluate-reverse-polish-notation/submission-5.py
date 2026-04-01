class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t == "+":
                res = st.pop() + st.pop()
                st.append(res)
            elif t == "-":
                res = -st.pop() + st.pop()
                st.append(res)
            elif t == "*":
                res = st.pop() * st.pop()
                st.append(res)
            elif t == "/":
                dividend = st.pop()
                res = st.pop() / dividend
                if res < 0: res = math.ceil(res)
                else: res = math.floor(res)
                st.append(res)
            else:
                st.append(int(t))
        return st[0]

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        lw, rw = [0] * len(heights), [0] * len(heights)
        st = []
        for i, h in enumerate(heights):
            while len(st) != 0 and st[-1][1] > h:
                idx, ht = st.pop()
                rw[idx] = i - idx - 1
            st.append((i, h))
        while len(st) != 0:
            idx, ht = st.pop()
            rw[idx] = len(heights) - idx - 1

        for i in range(len(heights) - 1, -1, -1):
            while len(st) != 0 and st[-1][1] > heights[i]:
                idx, ht = st.pop()
                lw[idx] = idx - i - 1
            st.append((i, heights[i]))
        while len(st) != 0:
            idx, ht = st.pop()
            lw[idx] = idx
        area = 0
        for i in range(len(heights)):
            cur = (lw[i] + rw[i] + 1) * heights[i]
            area = max(cur, area)
        return area

        
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        vert, diag1, diag2 = 0, 0, 0        # n bits integers
        result = []
        def recur(cur: List[str], index: int, vert, diag1, diag2):
            if index == n:
                result.append(list(cur))
                return
            row_mask = vert | diag1 | diag2
            i = 0
            for i in range(n):
                bit = 1 << (n - i - 1)
                if not row_mask & bit:
                    item = "." * i + 'Q' + "." * (n - i - 1)
                    cur.append(item)
                    new_vert = vert | bit
                    new_diag1 = ((diag1 | bit) << 1) & ((1 << n) - 1)
                    new_diag2 = (diag2 | bit) >> 1
                    recur(cur, index + 1, new_vert, new_diag1, new_diag2)
                    cur.pop()
        recur([], 0, 0, 0, 0)
        return result
            
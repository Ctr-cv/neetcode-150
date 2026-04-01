class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def recur(cur: str, idx: int, visited: dict, pos):
            if idx >= len(word):
                if cur == word: return True
                return False
            x, y = pos  # x: column, y: row number
            result = False
            for (dx, dy) in [(-1, 0), (1, 0), (0, 0), (0, -1), (0, 1)]:
                i, j = x + dx, y + dy
                if i < 0 or i >= len(board[0]): continue
                if j < 0 or j >= len(board): continue
                if (i, j) in visited: continue
                if word[idx] == board[j][i]:
                    visited[(i, j)] = 1
                    cur += word[idx]
                    if recur(cur, idx + 1, visited, (i, j)): return True
                    cur = cur[:-1]
                    visited.pop((i, j))
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if recur("", 0, {}, (i, j)): return True
        return False



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x: int, y: int, index: int):
            if index == len(word):
                return True
            if (x < 0 or y < 0 or x >= len(board[0]) or y >= len(board)):
                return False
            if (board[y][x] != word[index]): return False
            tmp = board[y][x]
            board[y][x] = "#"
            result = (dfs(x+1, y, index+1)) or (dfs(x-1, y, index+1)) or (dfs(x, y+1, index+1)) or (dfs(x, y-1, index+1))
            board[y][x] = tmp
            return result

        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(j, i, 0): return True
        return False




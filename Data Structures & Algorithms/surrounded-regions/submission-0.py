class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(i, j, visited):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            if board[i][j] == "X": return True
            if (i, j) in visited: return True
            visited[(i, j)] = 1
            if dfs(i+1, j, visited) and dfs(i-1, j, visited) and dfs(i, j+1, visited) and dfs(i, j-1, visited):
                return True
            else: return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    visited = {}
                    change = "X" if dfs(i, j, visited) else "A"
                    for k, v in visited.items():
                        x, y = k
                        board[x][y] = change

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "A": 
                    board[i][j] = "O"
                

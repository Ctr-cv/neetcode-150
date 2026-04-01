class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkRow(board) and self.checkCol(board) and self.checkBox(board)
    def checkRow(self, board: List[List[str]]):
        for i in range(len(board)):
            seen = {}
            for j in range(len(board[0])):
                if board[i][j] is not "." and board[i][j] in seen:
                    return False
                seen[board[i][j]] = True
        return True
    def checkCol(self, board: List[List[str]]):
        for i in range(len(board[0])):
            seen = {}
            for j in range(len(board)):
                if board[j][i] is not "." and board[j][i] in seen:
                    return False
                seen[board[j][i]] = True
        return True
    def checkBox(self, board: List[List[str]]):
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                seen = {}
                for x in range(3):
                    for y in range(3):
                        if board[i+x][j+y] is not "." and board[i+x][j+y] in seen:
                            return False
                        seen[board[i+x][j+y]] = True
        return True
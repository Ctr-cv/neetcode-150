class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def dfs(i, j, step: int):
            # Expands from treasure-chest to all lands
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]): return
            if grid[i][j] == -1 or grid[i][j] < step: return
            grid[i][j] = step
            dfs(i+1, j, step + 1)
            dfs(i-1, j, step + 1)
            dfs(i, j+1, step + 1)
            dfs(i, j-1, step + 1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    dfs(i, j, 0)
        
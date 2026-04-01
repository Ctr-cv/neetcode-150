class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def dfs(i, j, visited):
            if grid[i][j] == '0' or (i, j) in visited: return

            visited[(i, j)] = 1
            grid[i][j] = "0"

            if i+1 < len(grid):
                dfs(i+1, j, visited)
            if i > 0:
                dfs(i-1, j, visited)
            if j+1 < len(grid[0]):
                dfs(i, j+1, visited)
            if j > 0:
                dfs(i, j-1, visited)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j, {})
        return count
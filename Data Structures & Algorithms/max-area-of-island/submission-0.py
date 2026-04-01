class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = {}
        def dfs(i, j, size):
            if grid[i][j] == 0 or (i, j) in visited: return size
            visited[(i, j)] = 1
            grid[i][j] = 0
            size += 1
            if i+1 < len(grid): size += dfs(i+1, j, 0)
            if i > 0: size += dfs(i-1, j, 0)
            if j+1 < len(grid[0]): size += dfs(i, j+1, 0)
            if j > 0: size += dfs(i, j-1, 0)

            return size

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                size = dfs(i, j, 0)
                result = max(result, size)
        
        return result

        

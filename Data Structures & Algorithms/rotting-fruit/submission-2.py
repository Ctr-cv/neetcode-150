class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = {}
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 or grid[i][j] == 2: fresh += 1

        def dfs(i, j, minute, visited):
            nonlocal fresh
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]): return
            if grid[i][j] == 0: return
            if (i, j) in visited:
                if visited[(i, j)] <= minute: return
            else: fresh -= 1
            visited[(i, j)] = minute

            dfs(i + 1, j, minute + 1, visited)
            dfs(i - 1, j, minute + 1, visited)
            dfs(i, j + 1, minute + 1, visited)
            dfs(i, j - 1, minute + 1, visited)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2: dfs(i, j, 0, visited)

        if fresh > 0:
            return -1
        result = 0
        for k, v in visited.items():
            if v > result: result = v
        return result
            

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visited = {}
        def dfs(i, j, height, visited):
            if i < 0 or i >= len(heights) or j < 0 or j >= len(heights[0]):
                pacific, atlantic = 0, 0 
                if i < 0 or j < 0: pacific = 1
                if i >= len(heights) or j >= len(heights[0]): atlantic = 1
                return [pacific, atlantic]

            if heights[i][j] > height: return [0, 0] # Cannot flow upwards
            if (i, j) in visited: return [0, 0]
            visited[(i, j)] = 1

            t1 = dfs(i+1, j, heights[i][j], visited)
            t2 = dfs(i-1, j, heights[i][j], visited)
            t3 = dfs(i, j+1, heights[i][j], visited)
            t4 = dfs(i, j-1, heights[i][j], visited)
            result = [0, 0]
            if t1[0] or t2[0] or t3[0] or t4[0]: result[0] = 1
            if t1[1] or t2[1] or t3[1] or t4[1]: result[1] = 1
            return result
        ans = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if dfs(i, j, 1001, {}) == [1, 1]:
                    ans.append([i, j])
        return ans
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        neighbors = {i: [] for i in range(numCourses)}
        for pair in prerequisites:
            neighbors[pair[1]].append(pair[0])
        # Use states to track node status
        state = [0] * numCourses
        ans = []

        def dfs(cour):
            if state[cour] == 1: return False
            if state[cour] == 2: return True
            state[cour] = 1
            for nxt in neighbors[cour]:
                if not dfs(nxt):
                    return False
            # No cycle exists in all paths
            state[cour] = 2
            ans.append(cour)
            return True

        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i): return []

        return ans[::-1]
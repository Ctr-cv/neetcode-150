class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        neighbors = {}
        for pair in prerequisites:
            if pair[0] in neighbors:
                neighbors[pair[0]].append(pair[1])
            else:
                neighbors[pair[0]] = [pair[1]]

        # Dict to prevent re-checking the same node
        cycle = {}

        def dfs(cour, path):
            if cour in cycle: return cycle[cour]
            if cour not in neighbors:  # No pre-req
                cycle[cour] = True
                return True
            if cour in path:  # Detected cycle
                cycle[cour] = False
                return False

            path[cour] = 1
            for prereq in neighbors[cour]:
                if not dfs(prereq, path):
                    cycle[cour] = False
                    return False
            cycle[cour] = True
            return True

        for i in range(numCourses):
            if not dfs(i, {}): return False
        return True


            

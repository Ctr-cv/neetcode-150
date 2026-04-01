class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort() # Critical for skipping duplicates

        def recur(index: int, current_sum: int, cur: List[int]):
            # Base case: we found a match
            if current_sum == target:
                result.append(list(cur))
                return
            
            for i in range(index, len(candidates)):
                # Optimization: if the current number is too big, 
                # no need to check further because the list is sorted
                if current_sum + candidates[i] > target:
                    break
                
                # Skip duplicates at the same recursive depth
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                
                cur.append(candidates[i])
                # Move to i + 1 to ensure each element is used only once
                recur(i + 1, current_sum + candidates[i], cur)
                cur.pop() # Backtrack

        recur(0, 0, [])
        return result
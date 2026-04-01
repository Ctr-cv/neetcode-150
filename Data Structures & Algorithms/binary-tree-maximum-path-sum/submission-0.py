# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")

        def dfs(node):
            nonlocal max_sum
            
            if not node:
                return 0
            
            # Get best downward path from children
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            
            # Case 1: path passing through this node (split path)
            current_sum = node.val + left + right
            
            # Update global maximum
            max_sum = max(max_sum, current_sum)
            
            # Case 2: return best downward path to parent
            return node.val + max(left, right)
        
        dfs(root)
        return max_sum

            
            

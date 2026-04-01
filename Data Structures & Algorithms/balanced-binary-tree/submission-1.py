# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        def dfs(root):
            if root is None: return (True, 0)
            leftBalanced, leftHeight = dfs(root.left)
            rightBalanced, rightHeight = dfs(root.right)
            if not leftBalanced or not rightBalanced:
                return (False, -1)
            if abs(leftHeight - rightHeight) > 1:
                return (False, -1)
            return (True, max(leftHeight, rightHeight) + 1)
        res, _ = dfs(root)
        return res
            
            
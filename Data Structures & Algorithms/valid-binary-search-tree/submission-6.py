# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        st = [(root, -1001, 1001)]
        while len(st) != 0:
            node, lower, upper = st.pop()
            if not lower < node.val < upper: return False
            if node.left:
                st.append((node.left, lower, node.val))
            if node.right:
                st.append((node.right, node.val, upper))
        return True
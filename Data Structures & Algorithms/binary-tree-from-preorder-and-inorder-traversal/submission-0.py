# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dt = {}  # Track val -> index of values in inorder
        for i in range(len(inorder)):
            dt[inorder[i]] = i
        l, r = 0, len(inorder) - 1
        preorder_index = 0
        def recurHelper(l: int, r: int) -> Optional[TreeNode]:
            nonlocal preorder_index
            if l > r: return None
            root_val = preorder[preorder_index]
            root = TreeNode(root_val)
            preorder_index += 1
            idx = dt[root_val]
            root.left = recurHelper(l, idx - 1)
            root.right = recurHelper(idx + 1, r)
            return root
        return recurHelper(l, r)





        
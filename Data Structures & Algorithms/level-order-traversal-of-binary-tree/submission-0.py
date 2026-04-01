# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res, st = [], []
        if root: st = [(root, 0)]
        while len(st) != 0:
            node, idx = st.pop()
            if len(res) == idx:
                res.append([])
            res[idx].append(node.val)
            if node.right:
                st.append((node.right, idx + 1))
            if node.left:
                st.append((node.left, idx + 1))
        return res
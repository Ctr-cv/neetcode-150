# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curp, curq, prev = root, root, root
        while curp and curq and curp == curq:
            prev = curp
            if curp.val > p.val: curp = curp.left
            elif curp.val < p.val: curp = curp.right
            else: break

            if curq.val > q.val: curq = curq.left
            elif curq.val < q.val: curq = curq.right
            else: break
        return prev
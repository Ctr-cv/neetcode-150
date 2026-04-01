# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 1
        if not root: return 0
        st = [(root, root.val)]
        while len(st) != 0:
            node, val = st.pop()
            if node.left: 
                if node.left.val >= val: ans += 1
                st.append((node.left, max(node.left.val, val)))
            if node.right:
                if node.right.val >= val: ans += 1
                st.append((node.right, max(node.right.val, val)))
        return ans
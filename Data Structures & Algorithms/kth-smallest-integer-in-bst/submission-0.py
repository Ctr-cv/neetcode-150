# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        cur = root
        st = []
        while cur or st:
            while cur:
                st.append(cur)
                cur = cur.left
            cur = st.pop()
            count += 1
            if count == k: return cur.val
            cur = cur.right
        
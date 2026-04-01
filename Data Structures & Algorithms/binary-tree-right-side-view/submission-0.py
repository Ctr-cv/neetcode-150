# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        result = []
        st = deque()
        st.append((root, 0))
        while len(st) != 0:
            node, lv = st[0]
            while len(st) > 0 and st[0][1] == lv:
                n, l = st.popleft()
                if n.right:
                    st.append((n.right, lv + 1))
                if n.left:
                    st.append((n.left, lv + 1))
            result.append(node.val)
        return result

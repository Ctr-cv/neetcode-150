# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            pNode, qNode = stack.pop()
            if pNode is None and qNode is None:
                continue
            if pNode is None: return False
            if qNode is None: return False

            if pNode.val != qNode.val:
                return False
            stack.append((pNode.left, qNode.left))
            stack.append((pNode.right, qNode.right))

        return True if len(stack) == 0 else False
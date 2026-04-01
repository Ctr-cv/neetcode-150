# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        mp = {None: 0}
        while stack:
            node = stack[-1]
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()
                if self.isSameTree(node, subRoot): return True
                mp[node] = 1
        return False

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



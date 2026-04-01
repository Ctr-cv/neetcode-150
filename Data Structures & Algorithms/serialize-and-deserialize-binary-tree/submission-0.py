# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = ""
        st = [root]
        while len(st) != 0:
            node = st.pop()
            if not node:
                result += "N,"
            else:
                result += str(node.val) + ","
                st.append(node.right)
                st.append(node.left)
        result = result[:-1]
        return result

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data or data[0] == "N": return None
        values = data.split(",")
        idx, res = 1, TreeNode(int(values[0]))
        st = [[res, 0]]
        while idx < len(values):
            info = st[-1]
            node, state = info[0], info[1]
            val = values[idx]
            idx += 1
            if state == 0:
                info[1] = 1
                if val != "N":
                    n = TreeNode(int(val))
                    node.left = n
                    st.append([n, 0])
            elif state == 1:
                st.pop()        # This parent is not needed
                if val != "N":
                    n = TreeNode(int(val))
                    node.right = n
                    st.append([n, 0])
        return res

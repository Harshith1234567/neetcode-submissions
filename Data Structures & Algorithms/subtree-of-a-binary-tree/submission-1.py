# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if node is None:
                res.append("$#")
                return

            res.append("$")
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return "".join(res)

    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        serialized_root = self.serialize(root)

        serialized_subRoot = self.serialize(subRoot)

        return serialized_subRoot in serialized_root
        
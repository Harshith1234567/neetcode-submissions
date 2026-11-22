# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res=[0]

        def dfs(node,prev):
            if not node:
                return

            res[0]=max(res[0],prev+1)
            dfs(node.left, prev+1)
            dfs(node.right,prev+1)
            





        dfs(root,0)
        return res[0]
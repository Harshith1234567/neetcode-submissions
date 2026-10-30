# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preidx=[0]
        inidx=[0]

        def dfs(limit):
            if preidx[0]>=len(preorder):
                return None

            if inorder[inidx[0]]==limit:
                inidx[0]+=1

                return None
            root=TreeNode(preorder[preidx[0]])
            preidx[0]+=1
            root.left=dfs(root.val)
            root.right=dfs(limit)
            return root


        return dfs(float('inf'))
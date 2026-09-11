# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        # if not self.right :
        #     self.left = None
        # else:
        #     self.left = self.invertTree(self.right)

        # if not self.left :
        #     self.right = None
        # else:
        #     self.right = self.invertTree(self.left)

        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        
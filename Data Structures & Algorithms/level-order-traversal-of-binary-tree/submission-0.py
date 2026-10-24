# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        li=deque([root])
        res=[]

        while li:
            t=[]
            length=len(li)
            for i in range(length):
                ele=li.popleft()
                t.append(ele.val)

                if ele.left:
                    li.append(ele.left)

                if ele.right:
                    li.append(ele.right)
            res.append(t)

        return res
            

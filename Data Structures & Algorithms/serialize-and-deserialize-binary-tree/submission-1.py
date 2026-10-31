# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return 'N'

        q=deque([root])

        res=[]

        while q:
            node=q.popleft()
            if not node:
                res.append('N')
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        li=data.split(',')
        if li[0]=="N":
            return None

        
        root=TreeNode(int(li[0]))
        q=deque([root])
        i=1

        while q and i<len(li):
            node=q.popleft()
            if li[i]!="N":
                node.left=TreeNode(int(li[i]))
                q.append(node.left)

            i+=1
            if i<=len(li) and li[i]!="N":
                node.right=TreeNode(int(li[i]))
                q.append(node.right)
            i+=1
        return root



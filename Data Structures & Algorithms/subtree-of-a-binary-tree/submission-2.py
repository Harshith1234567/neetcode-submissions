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

    def create_lps(self, pattern):
        m = len(pattern)
        lps = [0] * m
        length, i = 0, 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length:
                length = lps[length - 1]   # fall back, don't advance i
            else:
                i += 1
        return lps

    def kmp(self, text, pattern):
        m, n = len(pattern), len(text)
        lps = self.create_lps(pattern)

        # scan text; j = how much of the pattern is currently matched
        i = j = 0
        while i < n:
            if text[i] == pattern[j]:
                i += 1
                j += 1
                if j == m:
                    return True            # full pattern matched
            elif j:
                j = lps[j - 1]             # reuse the matched prefix, don't move i back
            else:
                i += 1
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        serialized_root = self.serialize(root)
        serialized_subRoot = self.serialize(subRoot)
        return self.kmp(serialized_root, serialized_subRoot)

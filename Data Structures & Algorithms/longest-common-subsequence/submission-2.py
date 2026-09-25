class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mat=defaultdict(lambda: defaultdict(int))
        m=len(text1)
        n=len(text2)
        for i in range(m):
            for j in range(n):
                
                if text1[i] == text2[j]:
                    mat[i][j]=1+mat[i-1][j-1]

                else:
                    mat[i][j]=max(mat[i-1][j], mat[i][j-1])

        return mat[m-1][n-1]





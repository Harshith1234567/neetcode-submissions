class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo={}

        m=len(matrix)
        n=len(matrix[0])

        def oom(r,c):
            if r>m-1 or r<0 or c>n-1 or c<0:
                return True

        def dfs(r,c):
            
            if (r,c) in memo:
                return memo[(r,c)]
            
            if oom(r,c):
                return 0

            s=1

            if not oom(r+1,c) and matrix[r+1][c]>matrix[r][c]:
                s=max(s,dfs(r+1,c)+1)


            if not oom(r,c+1) and matrix[r][c+1]>matrix[r][c]:
                s=max(s,dfs(r,c+1)+1)

            if not oom(r-1,c) and matrix[r-1][c]>matrix[r][c]:
                s=max(s,dfs(r-1,c)+1)

            if not oom(r,c-1) and matrix[r][c-1]>matrix[r][c]:
                s=max(s,dfs(r,c-1)+1)

            memo[(r,c)]=s

            return s


        maxi=0

        for x in range(m):
            for y in range(n):
                maxi=max(maxi,dfs(x,y))

        return maxi
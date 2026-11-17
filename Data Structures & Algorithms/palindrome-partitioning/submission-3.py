class Solution:

    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        memo=[[False] * n for _ in range(n)]

        for l in range(1,n+1):
            for i in range(n-l+1):
                memo[i][i+l-1]= (s[i]==s[i+l-1] and (i+1>=i+l-2 or memo[i+1][i+l-2]) )


        def dfs(i):
            if i>=n:
                return [[]]

            res=[]

            for j in range(i,n):
                if memo[i][j]:
                    nxt=dfs(j+1)

                    for a in nxt:
                        cur=[s[i:j+1]]+a
                        res.append(cur)



            return res

        return dfs(0)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxi=[0]
        count=[0]
        def dfs(i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0:

                return

            grid[i][j]=0
            count[0]+=1

            

            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)


        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    count=[0]
                    dfs(r,c)
                    maxi[0]=max(maxi[0],count[0])

        return maxi[0]
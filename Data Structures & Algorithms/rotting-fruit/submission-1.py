class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q=deque([])
        countfruit=0
        countvis=0


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append([r,c])
                    countfruit+=1
                    countvis+=1
                    grid[r][c]=3

                if grid[r][c]==1:
                    countfruit+=1

        if countfruit==0:
            return 0
        
        res=0
        while q:
            n=len(q)
            res+=1
            for _ in range(n):
                r,c=q.popleft()

                for x,y in [[0,1],[0,-1],[1,0],[-1,0]]:
                    a,b=r+x,c+y
                    if a<0 or b<0 or a>=len(grid) or b>=len(grid[0]) or grid[a][b]==3 or grid[a][b]==0:
                        continue

                    q.append([a,b])
                    grid[a][b]=3
                    countvis+=1

        
                        
        if countvis==countfruit:
            res-=1
            return res

        return -1

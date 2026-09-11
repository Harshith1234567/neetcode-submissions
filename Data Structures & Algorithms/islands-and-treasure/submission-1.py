class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # nr,nc = len(grid), len(grid[0])

        # def bfs(x,y):
        #     q=deque([])
        #     for t1 , t2 in [[0,1],[0,-1],[1,0],[-1,0]]:
        #         k=x+t1
        #         l=y+t2

        #         if k>=0 and k<nr and l>= 0 and l<nc and grid[k][l] >0:
        #             q.append([k, l])
        #     to_add=0
        #     while q:
        #         #print(q)
        #         n=len(q)
        #         to_add+=1
        #         for _ in range(n):
        #             a, b = q.popleft()
        #             if grid[a][b] >0 and grid[a][b]>to_add:
                        
        #                 grid[a][b] = to_add

        #                 for t1 , t2 in [[0,1],[0,-1],[1,0],[-1,0]]:
        #                     k=a+t1
        #                     l=b+t2

        #                     if k>=0 and k<nr and l>= 0 and l<nc and grid[k][l] >0:
        #                         q.append([k, l])


            


        # for r in range(nr):
        #     for c in range(nc):
        #         if grid[r][c] ==0:
        #             bfs(r,c)
        #             #print(grid)


























        nr, nc = len(grid) , len(grid[0])
        q=deque([])
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 0:
                    q.append([r,c])
        res=1
        while q:
            n=len(q)
            for _ in range(n):
                x, y =q.popleft()

                for a,b in [[0,1],[0,-1],[1,0],[-1,0]]:
                    c=x+a
                    d=y+b

                    if c>=0 and c<nr and d>=0 and d<nc and grid[c][d] == 2147483647:
                        q.append([c,d])
                        grid[c][d] = res


            res+=1

        


        
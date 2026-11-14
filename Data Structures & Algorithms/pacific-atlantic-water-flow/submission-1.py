class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        res=[[set() for _ in range(len(heights[0]))] for a in range(len(heights))]
        final=[]
        def bfs(q,visit):

            while q:
                r,c=q.popleft()

                for x,y in [[0,1],[0,-1],[1,0],[-1,0]]:
                    
                    a,b=r+x,c+y

                    if a<0 or b<0 or a>=len(heights) or b>=len(heights[0]) or visit in res[a][b] :
                        continue
                    if heights[r][c]<=heights[a][b]:
                        res[a][b].add(visit)
                        q.append([a,b])

                        

                    



        q=deque([])
        for c in range(len(heights[0])):
            res[0][c].add('p')
            q.append([0,c])

        for r in range(len(heights)):
            res[r][0].add('p')
            q.append([r,0])
        bfs(q,'p')
        # print('1',res)
        q=deque([])
        for c in range(len(heights[0])):
            res[-1][c].add('a')
            q.append([len(heights)-1,c])
            

        for r in range(len(heights)):
            res[r][-1].add('a')
            
            q.append([r,len(heights[0])-1])

            


        # print('2',res)
        
        bfs(q,'a')
        

        return [[r, c] for r in range(len(heights)) for c in range(len(heights[0]))
        if 'p' in res[r][c] and 'a' in res[r][c]]


        
        
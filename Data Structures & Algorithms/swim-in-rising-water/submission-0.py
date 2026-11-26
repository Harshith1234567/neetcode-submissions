class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        heap=[[grid[0][0],0,0]]
        heapq.heapify(heap)

        visit=set()
        visit.add((0, 0))

        while heap:
            t,r,c =heapq.heappop(heap)
            if r==rows-1 and c==cols-1:
                return t

            for r1, c1 in [[0,1],[0,-1],[1,0],[-1,0]]:
                x,y=r1+r,c1+c

                if x<0 or y<0 or x>=rows or y>=cols or (x,y) in visit:
                    continue

                visit.add((x,y))
                heapq.heappush(heap,[max(t,grid[x][y]), x,y])


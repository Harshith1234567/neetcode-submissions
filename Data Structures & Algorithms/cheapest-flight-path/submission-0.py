class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src==dst:
            return 0


        graph=defaultdict(list)
        
        for x,y,c in flights:
            graph[x].append([y,c])

        
        q=deque([[0,-1,src]])
        prices={src:0}
        

        while q:
            c,s,node=q.popleft()
            if s>=k:
                continue

            for nei,ec in graph[node]:
                nc=c+ec

                if nei not in prices or nc<prices[nei]:
                    prices[nei] =nc
                    q.append([nc,s+1,nei])

        return prices[dst] if dst in prices else -1
                    




        
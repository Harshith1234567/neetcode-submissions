class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph=defaultdict(list)

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def bfs(i):
            q=deque([i])
            vis.add(i)

            while q:
                ele=q.popleft()
                for ne in graph[ele]:
                    if ne not in vis:
                        vis.add(ne)
                        q.append(ne)
                    

        count=0
        vis=set()
        for e in range(n):
            if e not in vis:
                count+=1
                bfs(e)

        return count
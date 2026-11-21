class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph=defaultdict(list)

        indegree=defaultdict(int)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

            indegree[u]+=1
            indegree[v]+=1


        q=deque([])
        for i in range(1,len(edges)+1):
            if indegree[i]==1:
                q.append(i)

        while q:
            ele = q.popleft()
            indegree[ele]-=1

            for nei in graph[ele]:
                indegree[nei]-=1
                if indegree[nei]==1:
                    q.append(nei)

        for u,v in reversed(edges):
            if indegree[u] ==2 and indegree[v]:
                return [u,v]

        return []

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj=defaultdict(list)

        for x,y in sorted(tickets)[::-1]:
            adj[x].append(y)

        res=[]

        def dfs(node):
            while adj[node]:
                dst=adj[node].pop()
                dfs(dst)
            res.append(node)



        dfs('JFK')
        return res[::-1]
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dic=defaultdict(list)
        if len(edges) > n - 1:
            return False

        for e in edges:
            dic[e[0]].append(e[1])
            dic[e[1]].append(e[0])

        visit=set()
        q=deque([[0,-1]])
        visit.add(0)

        while q:
            e=q.popleft()

            for adj in dic[e[0]]:
                if adj == e[1]:
                    continue
                if adj in visit :
                    return False

                visit.add(adj)
                q.append([adj, e[0]])
                
        return len(visit) == n

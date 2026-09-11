class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # dic=defaultdict(list)
        # if len(edges) > n - 1:
        #     return False

        # for e in edges:
        #     dic[e[0]].append(e[1])
        #     dic[e[1]].append(e[0])

        # visit=set()
        # q=deque([[0,-1]])
        # visit.add(0)

        # while q:
        #     e=q.popleft()

        #     for adj in dic[e[0]]:
        #         if adj == e[1]:
        #             continue
        #         if adj in visit :
        #             return False

        #         visit.add(adj)
        #         q.append([adj, e[0]])
                
        # return len(visit) == n
















        # inorder=defaultdict(int)
        # adja= defaultdict(list)
        # for edj in edges:
        #     inorder[edj[0]]+=1
        #     inorder[edj[1]]+=1
        #     adja[edj[0]].append(edj[1])
        #     adja[edj[1]].append(edj[0])

        # q=deque()
        # res=set()

        # for i in range(n):
        #     if inorder[i] ==1:
        #         q.append(i)

        # while q:
        #     e = q.popleft()
        #     res.add(e)
        #     for a in adja[e]:
        #         # if a in res:
        #         #     return False
        #         inorder[a]-=1
        #         if inorder[a]==1:
        #             q.append(a)



        # return len(res) == n









        adj=defaultdict(list)
        inorder=defaultdict(int)

        

        for pre in edges:
            adj[pre[0]].append(pre[1])
            adj[pre[1]].append(pre[0])
            inorder[pre[1]]+=1
            inorder[pre[0]]+=1
        q=deque([(0,-1)])
        count=0
        res={0}
        # for i in range(n):
        #     if inorder[i]==1:
        #         q.append(i)
        #         count+=1
        #         res.add(i)

        while q:

            node, parent=q.popleft()
            for nei in adj[node]:
                if nei==parent:
                    continue
                if nei in res:
                    return False

                res.add(nei)
                q.append((nei, node))


        return len(res)==n



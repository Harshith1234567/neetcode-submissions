class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # dic=defaultdict(list)
        
        # for e in edges:
        #     dic[e[0]].append(e[1])
        #     dic[e[1]].append(e[0])

        # print(dic)

        # def bfs(p):
        #     q=deque()
        #     q.append(p)
        #     vis=set()
        #     while q:
        #         e=q.popleft()
        #         print("e",e)
        #         if e in vis:
        #             continue
        #         vis.add(e)

        #         for nei in dic[e]:
        #             if nei in vis:
        #                 continue
        #             q.append(nei)
        #         dic[e]=[]
        #     print("vis",vis)
        #     return vis
        # count=0
        # visited=set()
        # for i in range(n):
        #     print("i",i)
        #     if len(dic[i]) >0:
        #         count+=1
        #         vis=bfs(i)
        #         #print("outer vis", vis)
        #         visited= visited.union(vis)
        #     elif i not in visited:
        #         count+=1
        #         visited.add(i)
        #     #print("visited",visited)

    

        # return count


        dic=defaultdict(list)
        
        for e in edges:
            dic[e[0]].append(e[1])
            dic[e[1]].append(e[0])



        def bfs(root):
            visited.add(root)
            q=deque([root])

            while q:
                e=q.popleft()

                for a in dic[e]:
                    if a in visited:
                        continue
                    q.append(a)
                    visited.add(a)
                #dic[e]=[]
            #return vis
        visited=set()
        count=0
        for i in range(n):
            # if len(dic[i])>0:
            #     count+=1
            #     #visited.union(bfs(i))

            if i not in visited:
                count+=1
                
                visited.add(i)
                bfs(i)

        return count

            





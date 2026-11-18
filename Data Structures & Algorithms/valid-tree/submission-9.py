class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        if n==1:
            return True
        inorder=defaultdict(int)

        graph=defaultdict(list)

        for x,y in edges:
            inorder[x]+=1
            inorder[y]+=1
            graph[x].append(y)
            graph[y].append(x)

        q=deque([])

        for i in range(n):
            if inorder[i]==1:
                q.append(i)
        count=0
        
        while q:
            ele=q.popleft()
            count+=1

            for nei in graph[ele]:
                inorder[nei]-=1
                if inorder[nei]==1:
                    q.append(nei)

        return count==n
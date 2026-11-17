class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inorder=defaultdict(int)

        graph=defaultdict(list)

        for dst,src in prerequisites:
            inorder[dst]+=1
            graph[src].append(dst)

        q=deque([])
        li=[]
        for i in range(numCourses):
            if inorder[i]==0:
                q.append(i)
                li.append(i)
        
        while q:
            ele=q.popleft()


            for nei in graph[ele]:
                inorder[nei]-=1
                if inorder[nei]==0:
                    li.append(nei)
                    q.append(nei)

        return li if len(li)==numCourses else []
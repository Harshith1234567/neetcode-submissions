class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        inorder=defaultdict(int)

        graph=defaultdict(list)

        for dst,src in prerequisites:
            inorder[dst]+=1
            graph[src].append(dst)

        q=deque([])

        for i in range(numCourses):
            if inorder[i]==0:
                q.append(i)
        count=0
        while q:
            ele=q.popleft()
            count+=1

            for nei in graph[ele]:
                inorder[nei]-=1
                if inorder[nei]==0:
                    q.append(nei)

        return count==numCourses
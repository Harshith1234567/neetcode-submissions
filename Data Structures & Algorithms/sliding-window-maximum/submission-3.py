class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output=[]
        q=deque()

        l=0

        for r,num in enumerate((nums)):
            while q and nums[q[-1]] <num:
                q.pop()

            q.append(r)

            while l>q[0]:
                q.popleft()

            if r+1>=k:
                

                output.append(nums[q[0]])
                l+=1

        return output

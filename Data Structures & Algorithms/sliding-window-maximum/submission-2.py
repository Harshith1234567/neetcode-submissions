
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        l=0
        li=[]
        res=[]
        for r in range(k):
            heapq.heappush(li,[-1*nums[r],r] )

        res.append(-1*li[0][0])

        # print(res)
        for r in range(k,len(nums)):
            # print(r)
            l+=1
            heapq.heappush(li,[-1*nums[r],r] )
            # print(li)

            while li[0][1]<l:
                heapq.heappop(li)

            res.append(-1*li[0][0])

        return res


            
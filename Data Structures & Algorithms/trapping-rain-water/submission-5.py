class Solution:
    def trap(self, height: List[int]) -> int:
        
        li=[0]
        maxi=height[0]
        for i in range(1,len(height)):
            li.append(maxi)
            maxi=max(maxi, height[i] )

        maxi=height[-1]
        res=0
        for i in range(len(height)-2, -1,-1):
            res+=(  max(min(li[i],maxi) - height[i],0 )  )
            maxi=max(maxi, height[i] )

        return res
                
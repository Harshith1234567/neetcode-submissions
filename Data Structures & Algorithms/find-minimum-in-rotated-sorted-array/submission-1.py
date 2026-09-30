class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        mini=float('inf')

        while l<=r:
            m=l+(r-l)//2
            mini=min(mini,nums[m])

            if nums[m]<nums[r]:
                r=m

            else:
                l=m+1

        return mini

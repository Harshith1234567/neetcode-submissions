class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=nums[0]
        sums=0

        for n in nums:
            sums+=n
            maxi=max(maxi,sums)
            
            if sums<0:
                sums=0

        return maxi





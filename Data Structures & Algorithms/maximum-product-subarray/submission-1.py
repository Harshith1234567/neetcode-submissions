class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]

        maxi=mini=1

        for num in nums:
            t=maxi*num
            maxi=max(t,num*mini,num)
            mini=min(t,num*mini,num)
            res=max(res,maxi)

        return res
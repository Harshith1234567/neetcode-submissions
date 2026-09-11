class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res=[1]*len(nums)
        t=nums[0]
        for i in range(1,len(nums)):
            res[i]=t
            t*=nums[i]

        t=nums[-1]

        for i in range(len(nums)-2,-1,-1):
            res[i]*=t
            t*=nums[i]



        return res

        
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        

        li=[1]*len(nums)
        maxi=1
        for i in range(1,len(nums)):

            
            for j in range(i):

                if nums[j]<nums[i] and li[j]+1>li[i]:
                    li[i]=li[j]+1
                    maxi=max(maxi,li[i])

        return maxi




            
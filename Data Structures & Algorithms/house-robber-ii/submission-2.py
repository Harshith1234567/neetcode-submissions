class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        a,b=0,0
        res1=0
        for num in nums[:-1]:
            t=max(num+a,b)
            
            a=b
            b=t


        res1=b
        a,b=0,0
        for num in nums[1:]:
            t=max(num+a,b)
            
            a=b
            b=t
            

        return max(b,res1)


        

        
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1 or n==2 or n==3:
            return max(nums)


        a=nums[0]
        b=max(nums[0], nums[1])

        for i in range(2,n-1):
            c=max(a+nums[i], b)

            b,a=c,b

        max_b=b
        
        a=nums[1]
        b= max(nums[1], nums[2])

        for i in range(3,n):
            c=max(a+nums[i], b)

            b,a=c,b

        return max(b, max_b)
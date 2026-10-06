class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi=0

        for i,n in enumerate(nums[:-1]):
            if n==0 and maxi<=i:
                return False
            maxi=max(maxi,i+n)

            

        return True if  maxi>=len(nums)-1 else False


        
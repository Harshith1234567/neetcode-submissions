import copy
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        def dfs(i,li,count):
            if count==target :
                res.append(copy.copy(li))

                return 

            if count>=target or i>=len(nums):
                return

            dfs(i,li+[nums[i]],count+nums[i])
            
            dfs(i+1,li,count)

        dfs(0,[],0)
        return res
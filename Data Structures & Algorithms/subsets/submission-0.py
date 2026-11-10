class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def dfs(cur,i):
            if i>=len(nums):
                res.append(cur)

                return
            
            dfs(cur+[nums[i]],i+1)
            dfs(cur,i+1)



        dfs([],0)
        return res
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]

        def dfs(i,li):
            res.append(li[::])

            for j in range(i,len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue

                dfs(j+1,li+[nums[j]])

        dfs(0,[])
        return res
        
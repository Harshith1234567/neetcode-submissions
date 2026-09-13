class Solution:
    def rob(self, nums: List[int]) -> int:
        dic={}
        def dfs(i):
            if i>=len(nums):
                return 0
            if i in dic:
                return dic[i]

            dic[i] = max(nums[i]+dfs(i+2), dfs(i+1))
            return dic[i]

        return dfs(0)
        
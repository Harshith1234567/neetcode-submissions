class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        t=sum(nums)

        if t%2:
            return False

        dicto=defaultdict(dict)

        def dfs(i, tar):
            if tar==0:
                return True

            if i>=len(nums) or tar<0:
                return False
            if tar in dicto[i]:
                return dicto[i][tar]

            dicto[i][tar] = (dfs(i+1, tar-nums[i]) or dfs(i+1, tar))
            return dicto[i][tar]
            
            




        return dfs(0,t//2)
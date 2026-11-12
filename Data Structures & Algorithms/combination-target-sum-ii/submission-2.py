import copy
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()

        def dfs(idx,li,count):
            if count==target :
                res.append(copy.copy(li))

                return 

            for i in range(idx,len(candidates)):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                if count+candidates[i]>target:
                    break
                dfs(i+1,li+[candidates[i]],count+candidates[i])

            

        dfs(0,[],0)
        

        return res
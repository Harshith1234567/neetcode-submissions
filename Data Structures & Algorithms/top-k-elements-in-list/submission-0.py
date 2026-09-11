class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for n in nums:
            if n not in dic:
                dic[n]=1
            else:
                dic[n]=dic[n]+1
        nums=sorted(dic.items(),key=lambda x:x[1],reverse = True)
        #nums=nums.values()
        return [x[0] for x in nums[:k]]
        
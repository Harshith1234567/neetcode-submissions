from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums=list(Counter(nums).items())

        nums = sorted(nums,key=lambda x:x[-1], reverse=True)



        return [nums[x][0] for x in range(k) ]
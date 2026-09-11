class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,num in enumerate(nums):
            try:
                if (target-num) in nums:
                    return[i,i+1+(nums[i+1:].index(target-num))]
            except:
                continue

        
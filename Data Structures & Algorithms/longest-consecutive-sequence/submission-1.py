class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns=set(nums)
        maxi=0
        for num in nums:
            if num-1 in ns:
                continue
            t=0
            while num in ns:
                num+=1
                t+=1
            maxi=max(t,maxi)

        return maxi

            
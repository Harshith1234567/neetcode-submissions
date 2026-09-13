class Solution:
    def rob(self, nums: List[int]) -> int:
        a,b=0,0

        for num in nums:
            t=max(num+ a,b)

            a=b
            b=t

        return b
        
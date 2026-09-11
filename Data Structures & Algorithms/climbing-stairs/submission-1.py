class Solution:
    def climbStairs(self, n: int) -> int:
        s=math.sqrt(5)

        a=(1+s)/2
        b=(1-s)/2
        n+=1

        return round((a**n - b**n)/s)
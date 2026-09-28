class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        res=r=max(piles)


        while l<=r:
            m=l+((r-l)//2)
            t=0
            for p in piles:
                t+=(math.ceil(float(p)/m))

            if t<=h:
                res=min(res,m)

                r=m-1

            else:
                l=m+1

        return res

                
import heapq
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pa= [[p,s] for p,s in zip(position,speed)]

        pa.sort(reverse=True)

        ini=(target-pa[0][0])/pa[0][1]

        res=1

        for p in pa:



            t=(target-p[0])/p[1]

            if t>ini:
                res+=1

                ini=t

        return res
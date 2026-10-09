class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        diff=0
        res=-1
        for i in range(len(gas)):
            td=gas[i]-cost[i]
            if res==-1 and td>=0:
                res=i

            diff+=td
            if diff<0:
                diff=0
                res=-1

        return res
            



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        memo=defaultdict(int)

        for x,y in intervals:
            memo[x]+=1
            memo[y]-=1

        res=[]
        li=[]
        cur=0
        for i in sorted(memo):
            if not li:
                li.append(i)
            cur+=memo[i]
            if cur == 0:
                li.append(i)
                res.append(li)
                li=[]

        return res
            


        
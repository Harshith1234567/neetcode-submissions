class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        li=[]
        res=[0]*len(temperatures)

        for i in range(len(res)):
            if len(res) == 0 or (len(li) and temperatures[i]<=li[-1][1]):
                li.append((i,temperatures[i]))
                continue
            while len(li) and li[-1][1] < temperatures[i]:
                res[li[-1][0]]=i-li[-1][0]
                li.pop()

            li.append((i,temperatures[i]))

        return res



        
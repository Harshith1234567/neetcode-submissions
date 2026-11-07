class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dicto=Counter(tasks)


        maxvalue=0
        count=0

        for e in dicto:

            if dicto[e]>maxvalue:
                maxvalue=dicto[e]
                count=1
            elif dicto[e]==maxvalue:
                count+=1

        pos=((n+1)*(maxvalue-1))+count

        return max(pos,len(tasks))
        
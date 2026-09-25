class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        li=[]
        res=[]
        n=len(temperatures)
        

        for i in range(n-1,-1,-1):
            

            while li and temperatures[li[-1]]<=temperatures[i]:
                    li.pop()

            if li==[]:
                
                res.append(0)

            
            else:
                res.append(li[-1]-i)


            li.append(i)

        return res[::-1]




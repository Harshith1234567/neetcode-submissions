class Solution:
    def isHappy(self, n: int) -> bool:
        vis=[]
        vis.append(n)
        #n=self.getSquare(n)
        while n !=1:
            n=self.getSquare(n)
            if n in vis:
                return False
            vis.append(n)
            


        return True




    def getSquare(self, n)  :
        num =0  
        while n :
            num +=(n % 10) **2
            n=n//10
        n=num
        return num
        
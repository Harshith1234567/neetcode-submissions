class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def rec(x,a):
            
            if a==0:
                return 1
            if a==1 :
                return x

            if a%2:
                return (rec(x,a//2)**2 ) *x
            else:
                return   (rec(x,a//2)**2 )

        if n < 0:
            return rec(1/x, -n)
        return rec(x,n)      
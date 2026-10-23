class Solution:
    def isHappy(self, n: int) -> bool:

        def sq_sums(num):
            res=0
            while num:
                r=num%10
                num=num//10
                res+=(r**2)

            return res

        f,s=n,n
        while f !=1 and s !=1:
            f=sq_sums(sq_sums(f))
            s=sq_sums(s)
            if f==1:
                break

            if f==s:

                return False



        return True

        


        
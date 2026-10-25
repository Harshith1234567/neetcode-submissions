class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        res=[0] * (len(num1)+len(num2))

        num1=num1[::-1]

        num2=num2[::-1]

        for i1,ele1 in enumerate(num1):
            for i2,ele2 in enumerate(num2):
                res[i1+i2] += int(ele1)*int(ele2)

                res[i1+i2+1]+=res[i1+i2]//10

                res[i1+i2]=res[i1+i2]%10

        res=res[::-1]
        s=0
        while s<len(res) and res[s]==0:
            s+=1

        res=map(str,res[s:])
        return ''.join(res)



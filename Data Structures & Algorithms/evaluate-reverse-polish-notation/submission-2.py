class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        li=[]

        


        for t in tokens:
            if t =='+':
                b=li.pop()
                a=li.pop()
                li.append(a + b)

            elif t =='-':
                b=li.pop()
                a=li.pop()
                li.append(a - b)

            elif t =='*':
                b=li.pop()
                a=li.pop()
                li.append(a * b)

            elif t =='/':
                b=li.pop()
                a=li.pop()
                li.append(int(a / b))

            else:
                li.append(int(t))

        return li[-1]

                
        
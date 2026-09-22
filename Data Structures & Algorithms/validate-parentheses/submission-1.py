class Solution:
    def isValid(self, s: str) -> bool:
        dicto={')':'(', '}':'{',']':'['}

        li=[]

        for a in s:
            if a not in dicto:
                li.append(a)

            else:
                if li==[] or li[-1]!=dicto[a]:
                    return False
                li.pop()




        return True if li==[] else False

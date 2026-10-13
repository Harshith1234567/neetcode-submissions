class Solution:
    def checkValidString(self, s: str) -> bool:
        inp=s
        l=[]
        s=[]

        for i, c in enumerate(inp):
            if c=='(':
                l.append(i)
            elif c=='*':
                s.append(i)

            else:
                if not l and not s:
                    return False

                if l:
                    l.pop()

                else:
                    s.pop()

        while l and s:
            if l.pop() > s.pop():
                return False

        return not l
        
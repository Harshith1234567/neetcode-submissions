class Solution:

    def encode(self, strs: List[str]) -> str:
        en=""
        for s in strs:
            en+=(str(len(s)) + '#'+ s)
        print (en)
        return en

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0

        while i<len(s):
            print(i)

            n=''

            while s[i]!='#':
                n+=s[i]
                i+=1
            
            i+=1


            res.append(s[i:i+int(n)])
            

            i=i+int(n)
            

        return res




class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+= (str(len(s)) + "#" +s )

        print(res) 
        return res

    def decode(self, s: str) -> List[str]:
        i=0
        n=len(s)
        res=[]
        while i<n:
            num=""
            while s[i]!="#":
                num+=s[i]
                i+=1
            #print(num)
            num=int(num)
            res.append(s[i+1:i+1+num])
            i=i+1+num

        return res


class Solution:

    def encode(self, strs: List[str]) -> str:
        # res=""
        # for s in strs:
        #     res+= (str(len(s)) + "#" +s )

        # print(res) 
        # return res









        e=""

        for s in strs:
            e+=(str(len(s))+"#"+s)

        return e




    def decode(self, s: str) -> List[str]:
        # i=0
        # n=len(s)
        # res=[]
        # while i<n:
        #     num=""
        #     while s[i]!="#":
        #         num+=s[i]
        #         i+=1
        #     #print(num)
        #     num=int(num)
        #     res.append(s[i+1:i+1+num])
        #     i=i+1+num

        # return res

















        n=len(s)
        i=0
        l=""
        res=[]
        while i<n:
            l=""
            while s[i]!="#":
                l+=s[i]
                i+=1
            #print(i)
            i+=1
            res.append(s[i: i+ int(l)])

            i=i+int(l)

        return res

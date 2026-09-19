class Solution:
    def minWindow(self, s: str, t: str) -> str:

        sdicto=defaultdict(int)
        tdicto={}

        for a in t:
            tdicto[a]=1+tdicto.get(a,0)

        # print(tdicto)
        
        m=26-len(tdicto)
        if m==26:
            return True

        l=0
        res=s
        flag=0
        for r,b in enumerate(s):
            sdicto[b]+=1
            # print(sdicto)

            if b in tdicto and sdicto[b]==tdicto[b] and sdicto[b]-1<tdicto[b]:
                m+=1

            # print(r,b, m)

            

            while m==26:
                flag=1
                if len(res) > (r-l+1):
                    res=s[l:r+1]
                
                a=s[l]
                
                if a not in tdicto or sdicto[a] > tdicto[a]:
                    sdicto[a]-=1
                    l+=1
                else:

                    break

        return res if flag else ''





            

            


        
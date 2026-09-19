class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dic=defaultdict(int)
        s2dic=defaultdict(int)
        if len(s1)>len(s2):
            return False

        for i in range(len(s1)):
            s1dic[s1[i]]+=1
            s2dic[s2[i]]+=1

        m=0

        for i in range(26):
            m+=(1 if s1dic[ chr(i + ord('a'))  ] == s2dic[chr(i + ord('a')) ] else 0)
        

        l=0
        for r in range(len(s1),len(s2)):
            if m==26 :
                return True
            s2dic[s2[r]]+=1
            if s1dic[s2[r]] ==s2dic[s2[r]]:
                m+=1
            elif s2dic[s2[r]] -1 == s1dic[s2[r]] :
                m-=1

            s2dic[s2[l]]-=1
            if s1dic[s2[l]] ==s2dic[s2[l]]:
                m+=1
            elif s2dic[s2[l]] + 1 == s1dic[s2[l]] :
                m-=1
            l+=1



        return m==26

            


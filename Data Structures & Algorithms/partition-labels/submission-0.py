class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dicto={}
        for i in range(len(s)):
            
            dicto[s[i]]=i
        li=[]
        count=0
        end=0
        for i, c in enumerate(s):
            count+=1
            end=max(end,dicto[c])

            if i==end:
                li.append(count)
                count=0

        return li


        

        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res=0
        l=0
        t=set()
        for r, a in enumerate(s):
            
            while a in t:
                t.remove(s[l])
                l+=1

            t.add(a)
            res=max(res,len(t))

        return res
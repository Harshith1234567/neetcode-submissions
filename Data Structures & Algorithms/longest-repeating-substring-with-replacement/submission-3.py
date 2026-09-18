class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mf=0
        dic=defaultdict(int)
        l=res=0

        for r in range(len(s)):

            dic[s[r]]+=1
            mf=max(dic[s[r]],mf)

            while r-l+1 - mf >k:
                dic[s[l]]-=1
                l+=1

            res=max(r-l+1,res)
        return res
        
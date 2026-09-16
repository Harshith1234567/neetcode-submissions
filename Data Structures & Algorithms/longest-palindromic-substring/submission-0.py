class Solution:
    def longestPalindrome(self, s: str) -> str:
        resl=0
        maxi=0
        

        for i in range(len(s)):
            l=r=i

            while l>=0 and r<len(s) and s[l]==s[r]:
                if maxi<r-l+1:
                    maxi=r-l+1
                    resl=l

                l-=1
                r+=1

            l=i
            r=i+1

            while l>=0 and r<len(s) and s[l]==s[r]:
                if maxi<r-l+1:
                    maxi=r-l+1
                    resl=l

                l-=1
                r+=1


        return s[resl:resl+maxi]

            
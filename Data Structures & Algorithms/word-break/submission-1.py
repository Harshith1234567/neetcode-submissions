class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem={}

        ml=0

        for word in wordDict:
            ml=max(ml,len(word))

        def dfs(i):
            if i in mem:
                return mem[i]
            if i ==len(s):
                return True
            

            

            for j in range(i,min(len(s), i+ml)):
                if s[i:j+1] in wordDict:
                    if dfs(j+1):
                        mem[i]=True
                        return True
                        

            mem[i]=False
            return False


        
        return dfs(0)
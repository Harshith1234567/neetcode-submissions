class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        if len(word1)<len(word2):
            word1,word2=word2,word1

        m=len(word1)
        n=len(word2)

        prev = list(range(n + 1))
        t= list(range(n + 1))

        for i,w1 in enumerate(word1):
            

            prev,t=t,[i+1]
            for j,w2 in enumerate(word2):
                mini=min(t[-1]+1,prev[j+1]+1)
                
                if w1==w2:
                    t.append(min(mini, prev[j]))

                else:
                    t.append(min(mini, prev[j]+1))

        return t[-1]




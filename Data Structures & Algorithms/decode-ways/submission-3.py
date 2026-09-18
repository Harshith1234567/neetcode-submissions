class Solution:
    def numDecodings(self, s: str) -> int:

        count=[0]
        dic={len(s):1}

        def dfs(i):
            
            t=0
            if i in dic:
                return dic[i]
            if i>=len(s) or int(s[i]) ==0:
                return 0
            # count[0]+=1
            
            if i+1<len(s):
                if int(s[i:i+2])>26 and int(s[i:i+2])%10==0:
                    count.append(3)
                    
                    return 0

                if int(s[i:i+2])<=26:
                    t+=dfs(i+2)
                    # count[0]+=1
            
            t+=dfs(i+1)
            dic[i]=t

            return t

                

        if int(s[0])==0:
            return 0
        
        a= dfs(0)

        if len(count)>1:
            return 0

        return a
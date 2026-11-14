class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        
        def dfs(op,cl,li):
            if op==cl==n:
                res.append(''.join(li))
                return
            
            if op<n:
                dfs(op+1,cl,li+['('])

            if cl<op:
                dfs(op,cl+1,li+[')'])


        
        dfs(0,0,[])
        return res
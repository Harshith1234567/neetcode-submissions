class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo=defaultdict(dict)
        
        def dfs(i,t):
            if t==0:
                
                return 1

            if i>=len(coins):
                return 0

            if t in memo[i]:
                return memo[i][t]

            s=0

            if t>=coins[i]:
                s=dfs(i+1, t)
                s+=dfs(i,t-coins[i])

            memo[i][t]=s
            return s

        return dfs(0,amount)

            

            






        
            
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo=defaultdict(dict)
        

        def dfs(i,b):

            if i>=len(prices):
                return 0

            if b in memo[i]:
                return memo[i][b]
            t=dfs(i+1,b)

            if b:
                buy=dfs(i+1,not b) -prices[i]
                memo[i][b]=max(buy,t)

            else:
                sell=dfs(i+2,not b) +prices[i]
                memo[i][b]=max(sell,t)


            
        
            return memo[i][b]
        return dfs(0,True)
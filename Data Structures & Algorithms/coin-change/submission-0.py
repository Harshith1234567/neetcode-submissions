class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dic={}

        def dfs(amt):
            if amt ==0:
                return 0
            if amt in dic:
                return dic[amt]

            res=1e9
            for coin in coins:
                if amt-coin>=0:
                    res=min(res, 1+dfs(amt-coin))
            dic[amt]=res
            return res


        m=dfs(amount)
        return m if m <1e9 else -1
        
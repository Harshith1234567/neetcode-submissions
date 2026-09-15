class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        low=prices[0]
        for price in prices:
            
           res=max(res,price-low)
           low=min(low,price)

        return res
        
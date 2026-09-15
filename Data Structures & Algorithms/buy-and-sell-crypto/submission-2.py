class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        maxi=low=prices[0]
        for price in prices:
            
            if price<low:
                low=price
                maxi=0
                continue
            maxi=max(maxi,price)


            res=max(res,maxi-low)

        return res
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float("inf")
        maxi = float("-inf")
        band=0
        for price in prices:
            if price < mini:
                mini=price
                maxi = float("-inf")
            else:
                print(price)
                if maxi < price:
                    maxi = price
                    if maxi-mini > band:
                        band= maxi-mini

        return band





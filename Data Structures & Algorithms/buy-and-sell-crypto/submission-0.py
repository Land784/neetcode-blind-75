class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxProfit = 0

        for price in prices:
            if price-minBuy > maxProfit:
                maxProfit = price - minBuy
            if price < minBuy:
                minBuy = price
        
        return maxProfit




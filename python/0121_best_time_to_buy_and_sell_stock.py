class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        low_price = prices[0]
        high_price = prices[0]
        for price in prices:
            if price < low_price:
                prev_profit = high_price - low_price
                if prev_profit > max_profit:
                    max_profit = prev_profit
                low_price = price
                high_price = price
            if price > high_price:
                high_price = price
                prev_profit = high_price - low_price
                if prev_profit > max_profit:
                    max_profit = prev_profit
                
        return max_profit

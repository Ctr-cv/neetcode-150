class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min = 10001
        max = -1
        for i, price in enumerate(prices):
            if i == 0:
                min = price
                continue
            if price - prices[i-1] > 0:
                if prices[i-1] < min:
                    min = prices[i-1]
                    max = 0
                if prices[i] > max:
                    max = prices[i]
            else:
                if result < max - min: result = max - min
        if max - min > result: result = max - min
        return result
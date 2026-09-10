class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        max_profit = 0
        if len(prices) == 1:
                return 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit > max_profit:
                max_profit = profit
            if prices[left] > prices[right]:
                left += 1
            else:
                right +=1
        return max_profit
            
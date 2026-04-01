class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0

        for i in range(1, len(prices)):
            
            curr_profit = prices[i] - min(prices[0:i])

            max_profit = max(max_profit, curr_profit)

        return max_profit
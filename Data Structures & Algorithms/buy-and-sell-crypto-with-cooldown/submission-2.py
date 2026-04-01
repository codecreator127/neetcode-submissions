class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        
        def dfs(day, holding):
            if day >= len(prices):
                return 0

            if (day, holding) in memo:
                return memo[(day, holding)]
            
            if holding:
                sell = prices[day] + dfs(day + 2, False)
                hold = dfs(day + 1, True)

                memo[(day, holding)] = max(sell, hold)
            else:
                buy = -prices[day] + dfs(day + 1, True)
                skip = dfs(day + 1, False)
                memo[(day, holding)] = max(buy, skip)

            return memo[(day, holding)]
        
        return dfs(0, False)
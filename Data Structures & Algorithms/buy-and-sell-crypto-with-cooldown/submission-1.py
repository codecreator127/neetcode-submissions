class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dfs(day, holding):
            if day >= len(prices):
                return 0
            
            if holding:
                sell = prices[day] + dfs(day + 2, False)
                hold = dfs(day + 1, True)

                return max(sell, hold)
            else:
                buy = -prices[day] + dfs(day + 1, True)
                skip = dfs(day + 1, False)
                return max(buy, skip)
                
        
        return dfs(0, False)
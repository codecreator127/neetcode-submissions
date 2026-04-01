class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ## use DP + memo

        memo = {}

        def dfs(i, j):
            if i == len(prices) - 1:
                if j != None:
                    return prices[i] - prices[j]
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]

            ## if bought, can sell or hold
            if j != None:
                memo[(i, j)] = max(dfs(i, None) + prices[i] - prices[j], dfs(i + 1, j))
            else:
                memo[(i, j)] = max(dfs(i + 1, None), dfs(i + 1, i))

            ## if not bought, can buy or skip

            return memo[(i, j)]

        return dfs(0, None)
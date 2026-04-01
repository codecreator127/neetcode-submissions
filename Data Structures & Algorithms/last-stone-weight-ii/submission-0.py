class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        memo = {}

        def dfs(i, diff):

            if i == len(stones):
                return abs(diff)
            
            if (i, diff) in memo:
                return memo[(i, diff)]

            add = dfs(i + 1, diff + stones[i])
            subtract = dfs(i + 1, diff - stones[i])

            memo[(i, diff)] = min(add, subtract)

            return memo[(i, diff)]
        
        return dfs(0, 0)
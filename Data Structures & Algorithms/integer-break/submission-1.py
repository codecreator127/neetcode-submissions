class Solution:
    def integerBreak(self, n: int) -> int:
        
        memo = {}
        
        def dfs(num):
            
            if num in memo:
                return memo[num]
            
            ans = 0

            for i in range(1, num):
                ans = max(
                    ans,
                    i * (num - i),
                    i * dfs(num - i)
                )
            
            memo[num] = ans
            return memo[num]
        
        return dfs(n)
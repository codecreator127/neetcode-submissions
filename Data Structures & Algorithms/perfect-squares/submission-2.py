class Solution:
    def numSquares(self, n: int) -> int:
        

        squares = []

        i = 1

        while i * i <= n:
            squares.append(i * i)
            i += 1

        memo = {}

        def dfs(remain):
            if remain == 0:
                return 0
            
            if remain in memo:
                return memo[remain]

            ans = float("inf")

            for sq in squares:
                if sq > remain:
                    break
                ans = min(ans, 1 + dfs(remain - sq))

            memo[remain] = ans
            return memo[remain]

        return dfs(n)
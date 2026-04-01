class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ## classic dp question
        dp = [[0] * n] * m

        def dfs(row, col):
            if row == (m - 1) and col == (n - 1):
                dp[m - 1][n - 1] += 1
                return

            # if dp[row][col] == 0:
            #     dp[row][col] += 1

            for dr, dc in [(1, 0), (0, 1)]:
                newRow = dr + row
                newCol = dc + col
                if newRow < m and newCol < n:
                    dfs(newRow, newCol)

            return

        dfs(0, 0)
        return dp[-1][-1]
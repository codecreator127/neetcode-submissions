class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        ## dfs
        ## memo
        ROW = len(grid)
        COL = len(grid[0])

        memo = {}

        def dfs(row, col):
            if row == ROW - 1 and col == COL - 1:
                return grid[row][col]
            
            if row >= ROW or col >= COL:
                return float("inf")
            
            if (row, col) in memo:
                return memo[(row, col)]
            
            curr = grid[row][col]

            memo[(row, col)] = min(curr + dfs(row + 1, col), curr + dfs(row, col + 1))
            return memo[(row, col)]
        
        return dfs(0, 0)
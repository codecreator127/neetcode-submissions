class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        ## starts at top left
        ## can either move down or right
        
        ROW = len(obstacleGrid)
        COL = len(obstacleGrid[0])
        
        memo = {}

        directions = [(0, 1), (1, 0)]

        def dfs(row, col):
            if row >= ROW or col >= COL:
                return 0

            if obstacleGrid[row][col] == 1:
                return 0
            
            if row == ROW - 1 and col == COL - 1:
                return 1
            
            if (row, col) in memo:
                return memo[(row, col)]

            memo[(row, col)] = dfs(row + 1, col) + dfs(row, col + 1)

            return memo[(row, col)]
        
        return dfs(0, 0)
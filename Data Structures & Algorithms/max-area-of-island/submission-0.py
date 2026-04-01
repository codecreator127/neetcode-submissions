class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        curr = 0

        def dfs(r, c):

            if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r])):
                return 0

            if grid[r][c] == 0:
                return 0

            if grid[r][c] == 1:
                grid[r][c] = 0
                return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

            return dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                maxArea = max(maxArea, dfs(r, c))

        
        return maxArea
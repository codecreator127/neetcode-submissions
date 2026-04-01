class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ## go through grid
        ## if hit a 1, increment counter
        ## do dfs until all 1s are turned to 0s
        ## iterate through all grid

        counter = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r])):
                return

            if grid[r][c] == '0':
                return
            
            grid[r][c] = '0'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                print(grid[r][c])
                if grid[r][c] == '1':
                    counter += 1
                    dfs(r, c)
    
        return counter

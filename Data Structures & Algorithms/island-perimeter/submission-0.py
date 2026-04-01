class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        ROW = len(grid)
        COL = len(grid[0])

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    start = (r, c)
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        seen = set()

        perimeter = 0

        def dfs(r, c):
            nonlocal perimeter

            if (r, c) in seen:
                return
            
            curr = 4

            for dr, dc in directions:
                
                newR = r + dr
                newC = c + dc

                if 0 <= newR < ROW and 0 <= newC < COL and grid[newR][newC] == 1:
                    seen.add((r, c))
                    curr -= 1
                    dfs(newR, newC)
                
            print(curr)
            
            perimeter += curr

        dfs(start[0], start[1])

        return perimeter






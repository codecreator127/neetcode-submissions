class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ## use dfs

        queue = deque()

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))

        ## do multisource bfs
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            r, c, distance = queue.popleft()

            if grid[r][c] == -1:
                continue
            
            if grid[r][c] == 2147483647:
                grid[r][c] = distance

            for dr, dc in directions:
                newRow = r + dr
                newCol = c + dc

                if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]) and grid[newRow][newCol] == 2147483647:
                    queue.append((newRow, newCol, distance + 1))


        return
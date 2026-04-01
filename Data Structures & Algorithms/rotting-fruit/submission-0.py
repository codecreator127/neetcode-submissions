class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()

        fresh = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1


        ## run bfs

        count = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue and fresh > 0:
            for _ in range(len(queue)):
                curr = queue.popleft()
                
                row = curr[0]
                col = curr[1]

                for dr, dc in directions:
                    newRow = dr + row
                    newCol = dc + col

                    if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]) and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        fresh -= 1
                        queue.append((newRow, newCol))
    
            count += 1

        
        return count if fresh == 0 else -1

            


                
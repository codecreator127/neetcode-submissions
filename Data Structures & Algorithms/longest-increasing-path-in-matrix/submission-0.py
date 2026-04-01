class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        ## multisource dfs
        ## return the longest possible path

        out = 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        memo = {}

        def dfs(r, c):
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            best = 1

            for dr, dc in directions:
                newR = r + dr
                newC = c + dc

                if 0 <= newR < len(matrix) and 0 <= newC < len(matrix[0]):
                    if matrix[newR][newC] > matrix[r][c]:
                        best = max(best, dfs(newR, newC) + 1)
            memo[(r, c)] = best
            return memo[(r, c)]
        
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                out = max(out, dfs(r, c))
        
        return out

            
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        firstRowZero = any(matrix[0][c] == 0 for c in range(n))
        firstColZero = any(matrix[r][0] == 0 for r in range(m))

        # Mark rows and columns
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Zero rows
        for r in range(1, m):
            if matrix[r][0] == 0:
                for c in range(1, n):
                    matrix[r][c] = 0

        # Zero columns
        for c in range(1, n):
            if matrix[0][c] == 0:
                for r in range(1, m):
                    matrix[r][c] = 0

        # Zero first row
        if firstRowZero:
            for c in range(n):
                matrix[0][c] = 0

        # Zero first column
        if firstColZero:
            for r in range(m):
                matrix[r][0] = 0
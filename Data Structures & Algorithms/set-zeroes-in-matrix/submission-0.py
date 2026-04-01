class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        zeros = []

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zeros.append((row, col))


        while zeros:
            row, col = zeros.pop()
            
            r = row + 1
            while r < len(matrix):
                matrix[r][col] = 0
                r += 1
            
            r = row - 1
            while r >= 0:
                matrix[r][col] = 0
                r -= 1
            
            c = col + 1
            while c < len(matrix[0]):
                matrix[row][c] = 0
                c += 1
            
            c = col - 1
            while c >= 0:
                matrix[row][c] = 0
                c -= 1
        
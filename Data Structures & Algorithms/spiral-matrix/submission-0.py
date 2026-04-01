class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ## use shrinking boundaries

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        out = []

        while top <= bottom and left <= right:
            # right
            for c in range(left, right + 1):
                out.append(matrix[top][c])
            top += 1

            # down
            for c in range(top, bottom + 1):
                out.append(matrix[c][right])
            right -= 1

            if top <= bottom:
                # left
                for c in range(right, left - 1, -1):
                    out.append(matrix[bottom][c])
                
                bottom -= 1

            if left <= right:
                # up
                for c in range(bottom, top - 1, -1):
                    out.append(matrix[c][left])

                left += 1

        return out
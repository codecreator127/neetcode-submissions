class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## run binary search twice, once for col, once for row

        outerLeft = 0
        outerRight = len(matrix) - 1

        while outerLeft <= outerRight:
            middle = (outerRight - outerLeft) // 2 + outerLeft

            if matrix[middle][0] > target:
                
                outerRight = middle - 1
            
            elif matrix[middle][-1] < target:
                outerLeft = middle + 1

            else:
                break


        if matrix[middle][0] <= target and target <= matrix[middle][-1]:

            row = matrix[middle]

            left = 0
            right = len(row) - 1

            while left <= right:
                
                mid = (right - left) // 2 + left
                
                if row[mid] < target:
                    left = mid + 1
                elif row[mid] > target:
                    right = mid - 1

                else:
                    return True

            
        return False
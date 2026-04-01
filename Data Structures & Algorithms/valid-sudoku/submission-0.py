class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # intuition, iterate through board once, put seen nums in seen dict, and check the row and the box
        seen = {}


        for row in range(len(board)):
            for col in range(len(board[row])):
                num = board[row][col]
                
                if num.isdigit() is False:
                    continue

                print(num)
                
                if num not in seen:
                    seen[num] = [(row, col)]
                else:
                    # check if valid

                    # invalid if same row or same col or within same box

                    for seen_num_coords in seen[num]:
                        if seen_num_coords[0] == row or seen_num_coords[1] == col:
                            return False

                        if (row // 3) * 3 + (col // 3) ==  (seen_num_coords[0] // 3) * 3 + (seen_num_coords[1] // 3):
                            return False

                    seen[num].append((row, col))

        return True
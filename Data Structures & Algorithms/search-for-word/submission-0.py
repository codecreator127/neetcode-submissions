class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        ## 4 choices, up, down, left, right anew

        curr = {}
        def backtrack(row, col, i):
            if row >= len(board) or row < 0 or col >= len(board[row]) or col < 0:
                return False

            if board[row][col] != word[i]:
                return False

            if i == len(word) - 1:
                return True

            temp = board[row][col]
            board[row][col] = "#"

            found = (
                backtrack(row + 1, col, i + 1) or
                backtrack(row - 1, col, i + 1) or
                backtrack(row, col + 1, i + 1) or
                backtrack(row, col - 1, i + 1)
            )
            # restore
            board[row][col] = temp
            return found
            
        for r in range(len(board)):
            for c in range(len(board[r])):
                if backtrack(r, c, 0):
                    return True

        return False
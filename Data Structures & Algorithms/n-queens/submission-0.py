class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ## 2 choices, put queen down, or not put queen down

        ## base case, check if we have hit n queens
        ## base check if valid board

        out = []

        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                out.append(copy)
                return
            
            for c in range(n):
                if self.checkValid(r, c, board):
                    board[r][c] = "Q"
                    backtrack(r + 1)
                    board[r][c] = "."


        backtrack(0)
        return out


    # only check the Qs before, don't need to check after
    def checkValid(self, r, c, board):

        row = r - 1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1

        row = r - 1
        col = c - 1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        row = r - 1
        col = c + 1

        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1

        return True

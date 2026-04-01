class Solution:
    def solve(self, board: List[List[str]]) -> None:

        if not board:
            return
        
        queue = deque()

        rows = len(board)
        cols = len(board[0])

        def add_if_O(r, c):
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == "O":
                board[r][c] = "S"
                queue.append((r, c))

        for r in range(rows):
            add_if_O(r, 0)
            add_if_O(r, cols - 1)

        for c in range(cols):
            add_if_O(0, c)
            add_if_O(rows - 1, c)

        ## do bfs to check if it is surrounded or not, if it is then color it in

        while queue:
            r, c = queue.popleft()

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newRow = r + dr
                newCol = c + dc

                add_if_O(newRow, newCol)

        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"


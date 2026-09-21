class Solution:
    def solve(self, board: List[List[str]]) -> None:

        regions = []
        
        def dfs(r, c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[r]):
                return
            if board[r][c] == 'X':
                return

            if (r, c) in regions:
                return

            regions.append((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)

            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)

        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c)

            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    if (r, c) not in regions:
                        board[r][c] = 'X'
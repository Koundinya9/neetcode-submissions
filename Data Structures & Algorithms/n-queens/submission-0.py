class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [['.'] * n for _ in range(n)]
        ans = []
        def backtrack(r):
            if r == n:
                copy = [''.join(row) for row in board]
                ans.append(copy)
                return

            for c in range(n):
                if safe(r, c, board):
                    board[r][c] = 'Q'
                    backtrack(r + 1)
                    board[r][c] = '.'


        def safe(row, col, board):
            
            for r in range(row):
                if board[r][col] == 'Q':
                    return False



            r = row - 1
            c = col - 1

            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1

            r = row - 1
            c = col + 1

            while r >= 0 and c < len(board):
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c += 1

            return True

        
        backtrack(0)

        return ans

            

            
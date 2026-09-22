class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def backtrack(path, i, j):
            if (i, j) in visited:
                return False

            visited.add((i, j))
            path += board[i][j]

            if path[-1] != word[len(path) - 1]:
                visited.remove((i, j))
                return False

            if path == word:
                return True

            if i > 0 and backtrack(path, i - 1, j):
                return True
            if i < len(board) - 1 and backtrack(path, i + 1, j):
                return True
            if j > 0 and backtrack(path, i, j - 1):
                return True
            if j < len(board[i]) - 1 and backtrack(path, i, j + 1):
                return True

            visited.remove((i, j))
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if backtrack("", i, j):
                        return True

        return False
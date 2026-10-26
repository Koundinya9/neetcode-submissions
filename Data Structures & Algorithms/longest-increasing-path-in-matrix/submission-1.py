class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        cache = {}

        def rec(i, j, ans):
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[i]):
                return 0

            if (i, j, ans) in cache:
                return cache[(i, j, ans)]

            left = right = top = down = 0

            if i + 1 < len(matrix) and matrix[i + 1][j] > matrix[i][j]:
                down = 1 + rec(i + 1, j, ans)

            if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
                top = 1 + rec(i - 1, j, ans)

            if j + 1 < len(matrix[i]) and matrix[i][j + 1] > matrix[i][j]:
                right = 1 + rec(i, j + 1, ans)

            if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
                left = 1 + rec(i, j - 1, ans)

            cache[(i, j, ans)] = max(1, left, right, top, down)

            return cache[(i, j, ans)]

        ans = 0


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, rec(i, j, 0))
        return ans
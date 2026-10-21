class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        paths = {}

        def rec(i, j):
            if i == m - 1 and j == n - 1:
                return 1

            if i >= m or j >= n:
                return 0

            if (i, j) in paths:
                return paths[(i, j)]

            paths[(i, j)] = rec(i + 1, j) + rec(i, j + 1)

            return paths[(i, j)]

        return rec(0, 0)
        
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        cache = {}


        def rec(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i == len(triangle) or j == len(triangle[i]):
                return 0
        
            cache[(i, j)] = triangle[i][j] + min(rec(i + 1, j), rec(i + 1, j + 1))
            return cache[(i, j)]

        return rec(0, 0)
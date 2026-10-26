class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        cache = {}
        
        def rec(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if j >= len(t):
                return 1

            if i >= len(s):
                return 0
            

            if s[i] == t[j]:
                cache[(i, j)] = rec(i + 1, j + 1) + rec(i + 1, j)
                return cache[(i, j)]

            cache[(i, j)] = rec(i + 1, j)

            return cache[(i, j)]
            

        return rec(0, 0)
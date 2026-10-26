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
            
            cache[(i, j)] = rec(i + 1, j)

            if s[i] == t[j]:
                cache[(i, j)] += rec(i + 1, j + 1)

            return cache[(i, j)]
            

        return rec(0, 0)
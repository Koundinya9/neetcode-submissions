class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        cache = {}

        def rec(i, j):
            if j >= len(p) and i >= len(s):
                return True

            if j >= len(p):
                return False

            if (i, j) in cache:
                return cache[(i, j)]

            res = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if j + 1 < len(p) and p[j + 1] == '*':
                res = rec(i, j + 2) or (res and rec(i + 1, j))

            else:
                res = res and rec(i + 1, j + 1)

            
            
            cache[(i, j)] = res
            return cache[(i, j)]

            

        return rec(0, 0)
        
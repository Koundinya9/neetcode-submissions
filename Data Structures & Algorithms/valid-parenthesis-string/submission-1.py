class Solution:
    def checkValidString(self, s: str) -> bool:
        cache = {}
        def rec(i, o):
            if o < 0:
                cache[(i, o)] = False
                return False

            if (i, o) in cache:
                return cache[(i, o)]

            if i == len(s):
                if o == 0:
                    cache[(i, o)] = True
                    return True
                cache[(i, o)] = False
                return False

            if s[i] == '(':
                cache[(i, o)] = rec(i + 1, o + 1)
            elif s[i] == ')':
                cache[(i, o)] = rec(i + 1, o - 1)
            else:
                cache[(i, o)] = rec(i + 1, o) or rec(i + 1, o + 1) or rec(i + 1, o - 1)
            return cache[(i, o)]


        return rec(0, 0)
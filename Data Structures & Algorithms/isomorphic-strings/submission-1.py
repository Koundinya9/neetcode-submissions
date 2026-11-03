class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        i = 0

        d = {}
        used = set()

        while i < len(s):
            if s[i] not in d:
                if t[i] in used:
                    return False
                d[s[i]] = t[i]
                used.add(t[i])
            else:  
                if d[s[i]] != t[i]:
                    return False

            i += 1

        return True
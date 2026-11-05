class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        e = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                e.append(i)
        if len(e) != 2:
            return False

        i = e[0]
        j = e[1]
        if s1[i] != s2[j] and s1[j] != s2[i]:
            return False

        return True

        

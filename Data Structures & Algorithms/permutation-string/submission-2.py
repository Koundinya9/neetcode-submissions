class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        charset = "".join(sorted(s1))
        l, r = 0, len(s1) - 1

        while r < len(s2):
            temp = "".join(sorted(s2[l : r + 1]))
            if temp == charset:
                return True
            r += 1
            l += 1

        return False

        
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)

        cache = {}

        def rec(i1, i2, i3):
            if i3 >= l3:
                return True

            if (i1, i2, i3) in cache:
                return cache[(i1, i2, i3)]
            cache[(i1, i2, i3)] = False
            if i1 < l1 and s1[i1] == s3[i3]:
                cache[(i1, i2, i3)] = cache[(i1, i2, i3)] or rec(i1 + 1, i2, i3 + 1)

            if i2 < l2 and s2[i2] == s3[i3]:
                cache[(i1, i2, i3)] = cache[(i1, i2, i3)] or rec(i1, i2 + 1, i3 + 1)

            

            return cache[(i1, i2, i3)]
            


        return rec(0, 0, 0)
        


        
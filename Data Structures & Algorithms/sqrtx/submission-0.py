class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x

        while l <= r:
            m = (l + r) // 2

            sq = m * m

            if sq > x:
                r = m - 1
            elif sq < x:
                l = m + 1
            else:
                return m

        return l - 1
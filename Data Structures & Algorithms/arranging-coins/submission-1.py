class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        ans = 0

        while l <= r:
            m = (l + r) // 2
            coins = m * (m + 1) // 2

            if coins > n:
                r = m - 1 
            else:
                l = m + 1
                ans = max(ans, m)
        return ans

        
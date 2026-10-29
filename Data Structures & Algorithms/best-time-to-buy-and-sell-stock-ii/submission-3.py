class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cache = {}
        
        def rec(i, buy):
            if (i, buy) in cache:
                return cache[(i, buy)]

            if i >= len(prices):
                return 0

            if not buy:
                cache[(i, buy)] = max(prices[i] + rec(i + 1, not buy), rec(i + 1, buy))

            else:
                cache[(i, buy)] = max(rec(i + 1, not buy)  - prices[i], rec(i + 1, buy))

            return cache[(i, buy)]

        return rec(0, True)
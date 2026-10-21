class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        cache = {}

        def rec(b, i):
            if i >= n:
                return 0

            if (b, i) in cache:
                return cache[(b, i)]

            if b:
                cache[(b, i)] = max(rec(not b, i + 1) - prices[i], rec(b, i + 1))
            else:
                cache[(b, i)] = max(rec(not b, i + 2) + prices[i], rec(b, i + 1))

            return cache[(b, i)]

        return rec(True, 0)
                
                  
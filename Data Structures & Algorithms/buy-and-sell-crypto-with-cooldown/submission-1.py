class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        cache = {}

        def rec(b, i):
            if i >= n:
                return 0

            if (b, i) in cache:
                return cache[(b, i)]
            
            skip = rec(b, i + 1)

            if b:
                profit = rec(not b, i + 1) - prices[i]

                cache[(b, i)] = max(profit, skip)

            else:
                profit = rec(not b, i + 2) + prices[i]

                cache[(b, i)] = max(profit, skip)
            
            return cache[(b, i)]

        return rec(True, 0)
                
                  
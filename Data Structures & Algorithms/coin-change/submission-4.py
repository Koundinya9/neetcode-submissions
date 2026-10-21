class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}

        def rec(amt, i):
            if amt == 0:
                return 0

            if i < 0 or amt < 0:
                return float('inf')

            if (i, amt) in cache:
                return cache[(i, amt)]

            
            if coins[i] > amt:
                return rec(amt, i - 1)

            cache[(i, amt)] = min(1 + rec(amt - coins[i], i), rec(amt, i - 1))
            return cache[(i, amt)]

        coins.sort()
        n = len(coins)
        ans =  rec(amount, n - 1) 

        return ans if ans != float('inf') else -1

        
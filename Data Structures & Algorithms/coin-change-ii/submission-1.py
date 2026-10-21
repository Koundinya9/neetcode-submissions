class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)

        cache = {}

        def rec(i, rem):
            if rem == 0:
                return 1

            if i < 0:
                return 0

            if (i, rem) in cache:
                return cache[(i, rem)]
            
            
            if rem >= coins[i]:
                cache[(i, rem)] = rec(i, rem - coins[i]) + rec(i - 1, rem)

            else:
                cache[(i, rem)] = rec(i - 1, rem)

            return cache[(i, rem)]

        return rec(n - 1, amount)
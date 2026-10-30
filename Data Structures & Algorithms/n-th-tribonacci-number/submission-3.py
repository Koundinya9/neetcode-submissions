class Solution:
    def tribonacci(self, n: int) -> int:

        if n <= 2:
            return 1 if n > 0 else 0

        cache = {}
        
        def rec(i):
            if i in cache:
                return cache[i]

            if i <= 2:
                cache[i] = 1 if i > 0 else 0
                return cache[i]


            cache[i] = rec(i - 1) + rec(i - 2) + rec(i - 3)
            return cache[i]

        return rec(n)

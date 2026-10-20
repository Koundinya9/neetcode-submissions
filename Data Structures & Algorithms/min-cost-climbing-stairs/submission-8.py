class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = {}
        def rec(i):
            if i >= n:
                return 0

            if i in cache:
                return cache[i]

            cache[i] = cost[i] + min(rec(i + 1), rec(i + 2))

            return cache[i]


        return min(rec(0), rec(1))
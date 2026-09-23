class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cache = [-1] * len(cost)
        def rec(i):
            if i >= len(cost):
                return 0

            if cache[i] != -1:
                return cache[i]

            cache[i] = min(cost[i] + rec(i + 1), cost[i] + rec(i + 2))
            return cache[i]

        return min(rec(0), rec(1))
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        cache = {}

        def rec(i, j):
            if i == n:
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            ans = rec(i + 1, j)

            if j == -1 or nums[j] < nums[i]:
                ans = max(ans, 1 + rec(i + 1, i))

            cache[(i, j)] = ans

            return cache[(i, j)]

        return rec(0, -1)
        
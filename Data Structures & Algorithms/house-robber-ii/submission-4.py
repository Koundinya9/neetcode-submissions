class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        cache = [[-1] * 2 for _ in range(n)]

        def rec(i, flag):
            if i >= n or (flag and i == len(nums) - 1):
                return 0

            if cache[i][flag] != -1:
                return cache[i][flag]

            cache[i][flag] = max(rec(i + 1, flag), nums[i] + rec(i + 2, flag))
            return cache[i][flag]

        return max(rec(0, True), rec(1, False))
        
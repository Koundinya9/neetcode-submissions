class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = {}
        def rec(nums):
            if len(nums) == 2:
                return 0
            
            if tuple(nums) in cache:
                return cache[tuple(nums)]

            mx = 0

            for i in range(1, len(nums) - 1):
                burst = nums[i - 1] * nums[i] * nums[i + 1]
                burst += rec(nums[:i] + nums[i + 1:])
                mx = max(mx, burst)
            cache[tuple(nums)] = mx
            return cache[tuple(nums)]

        return rec(nums)

        
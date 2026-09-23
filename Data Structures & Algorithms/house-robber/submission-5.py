class Solution:
    def rob(self, nums: List[int]) -> int:

        cache = [-1] * len(nums)
        def breh(i):
            if i >= len(nums):
                return 0

            if cache[i] != -1:
                return cache[i]

            cache[i] = max(nums[i] + breh(i + 2), breh(i + 1))
            return cache[i]
            

        return breh(0)
        
class Solution:
    def jump(self, nums: List[int]) -> int:

        cache = {}

        def rec(i):
            if i >= len(nums) - 1:
                cache[i] = 0
                return 0

            if i in cache:
                return cache[i]

            if nums[i] == 0:
                cache[i] = float('inf')
                return float('inf')

            cache[i] = float('inf')
            for j in range(1, nums[i] + 1):
                cache[i] = min(cache[i], 1 + rec(i + j))

            return cache[i]

        return rec(0)
                    

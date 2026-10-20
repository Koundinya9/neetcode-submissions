class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}
        def rec(i):
            if i >= n:
                return 0
            
            if i in cache:
                return cache[i]

            cache[i] = nums[i] + max(rec(i + 2), rec(i + 3))
            return cache[i]

        return max(rec(0) , rec(1))
        
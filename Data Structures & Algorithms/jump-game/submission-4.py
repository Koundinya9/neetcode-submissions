class Solution:
    def canJump(self, nums: List[int]) -> bool:

        cache = {}
        def rec(i):
            if i >= len(nums) - 1:
                cache[i] = True
                return True

            if i in cache:
                return cache[i]

            if nums[i] == 0:
                cache[i] = False
                return False

            cache[i] = False

            for j in range(1, nums[i] + 1):
                if rec(i + j):
                    cache[i] = True
                    return True

            cache[i] = False
            return False

        return rec(0)
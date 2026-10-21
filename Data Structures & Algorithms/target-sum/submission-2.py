class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)

        cache = {}

        def rec(i, rem):
            if i > n:
                return 0

            if (i, rem) in cache:
                return cache[(i, rem)]

            if i == n:
                if rem == 0:
                    return 1
                else:
                    return 0

            
            cache[(i, rem)] = rec(i + 1, rem + nums[i]) + rec(i + 1, rem - nums[i])
            return cache[(i, rem)]

        return rec(0, target)


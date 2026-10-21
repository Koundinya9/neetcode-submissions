class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 != 0:
            return False

        n = len(nums)

        cache = {}

        def rec(i, target):
            if i == n:
                return target == 0

            if (i, target) in cache:
                return cache[(i, target)]

            if target < 0:
                return False

            cache[(i, target)] = rec(i + 1, target) or rec(i + 1, target - nums[i])
            return cache[(i, target)]

        return rec(0, sum(nums) / 2)
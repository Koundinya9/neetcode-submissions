class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = ans = 0

        i = 0

        while i < len(nums):
            if nums[i] == 1:
                curr += 1
            if nums[i] == 0:
                ans = max(ans, curr)
                curr = 0

            i += 1
        ans = max(ans, curr)
        return ans
        
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        ans = 0
        inc = dec = 1



        i = 0

        while i < len(nums) - 1:
            if nums[i + 1] > nums[i]:
                dec = 1
                inc += 1
            elif nums[i + 1] < nums[i]:
                inc = 1
                dec += 1
            else:
                inc = dec = 1

            i += 1
            ans = max(ans, inc, dec)

        return ans
            
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ans = s = 0
        i = 0

        while i < len(nums) - 1:
            if nums[i + 1] > nums[i]:
                s += nums[i]
            else:
                ans = max(ans, s + nums[i])
                s = 0

            i += 1
            ans = max(ans, s)
        ans = max(ans, s + nums[-1])

        return ans


        
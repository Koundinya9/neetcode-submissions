class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        temp = 1

        for i in range(len(nums)):
            temp = temp * nums[i]
            prefix[i] = temp
            if temp == 0:
                temp = 1
        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            temp = temp * nums[i]
            suffix[i] = temp
            if temp == 0:
                temp = 1

        ans = float("-inf")

        for i in range(len(nums)):
            ans = max(ans, max(prefix[i], suffix[i]))

        return ans
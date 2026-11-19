class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = nums[i - 1] + prefix[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i + 1] + suffix[i + 1]

        ans = -1

        for i in range(len(nums)):
            if prefix[i] == suffix[i]:
                ans = i
                return ans
        return ans
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')

        l = 0
        s = 0

        for r in range(len(nums)):
            s += nums[r]

            while s >= target:
                ans = min(ans, r - l + 1)
                s -= nums[l]
                l += 1
                
        return ans if ans < float('inf') else 0
        
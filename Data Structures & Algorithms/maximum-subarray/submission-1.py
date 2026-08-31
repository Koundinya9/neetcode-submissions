class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        cur = nums[0]
        maxsub = 0 

        for num in nums:
            if maxsub < 0:
                maxsub = 0

            maxsub += num
            cur = max(cur, maxsub)

        return cur
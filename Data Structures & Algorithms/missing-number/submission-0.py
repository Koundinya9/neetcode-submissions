class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        mask = 0

        for i in range(len(nums) + 1):
            mask ^= i
        
        for n in nums:
            mask ^= n

        return mask
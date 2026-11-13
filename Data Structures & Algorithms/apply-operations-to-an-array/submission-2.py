class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        changed = False

        i, j = 0, 1

        while j < len(nums):
            if nums[i] == nums[j]:
                changed = True
                nums[i] = 2 * nums[i]
                nums[j] = 0

            i += 1
            j += 1

        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            

        return nums
                
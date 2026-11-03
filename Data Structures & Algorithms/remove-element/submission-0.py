class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        
        l = r = 0
        k = 0

        while r < len(nums):

            while r < len(nums) and nums[r] == val:
                r += 1
                k += 1
            
            if r < len(nums):
                nums[l] = nums[r]
            l += 1
            r += 1
        
        return len(nums) - k
                

        
        
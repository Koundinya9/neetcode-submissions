class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        l = 0
        ans = []

        while l <= len(nums) - 3:
            m = l + 1
            r = len(nums) - 1

            while m < r:
                if nums[l] + nums[m] + nums[r] < 0:
                    m += 1
                elif nums[l] + nums[m] + nums[r] > 0:
                    r -= 1
                else:
                    if [nums[l], nums[m], nums[r]] not in ans:
                        ans.append([nums[l], nums[m], nums[r]])
                    r -= 1
            l += 1
                    
        return ans



class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        ans = []

        for a in range(len(nums) - 3):
            for d in range(len(nums) - 1, a, -1):
                c = a + 1
                b = d - 1

                while c < b:
                    s = nums[a] + nums[b] + nums[c] + nums[d] 
                    if s < target:
                        c += 1
                    elif s > target:
                        b -= 1
                    else:
                        if [nums[a], nums[b], nums[c], nums[d]] not in ans:
                            ans.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        b -= 1
        return ans

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        def backtrack(path, i, sm):

            if i >= len(nums) or sm > target:
                return

            if sm == target:
                ans.append(path[:])
                return
            

            path.append(nums[i])
            backtrack(path, i, sm + nums[i])
            path.pop()
            backtrack(path, i + 1, sm)


        ans = []
        backtrack([], 0, 0)
        return ans
        
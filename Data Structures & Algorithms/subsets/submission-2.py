class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(path, i):
            if i == len(nums):
                ans.append(path[:])
                return

            path.append(nums[i])
            backtrack(path, i + 1)
            path.pop()
            backtrack(path, i + 1)


        ans = []
        backtrack([], 0)
        return ans
        
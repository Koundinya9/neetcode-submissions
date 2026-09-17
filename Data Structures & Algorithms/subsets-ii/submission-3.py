class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def backtrack(path, i):
            if i == len(nums):
                if sorted(path) not in ans:
                    ans.append(sorted(path[:]))
                return

            path.append(nums[i])
            backtrack(path, i + 1)
            path.pop()
            backtrack(path, i + 1)

        ans = []
        backtrack([], 0)
        return ans
        
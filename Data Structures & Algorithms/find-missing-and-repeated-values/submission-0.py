class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = [0] * 2

        seen = set()
        nums = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in seen:
                    ans[0] = grid[i][j]
                else:
                    seen.add(grid[i][j])

                nums.append(grid[i][j])

        for i in range(1, len(nums) + 1):
            if i not in nums:
                ans[1] = i
                

        return ans
        
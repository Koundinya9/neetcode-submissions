class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []

        nums.sort()

        for i in range(1, len(nums) + 1):
            if i not in nums:
                ans.append(i)

        return ans
        
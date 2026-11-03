class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        pref = [0] * len(nums)
        suff = [0] * len(nums)

        for i in range(1, len(nums)):
            pref[i] = pref[i - 1] + nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            suff[i] = suff[i + 1] + nums[i + 1]

        for i in range(len(nums)):
            if pref[i] == suff[i]:
                return i

        return -1
        
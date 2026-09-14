class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)
        ans = 0
        for n in s:
            c = 1
            if n - 1 not in s:
                j = n
                while j + 1 in s:
                    c += 1
                    j += 1
            print(str(n) + " " + str(c))
            ans = max(ans, c)

        return ans
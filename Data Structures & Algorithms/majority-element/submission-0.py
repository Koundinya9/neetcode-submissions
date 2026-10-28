class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        

        ans = None
        c = 0

        for n in nums:
            if c == 0:
                ans = n

            if n == ans:
                c += 1
            else:
                c -= 1

        return ans
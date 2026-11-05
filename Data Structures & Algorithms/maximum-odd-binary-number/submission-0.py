class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = 0

        for c in s:
            if c == '1':
                ones += 1

        ans = ""

        for i in range(len(s) - 1):
            if i < ones - 1:
                ans += '1'
            else:
                ans += '0'

        return ans + '1'
        
class Solution:
    def numDecodings(self, s: str) -> int:

        wo = {len(s) : 1}

        def rec(i):
            if i in wo:
                return wo[i]

            if s[i] == '0':
                return 0

            temp = rec(i + 1)

            if i < len(s) - 1:
                if s[i] == '1' or (s[i] == '2' and s[i + 1] < '7'):
                    temp += rec(i + 2)

            wo[i] = temp
            return temp

        return rec(0)





class Solution:
    def validPalindrome(self, s: str) -> bool:
        c = 0

        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                reml = s[:l] + s[l + 1:]
                remr = s[:r] + s[r + 1:]
                if reml == reml[::-1] or remr == remr[::-1]:
                    return True
                else:
                    return False
            else:
                l += 1
                r -= 1
        return True
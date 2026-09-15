class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        d = defaultdict(int)

        l = 0

        maxf = 0

        ans = 0

        for r in range(len(s)):
            d[s[r]] += 1
            maxf = max(maxf, d[s[r]])

            while (r - l + 1) - maxf > k:
                d[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
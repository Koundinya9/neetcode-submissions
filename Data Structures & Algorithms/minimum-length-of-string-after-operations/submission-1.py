class Solution:
    def minimumLength(self, s: str) -> int:
        ans = 0

        d = Counter(s)

        for k, v in d.items():
            if v >= 3:
                if v % 2 == 0:
                    ans += 2
                else:
                    ans += 1
            else:
                ans += v
        return ans

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        start = 11
        end = 13

        ans = 0

        for d in details:
            if int(d[start:end]) > 60:
                ans += 1
        return ans

        
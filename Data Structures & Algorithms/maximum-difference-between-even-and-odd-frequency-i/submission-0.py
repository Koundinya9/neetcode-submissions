class Solution:
    def maxDifference(self, s: str) -> int:
        d = Counter(s)

        mo = float('-inf')
        me = float('inf')

        for k, v in d.items():
            if v % 2 == 0:
                me = min(me, v)
            else:
                mo = max(mo, v)

        return mo - me

        
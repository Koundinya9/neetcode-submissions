class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def rec(i, level):
            if len(level) == k:
                ans.append(level[:])
                return

            if i > n:
                return

            level.append(i)
            rec(i + 1, level)
            level.pop()
            rec(i + 1, level)
            return

        ans = []
        rec(1, [])
        return ans


        
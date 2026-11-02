class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d = {}

        for i in range(1, n + 1):
            d[i] = 0

        for rel in trust:
            d[rel[1]] += 1
            d[rel[0]] -= 1


        for i in d:
            if d[i] == n - 1:
                return i
        return -1
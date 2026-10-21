class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        cache = {}

        def rec(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            if text1[i] == text2[j]:
                return 1 + rec(i + 1, j + 1)

            cache[(i, j)] = max(rec(i + 1, j), rec(i, j + 1))

            return cache[(i, j)]

        return rec(0, 0)
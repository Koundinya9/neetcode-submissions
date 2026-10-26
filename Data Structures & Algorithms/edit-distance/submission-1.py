class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        cache = {}
        def rec(i, j):
            if i >= len(word1):
                return len(word2[j:])
            if j >= len(word2):
                return len(word1[i:])

            if (i, j) in cache:
                return cache[(i, j)]

            if word1[i] == word2[j]:
                cache[(i, j)] = rec(i + 1, j + 1)
                return cache[(i, j)]
            
            cache[(i, j)] = 1 + min(rec(i + 1, j + 1), rec(i, j + 1), rec(i + 1, j))
            return cache[(i, j)]

        return rec(0, 0)
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        cache = {len(s) : True}
        def rec(i):
            if i in cache:
                return cache[i]

            for word in wordDict:
                if word == s[i : i + len(word)] and rec(i + len(word)):
                    cache[i] = True
                    return True
            cache[i] = False
            return False


            return cache[i]

        return rec(0)
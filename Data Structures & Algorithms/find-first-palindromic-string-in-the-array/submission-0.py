class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        def ispali(s):
            l, r = 0, len(s) - 1

            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        for word in words:
            if ispali(word):
                return word

        return ""

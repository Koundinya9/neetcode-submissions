class Solution:
    def reverseWords(self, s: str) -> str:
        
        ans = ""

        words = s.split(' ')

        for word in words:
            ans = ans + word[::-1] + ' '



        return ans[:len(s)]

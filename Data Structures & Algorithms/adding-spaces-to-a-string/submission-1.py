class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        j = 0
        for i in spaces:
            ans = ans + s[j:i]
            ans = ans + ' '
            j = i
        ans = ans + s[j:]
        return ans

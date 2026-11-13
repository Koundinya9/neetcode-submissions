class Solution:
    def compress(self, chars: List[str]) -> int:
        i = j = 0
        l = 0
        ans = ""

        while i < len(chars) and j < len(chars):
            while j < len(chars) and chars[i] == chars[j]:
                j += 1
            
            l = j - i
            if l == 1:
                ans = ans + chars[i]
            else:
                ans = ans + chars[i] + str(l)

            i = j

        for c in range(len(ans)):
            chars[c] = ans[c]
        
        return len(ans)
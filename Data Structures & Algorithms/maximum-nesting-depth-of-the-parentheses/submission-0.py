class Solution:
    def maxDepth(self, s: str) -> int:
        curr = ans = 0

        stack = []

        i = 0

        while i < len(s):
            if s[i] == '(':
                stack.append(s[i])
                curr += 1
                ans = max(curr, ans)
            if s[i] == ')':
                stack.pop()
                curr -= 1

            i += 1

        return ans
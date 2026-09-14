class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        stack = []

        while i < len(s):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif stack and s[i] == ']' and stack[-1] == '[':
                stack.pop()
            elif stack and s[i] == ')' and stack[-1] == '(':
                stack.pop()
            elif stack and s[i] == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
            i += 1
        return True if len(stack) == 0 else False
            
            

            
        
        
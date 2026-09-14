class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        i = 0

        while i < len(tokens):
            if tokens[i] == '+':
                first = stack.pop()
                second = stack.pop()
                stack.append(first + second)
            elif tokens[i] == '-':
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            elif tokens[i] == '*':
                first = stack.pop()
                second = stack.pop()
                stack.append(second * first)
            elif tokens[i] == '/':
                first = stack.pop()
                second = stack.pop()
                stack.append(int(float(second) / first))
            else:
                stack.append(int(tokens[i]))
            i += 1
        return stack[-1]
        
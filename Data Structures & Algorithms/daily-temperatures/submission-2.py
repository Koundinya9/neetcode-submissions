class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                topind, toptemp = stack.pop()
                result[topind] = i - topind
            stack.append((i, t))
        return result
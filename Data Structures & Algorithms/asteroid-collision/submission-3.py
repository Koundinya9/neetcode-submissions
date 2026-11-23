class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)):
            if not stack:
                stack.append(asteroids[i])
            else:
                while stack and stack[-1] > 0 and asteroids[i] < 0:
                    top = stack[-1]
                    if abs(top) == abs(asteroids[i]):
                        stack.pop()
                        break
                    elif abs(top) < abs(asteroids[i]):
                        stack.pop()                        
                    else:
                        break
                else:
                    stack.append(asteroids[i])
        return stack
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        temp = []

        for i in range(len(position)):
            temp.append([position[i], speed[i], target - position[i], (target - position[i]) / speed[i]])

        cars = sorted(temp, key = lambda x : x[2])

        stack = []

        for car in cars:
            if not stack or stack[-1] < car[3]:
                stack.append(car[3])

        return len(stack)
            

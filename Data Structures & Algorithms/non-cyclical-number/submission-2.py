class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        

        while n:
            temp = n
            n1 = 0
            while temp:
                r = temp % 10
                n1 += r * r
                temp = temp // 10

            if n1 in seen:
                return False

            if n1 == 1:
                return True
            n = n1
            seen.add(n1)

        
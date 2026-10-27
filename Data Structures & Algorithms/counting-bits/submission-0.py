class Solution:
    def countBits(self, n: int) -> List[int]:

        ans = []

        for i in range(n + 1):
            one = 0
            temp = i
            while temp:
                temp = temp & (temp - 1)
                one += 1
            ans.append(one)

        return ans
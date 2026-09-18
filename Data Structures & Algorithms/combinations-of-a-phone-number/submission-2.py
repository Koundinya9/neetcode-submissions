class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digitstonumbers = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        }

        ans = []

        if digits == "":
            return ans

        def backtrack(path, i):
            if i == len(digits):
                ans.append(''.join(path[:]))
                return

            if i > len(digits):
                return

            nums = digitstonumbers[digits[i]]

            for n in nums:
                path.append(n)
                backtrack(path, i + 1)
                path.pop()

        backtrack([], 0)
        return ans
         
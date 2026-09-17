class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(path, o, c):
            if o == n and c == n:
                ans.append(''.join(path[:]))
                return

            if c > n or o > n or c > o:
                return

            if o < n:
                path.append('(')
                backtrack(path, o + 1, c)
                path.pop()

            if c < o:
                path.append(')')
                backtrack(path, o, c + 1)
                path.pop()

        ans = []
        backtrack([], 0, 0)
        return ans
        
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def backtrack(path, l):
            if l >= len(s):
                ans.append(path[:])
                return
            
            for r in range(l, len(s)):
                if ispal(s, l, r):
                    path.append(s[l : r + 1])
                    backtrack(path, r + 1)
                    path.pop()
            


        def ispal(s, l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1

            return True
        
        ans = []
        backtrack([], 0)
        return ans
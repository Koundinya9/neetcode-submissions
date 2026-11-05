class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        i = len(heights) - 1
        tall = float('-inf')
        while i >= 0:
            if heights[i] > tall:
                tall = heights[i]
                ans.append(i)
            i -= 1
        ans.sort()
        return ans
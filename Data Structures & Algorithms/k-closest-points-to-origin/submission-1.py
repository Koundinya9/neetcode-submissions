class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        d = []

        for x, y in points:
            d.append((x ** 2 + y ** 2, x, y))

        heapq.heapify(d)

        ans = []
        while k > 0:
            point, x, y = heapq.heappop(d)
            ans.append([x, y])
            k -= 1

        return ans

        
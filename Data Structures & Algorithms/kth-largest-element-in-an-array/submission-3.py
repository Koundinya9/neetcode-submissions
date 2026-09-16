class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        temp = [-n for n in nums]

        heapq.heapify(temp)

        while k > 0:
            ans = heapq.heappop(temp)
            k -= 1
        return -ans


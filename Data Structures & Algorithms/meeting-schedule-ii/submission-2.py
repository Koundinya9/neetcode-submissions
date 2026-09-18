"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        si = sorted(intervals, key=lambda x : x.start)
        
        heap = []

        for m in si:
            if heap and heap[0] <= m.start:
                heapq.heappop(heap)

            heapq.heappush(heap, m.end)

        return len(heap)        
        
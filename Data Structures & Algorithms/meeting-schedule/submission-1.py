"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        si = sorted(intervals, key=lambda x : x.start)

        end = 0

        for m in si:
            if m.start < end:
                return False
            
            end = m.end

        return True
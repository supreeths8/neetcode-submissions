"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)

        curr_start, curr_end = intervals[0].start, intervals[0].end

        for interval in intervals[1:]:
            if interval.start < curr_end:
                return False
            curr_end = interval.end
        
        return True


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        prevEnd = -1
        for i, interval in enumerate(sorted_intervals):
            if (interval.start < prevEnd): return False
            prevEnd = interval.end
        return True
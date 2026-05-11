"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #first we must sort by start time so we get check the earliest meetings first
        intervals.sort(key = lambda x: x.start)

        for i in range(1, len(intervals)):
            int1 = intervals[i-1]
            int2 = intervals[i]
            if(int1.end > int2.start):
                return False
        return True
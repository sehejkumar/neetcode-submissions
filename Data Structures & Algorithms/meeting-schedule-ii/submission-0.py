"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for currInterval in intervals:
            #we extract the start time, and if we need or can remove a room
            time.append((currInterval.start,1))
            time.append((currInterval.end,-1))
        
        #primary sort is by time, secondary by even time so end events are processed before starts at the same time
        time.sort(key = lambda x: (x[0], x[1]))

        #res and count r 0 to start with
        res = count = 0
        #for current timestamp
        for t in time:
            #if end time for meeting, -1
            #if start time for meeting, +1
            count += t[1]
            res = max(res,count)
        return res


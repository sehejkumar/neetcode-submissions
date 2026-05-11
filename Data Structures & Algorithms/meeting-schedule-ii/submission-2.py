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
            time.append([currInterval.start,1])
            time.append([currInterval.end, -1])
        #sort by start time then by end in case times are equal
        time.sort(key = lambda x : (x[0], x[1]))
        res = 0
        cur = 0
        for t in time:
            cur+= t[1]
            res = max(res,cur)
        return res

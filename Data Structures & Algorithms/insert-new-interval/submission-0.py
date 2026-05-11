class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        resInterval = []
        for i in range(len(intervals)):
            #if the end time for new interval is less than the start time for currInterval
            if newInterval[1] < intervals[i][0]:
                resInterval.append(newInterval)
                return resInterval + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                resInterval.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        resInterval.append(newInterval)
        return resInterval
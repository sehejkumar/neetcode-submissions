class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort by start time
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        for currStart, currEnd in intervals:
            lastEnd = res[-1][1]
            if currStart<= lastEnd:
                res[-1][1] = max(currEnd,lastEnd)
            else:
                res.append([currStart,currEnd])
        return res
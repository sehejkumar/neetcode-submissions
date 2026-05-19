class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #idea is to move inward based on which bar is shorter

        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            minVal = min(heights[l], heights[r])
            currArea = minVal * (r-l)
            res = max(res,currArea)
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return res
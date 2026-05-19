class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        for i in range(n):
            first = heights[i]
            for j in range(i+1,n):
                second = heights[j]
                check = min(first,second)
                currLargest = check * (j-i)
                if currLargest >= res:
                    res = currLargest

        return res
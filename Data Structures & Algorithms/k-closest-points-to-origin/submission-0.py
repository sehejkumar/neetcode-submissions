class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #use max heap to find closes
        maxHeap = []
        for x,y in points:
            currDist = -(x**2+y**2)
            heapq.heappush(maxHeap, [currDist,x,y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        res = []
        while maxHeap:
            dist,x,y = heapq.heappop(maxHeap)
            res.append([x,y])
        return res
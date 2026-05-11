class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        
        for num in nums:
            counter[num]  = 1 + counter.get(num,0)
        
        minHeap = []
        for currNum, currCount in counter.items():
            heapq.heappush(minHeap, (currCount,currNum))
            if len(minHeap)> k:
                heapq.heappop(minHeap)
        res = []
        for i in range(k):
            count, num = heapq.heappop(minHeap)
            res.append(num)
        return res
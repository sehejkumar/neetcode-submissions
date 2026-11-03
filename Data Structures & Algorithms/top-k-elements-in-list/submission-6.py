class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elementCount = Counter(nums)

        #we want a priority queue
        minHeap = []
        for num, count in elementCount.items():
            
            heapq.heappush(minHeap, (count, num))

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        res = []

        while len(minHeap) > 0:
            count, num = heapq.heappop(minHeap)
            res.append(num)

        return res

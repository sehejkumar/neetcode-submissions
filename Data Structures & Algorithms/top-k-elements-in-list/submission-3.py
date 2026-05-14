class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #counter map
        freqMap = defaultdict(int)
        for num in nums:
            freqMap[num] += 1
        minHeap = []
        for currNum in freqMap.keys():
            heapq.heappush(minHeap, (freqMap[currNum], currNum))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return res
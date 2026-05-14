class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #counter map
        freqMap = defaultdict(int)
        for num in nums:
            freqMap[num] += 1
        #min heap
        minHeap = []
        #for each number
        for currNum in freqMap.keys():
            #push to heap in (count,num) since it sorts by key
            heapq.heappush(minHeap, (freqMap[currNum], currNum))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1]) #append the num
        return res
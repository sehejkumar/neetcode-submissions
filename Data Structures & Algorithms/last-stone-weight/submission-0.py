class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [] #define max heap as we need to pop two largest
        heapq.heapify(maxHeap)
        # add to max heap
        for currStone in (stones):
            heapq.heappush(maxHeap,-currStone)
        #we want to end with one element in max heap
        while len(maxHeap) > 1:
            #get negative cuz we stored negative of original for max heap
            firstRockVal = -heapq.heappop(maxHeap)
            secondRockVal = -heapq.heappop(maxHeap)
            if firstRockVal == secondRockVal:
                continue
            if secondRockVal < firstRockVal:
                newVal = firstRockVal - secondRockVal
                heapq.heappush(maxHeap, -newVal)

        return -maxHeap[-1] if maxHeap else 0 #return top

            
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for currNum in nums:
            heapq.heappush(minHeap, currNum)

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]


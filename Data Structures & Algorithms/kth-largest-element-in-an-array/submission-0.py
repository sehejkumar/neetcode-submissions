class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)
        kthLargest = 0;
        for i in range(k):
            kthLargest = -(heapq.heappop(maxHeap))
        return kthLargest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for num, count in counter.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            currCount, currNum = heapq.heappop(heap)
            res.append(currNum)

        return res
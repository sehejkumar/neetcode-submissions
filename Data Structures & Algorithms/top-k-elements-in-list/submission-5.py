class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for currNum in nums:
            count[currNum] += 1
        for currNum, currCount in count.items():
            freq[currCount].append(currNum)

        res=[]
        for i in range(len(freq)-1,0,-1):
            for currNum in freq[i]:
                res.append(currNum)
                if len(res) == k:
                    return res

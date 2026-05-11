class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        
        for num in nums:
            counter[num]  = 1 + counter.get(num,0)
        
        arr=[]
        for currNum, currCount in counter.items():
            arr.append([currCount, currNum])
        arr.sort()

        res=[]
        while len(res) < k:
          res.append(arr.pop()[1])
        return res
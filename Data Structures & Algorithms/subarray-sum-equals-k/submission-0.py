class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currSum = 0
        prefixSums = {0:1}
        
        for currNum in nums:
            currSum+= currNum
            diff = currSum - k
            res+= prefixSums.get(diff, 0)
            prefixSums[currSum] = 1 + prefixSums.get(currSum, 0) 

        return res

        
        
        
        
        
        
        
        
        
        
        
        # count = 0
        # for i in range(len(nums)):
        #     currSum = 0
        #     for j in range(i, len(nums)):
        #         currSum+= nums[j]
        #         if currSum == k:
        #             count+=1
        
        # return count


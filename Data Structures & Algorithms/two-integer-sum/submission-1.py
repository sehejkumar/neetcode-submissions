class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numAndIndex = {} #hashmap of num and index

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in numAndIndex:
                return [numAndIndex[difference], i]
            else:
                numAndIndex[nums[i]] = i
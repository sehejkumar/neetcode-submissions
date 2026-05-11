class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numHash = {}
        for i, currNum in enumerate(nums):
            diff = target - currNum
            if diff in numHash:
                return [numHash[diff],i]
            else:
                numHash[currNum] = i
        return [-1,-1]
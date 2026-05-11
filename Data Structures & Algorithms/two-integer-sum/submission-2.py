class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i, currNum in enumerate(nums):
            compliment = target - currNum
            if compliment in numMap:
                return [numMap[compliment], i]
            else:
                numMap[currNum] = i

        return [-1,-1]
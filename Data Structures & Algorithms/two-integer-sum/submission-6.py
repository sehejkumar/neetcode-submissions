class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenMap = {}

        for i, currNum in enumerate(nums):
            diff = target - currNum
            if diff in seenMap:
                return [seenMap[diff], i]
            else:
                seenMap[currNum] = i

        return [-1,-1]
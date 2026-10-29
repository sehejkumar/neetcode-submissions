class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i,currNum in enumerate(nums):
            complement = target - currNum
            if complement in myMap:
                return[myMap[complement], i]
            else:
                myMap[currNum] = i

        return [-1,-1]
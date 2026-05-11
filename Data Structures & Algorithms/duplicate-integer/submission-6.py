class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenSet = set()
        for currNum in nums:
            if currNum not in seenSet:
                seenSet.add(currNum)
            else:
                return True
        return False
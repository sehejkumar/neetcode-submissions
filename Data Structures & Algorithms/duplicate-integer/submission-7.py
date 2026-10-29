class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for currNum in nums:
            if currNum in seen:
                return True
            else:
                seen.add(currNum)
        return False
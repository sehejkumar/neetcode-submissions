class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # seen = []
        seen = set()
        for currNum in nums:
            if currNum not in seen:
                # seen.append(currNum)
                seen.add(currNum)
            else:
                return True
        return False

#using a list and set are both O(n)
#however, to search a list is O(n) while set is O(1)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            total_hours = 0
            mid = (l + r) // 2

            for currPile in piles:
                total_hours += math.ceil(currPile/mid)

            if total_hours > h:
                l = mid + 1
            else:
                r = mid

        return l
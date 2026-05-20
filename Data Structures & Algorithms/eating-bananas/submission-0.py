class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 #min possible time
        r = max(piles) # max time
        res = r

        while l <= r:
            k = (l + ((r-l)//2))
            time = 0
            for bananas in piles:
                time+= math.ceil(float(bananas)/k)
            if time <= h:
                res = k
                r = k-1
            else:
                l = k+1
        return res
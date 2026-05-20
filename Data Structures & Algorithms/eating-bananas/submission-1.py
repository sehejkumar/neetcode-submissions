class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 #min possible bananas per hour
        r = max(piles) # max possible bananas per hour
        res = r

        while l <= r:
            k = (l + ((r-l)//2)) #find mid point
            time = 0
            for bananas in piles: #for each banana
                #get time which is number / speed (num bananas at i / k) and round up
                time+= math.ceil(float(bananas)/k)
            if time <= h: #if we have gone under or at time
                res = k
                r = k-1 #try again going lower in number of bananas
            else:
                l = k+1 #exceeded time, need more banans per hour
        return res
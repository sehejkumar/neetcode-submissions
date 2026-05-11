class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        #need to create a list of tuples of (timstamp, user,website) and sort based on timestamp
        #to keep order of websites visited accurate
        #need to also map each website visited to the user (can use hashmap)
        patternMap = defaultdict(list)
        for (currTime, currUser, currWebsite) in sorted(zip(timestamp, username, website)):
            patternMap[currUser].append(currWebsite)
        #now that we have all websites based on user, we need to show all possible orderings
        #of three websites that are in time order
        #can use combinations
        #have a count of how many users used that pattern
        count = defaultdict(int)
        for user,website in patternMap.items():
            for currComb in set(combinations(website,3)):
                count[currComb] +=1
        maxPattern, maxCount = "",0
        for currComb, currCount in count.items():
            if currCount > maxCount or (currCount == maxCount) and currComb < maxPattern:
                maxPattern = currComb
                maxCount = currCount
        return list(maxPattern)



from collections import defaultdict
from itertools import combinations
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        '''
        Essentially, we need to line up the user, with the time, and the website
        so, we can zip them together as (t,u,w) and call sorted based on time
        then we place it into the map w keys as user and values as the sites in order
        '''
        patternMap = defaultdict(list) 
        for (currTime, currUser, currWeb) in sorted(zip(timestamp,username,website)):
            patternMap[currUser].append(currWeb)
        '''
        With all the users and websites added, we need to count the frequency of all patterns
        we store the scores (frequency based on all users) in a dict
        we will get the user and websites per user, then create multiple combinations in order and in a set
        (no dups) of the list of websites for that user
        For every combination, add to score if a user visited in increasing order
        '''
        scores = defaultdict(int) #start at count of 0
        for currUser,currWebsites in patternMap.items():
            for currComb in set(combinations(currWebsites,3)):
                scores[currComb] += 1

        #find the most frequent patter and how many
        maxPattern, maxCount = "",0
        #get a pattern and its count
        for currPattern, currCount in scores.items():
            #if greater than count or equal but lexicographically smaller
            if currCount > maxCount or (currCount == maxCount and currPattern < maxPattern):
                maxPattern = currPattern
                maxCount = currCount

        return list(maxPattern)

        
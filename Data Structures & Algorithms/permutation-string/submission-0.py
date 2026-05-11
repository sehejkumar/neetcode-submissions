class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #since we know permuation must contain exact num of chars in s1
        #use sliding window of same size over s2
        # if len(s1) > len(s2): return False
        # counts1={} #store frequency of s1 caharacters
        # for c in s1:
        #     counts1[c] = 1+ counts1.get(c,0)
        # targetLen = len(counts1) #length of s1
        # for i in range(len(s2)): #iterate through s2
        #     count2,cur = {},0 #frequency of s2 and count of curr characters
        #     for j in range(i, len(s2)):#start a new window
        #         count2[s2[j]] = 1+ count2.get(s2[j],0) #set the frequency of 
        #         if counts1.get(s2[j],0) < count2[s2[j]]: #too many of one character seen
        #             break
        #         if counts1.get(s2[j],0) == count2[s2[j]]: #exact amount seen
        #             cur+=1 #character fits permutation
        #         if cur == targetLen:
        #             return True

        # return False
        '''
        Here is the more optimal solution
        '''
        if len(s1) > len(s2):
            return False
        #two arrays set to 0 of len 26
        s1Count, s2Count = [0] * 26, [0]*26
        #set the frequency of first len(s1) characters 
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        matches = 0
        #find how many matches we have rn
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        l = 0
        #start right pointer at character after len(s1) so no double checking
        for r in range(len(s1),len(s2)):
            #valid permutations in both strings, go no further
            if matches == 26:
                return True
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches +=1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -=1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches +=1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -=1
            l+=1
        return matches == 26




    

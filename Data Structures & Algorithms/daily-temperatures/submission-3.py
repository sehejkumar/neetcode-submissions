class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #dp Solution
        #start from end and work back
        n = len(temperatures)
        res = [0] * n
        #start at second to last elem and go backwards
        for i in range(n-2,-1,-1):
            j = i+1
            while j < n and temperatures[j] <= temperatures[i]:
                #if next day can never find a warmer day, break
                if res[j] == 0:
                    j = n
                    break
                else:
                    #res[j] hold where next warmer day is
                    #jump there
                    j+=res[j]
                
            #we found a warmer day
            if j < n:
                res[i] = j-i
        return res



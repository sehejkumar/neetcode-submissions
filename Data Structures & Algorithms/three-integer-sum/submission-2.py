class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[] #result list
        nums.sort() #sort array to do 2 pointer

        for i, currNum in enumerate(nums):
            #after sorting
            #if we see positive number, all remaining numbers are positive
            if currNum > 0:
                break
                #skip duplicate numbers
            if i > 0 and currNum == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            while l < r:
                currSum = currNum + nums[l] + nums[r]
                if currSum > 0:
                    r-=1
                elif currSum < 0:
                    l+=1
                else:
                    res.append([currNum, nums[l], nums[r]])
                    l+=1
                    r-=1
                    #skip dups on left
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    #skip dups on right
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res

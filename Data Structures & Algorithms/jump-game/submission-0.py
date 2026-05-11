class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goalIndex = len(nums) - 1 # we want to eventually get to this index
        #we should work back per index and see if we can at least get to the next index 
        #start at second to last index and go backwards
        #at curr index, if the index plus the max jump length is greater than the goal index
        #we can move to goal so update goal index as curr Index
        for i in range(len(nums) - 2,-1,-1): 
            if i + nums[i] >= goalIndex:
                goalIndex = i
        return goalIndex == 0 #we can make all jumps and list is valid
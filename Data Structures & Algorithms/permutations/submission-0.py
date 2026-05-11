class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backTrack(nums,0) 
        return self.res

    def backTrack(self, nums: List[int], index: int):
        if index == len(nums):
            self.res.append(nums[:]) #append the whole permutation
            return
        else:
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                self.backTrack(nums, index+1)
                nums[index], nums[i] = nums[i], nums[index]

    
     

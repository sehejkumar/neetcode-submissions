class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[] #result
        subset=[] # current subset being built
        def dfs(i):
            if i >= len(nums): #if we made decision for every element
                res.append(subset.copy()) #add to result
                return
            subset.append(nums[i]) #choose to add to subet
            dfs(i+1) #do dfs
            subset.pop() #choose to remove that element
            dfs(i+1) #do dfs
        
        dfs(0)
        return res
            
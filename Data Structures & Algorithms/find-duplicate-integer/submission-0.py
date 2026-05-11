class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # seen set
        # looping through the array
        # if not in seen add to seen
        #else, only one number is duplicated, return that number

        #that is O(n) space
        #so what we can do is use a two pointer (slow and fast pointer)
        slow,fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break;
        return slow
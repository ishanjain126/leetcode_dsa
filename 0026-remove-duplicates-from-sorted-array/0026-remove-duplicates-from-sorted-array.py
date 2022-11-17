class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        stack = []
        i, j = 0, 1
        while i<j and j < len(nums):
            if(nums[i] == nums[j]):
                nums.pop(i)
            else:
                i += 1
                j += 1                
        return len(nums)
            
                
        
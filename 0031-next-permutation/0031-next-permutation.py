class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot_idx = None
        # Find the pivot index such that the array behaviour changes from increasing to decreasing 
        for i in range(len(nums) - 1, 0, -1):
            if nums[i-1] < nums[i]:
                pivot_idx = i-1
                break
                
        # If pivot index exists execute the below logic else simply reverse the array to get the 
        # very first permutation
        
        if pivot_idx is not None:
            # Find an array element which is greater than the element at the pivot index and swap
            for i in range(len(nums) - 1, pivot_idx, -1):
                if(nums[i] > nums[pivot_idx]):
                    nums[pivot_idx], nums[i] = nums[i], nums[pivot_idx]
                    break
            # Reverse the array after the pivot index to the end
            nums[pivot_idx+1:] = reversed(nums[pivot_idx+1:])
        else:
            nums.reverse()

                
        
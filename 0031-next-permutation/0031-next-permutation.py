class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx1 = None
        for i in range(len(nums) - 1, 0, -1):
            if nums[i-1] < nums[i]:
                idx1 = i-1
                break

        if idx1 is not None:
            for i in range(len(nums) - 1, idx1, -1):
                if(nums[i] > nums[idx1]):
                    nums[idx1], nums[i] = nums[i], nums[idx1]
                    break
            nums[idx1+1:] = reversed(nums[idx1+1:])
        else:
            nums.reverse()

                
        
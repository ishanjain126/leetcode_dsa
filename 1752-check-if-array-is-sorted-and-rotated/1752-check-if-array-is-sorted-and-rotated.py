class Solution:
    def check(self, nums: List[int]) -> bool:
        updated_nums = nums
        updated_nums.append(nums[0])
        count = 0
        for i in range(len(updated_nums) - 1):
            if updated_nums[i] <= updated_nums[i+1]:
                pass
            else:
                count += 1
            if count > 1:
                return False
        return True
        
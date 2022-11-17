class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(len(nums)-k, len(nums)):
            num = nums.pop()
            nums.insert(0, num)
        return nums
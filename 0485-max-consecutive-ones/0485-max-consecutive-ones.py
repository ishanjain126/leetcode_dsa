class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = count
        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0
            if res < count:
                res = count
        return res
        
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # get the prefix sum and then use the hashmap (dic)
        res = {}
        res[0] = 1
        count = 0
        prefix_sum = 0
        for i in nums:
            prefix_sum += i
            count += res.get(prefix_sum - k, 0)
            res[prefix_sum] = res.get(prefix_sum, 0) + 1
        print(res)
        return count
            
            
    
        
            
        
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_ele = math.inf
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_ele:
                min_ele = prices[i]
            if (prices[i] - min_ele) > max_profit:
                max_profit = prices[i] - min_ele

        return max_profit
                    
            
        
        
        
            
        
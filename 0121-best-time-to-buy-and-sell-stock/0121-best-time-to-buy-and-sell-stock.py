class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Brute force approach
        
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         temp_profit = prices[j] - prices[i]
        #         if temp_profit > 0 and max_profit < temp_profit:
        #             max_profit = temp_profit
        # return max_profit
        
        # Optimal approach
        #         i = 0
        #         j = 1
        #         max_profit = 0
        #         while j < len(prices):

        #             min_ele = prices[i]
        #             max_ele = prices[j]

        #             if min_ele > max_ele:
        #                 i = j
        #             else:
        #                 if max_ele - min_ele > max_profit:
        #                     max_profit = max_ele - min_ele

        #             j += 1

        min_ele = math.inf
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_ele:
                min_ele = prices[i]
            if (prices[i] - min_ele) > max_profit:
                max_profit = prices[i] - min_ele

        return max_profit
                    
            
        
        
        
            
        
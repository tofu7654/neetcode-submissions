class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0 
        maxp = 0

        for r in range(len(prices)):
            profit = prices[r] - prices[l]

            maxp = max(maxp, profit)

            if profit < 0:
                l = r

            r += 1
        
        return maxp

        

            
            

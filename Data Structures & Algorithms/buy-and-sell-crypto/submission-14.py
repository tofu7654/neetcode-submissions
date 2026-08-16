class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        l, r = 0, 1

        while r < len(prices):
            # is this transaction profitable?
            profit = prices[r] - prices[l]

            # update max profit
            if profit > maxp:
                maxp = profit

            # move window over if not
            if profit < 0:
                l = r
            # move right pointer to right
            r += 1
        
        return maxp


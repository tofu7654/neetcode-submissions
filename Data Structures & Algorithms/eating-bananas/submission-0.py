class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # 1 -> biggest pile GOTCHA
        res = r # because this is the starting point

        while l <= r:
            # find the middle
            k = (l + r) // 2

            hours = 0
            # eat each pile and count up the hours
            for pile in piles:
                hours += math.ceil(pile / k) 

            # if we finished the piles quicker, update res
            if hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res



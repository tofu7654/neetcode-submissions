class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = max(piles)

        while l <= r: # if we only have one pile 
            m = (l + r) // 2

            hours = 0
            for p in piles:
                # see how many hours it takes for each pile
                hours += math.ceil(p / m)

            if hours <= h:
                k = m
                r = m - 1
            else:
                l = m + 1
        
        return k


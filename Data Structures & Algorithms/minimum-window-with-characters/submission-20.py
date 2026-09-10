class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqW, freqT = {}, {}
        l = 0
        lengthShortest, shortest = float("infinity"), [-1, -1]

        # edge case where T is empty 
        
        # build freq map of T
        for c in t:
            freqT[c] = freqT.get(c, 0) + 1

        have = 0
        need = len(freqT)
        for r in range(len(s)):
            c = s[r]
            freqW[c] = freqW.get(c, 0) + 1

            if c in freqT:
                # check if condition is met
                if freqW[c] == freqT[c]:
                    have += 1
            
            # if have == need, make invalid
            while have == need:
                if r - l + 1 < lengthShortest:
                    shortest = [l, r]
                    lengthShortest = r - l + 1
                
                # make window invalid
                freqW[s[l]] -= 1
                if s[l] in freqT and freqW[s[l]] < freqT[s[l]]:
                    have -= 1
                
                l += 1
            
        l, r = shortest
        return s[l:r + 1] if lengthShortest != float("infinity") else ""



        
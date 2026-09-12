class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqW, freqT = {}, {}
        l = 0
        shortestLength, shortest = float("infinity"), [-1, -1]

        # build freq of T hashmap
        for c in t:
            freqT[c] = freqT.get(c, 0) + 1

        need = len(freqT)
        have = 0
        for r in range(len(s)):
            c = s[r]
            # add char to freq of window
            freqW[c] = freqW.get(c, 0) + 1

            # if this character is necessary a
            if c in freqT:
                if freqW[c] == freqT[c]:
                    have += 1

            while have == need:
                # check shortest and update if necessary
                if r - l + 1 < shortestLength:
                    shortestLength = r - l + 1
                    shortest = [l, r]

                # make the window invalid
                freqW[s[l]] -= 1
                # check if the criteria is not met anymore
                if s[l] in freqT and freqW[s[l]] < freqT[s[l]]:
                    have -= 1
                
                l += 1

        l, r = shortest
        return s[l:r + 1] if shortestLength != float("infinity") else ""
            

                


                
            

            




        


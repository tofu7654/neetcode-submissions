class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        l = 0
        res = 0

        for r in range(len(s)):
            
            # add the r char to the freq
            freq[ord(s[r]) - ord('A')] += 1

            # if we are out of replacements
            while ((r - l + 1) - (max(freq)) > k):

                # move the left pointer until we have enough replacements again
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            res = max(r - l + 1, res)
        
        return res


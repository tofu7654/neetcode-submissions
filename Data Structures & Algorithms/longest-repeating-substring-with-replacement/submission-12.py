class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        l = 0
        res = 0
        length = 0

        for r in range(len(s)):
            
            # add the r char to the freq
            freq[ord(s[r]) - ord('A')] += 1
            length += 1

            # if we are out of replacements
            while (length - (max(freq)) > k):

                # move the 
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
                length -= 1
            
            length = r - l + 1
            res = max(length, res)
        
        return res


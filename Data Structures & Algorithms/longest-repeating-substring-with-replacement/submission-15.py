class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, longest = 0, 0

        for r in range(len(s)):
            
            # count frequency of this character
            count[s[r]] = count.get(s[r], 0) + 1

            # if window - max freq > k 
            while (r - l + 1) - (max(count.values())) > k:
                count[s[l]] -= 1
                l += 1
            
            longest = max(r - l + 1, longest)

        return longest






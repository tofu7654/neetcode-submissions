class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l, longest = 0, 0

        for r in range(len(s)):

            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            
            charset.add(s[r])
            longest = max(r - l + 1, longest)
        
        return longest

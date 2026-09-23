class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        l, longest = 0,0

        for r in range(len(s)):
            c = s[r]
            while c in hashSet:
                hashSet.remove(s[l])
                l += 1
            
            hashSet.add(c)
            longest = max(longest, r - l + 1)
        
        return longest


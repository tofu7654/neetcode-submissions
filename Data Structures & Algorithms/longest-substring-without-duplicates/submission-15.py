class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        numSet = set()
        l = 0
        longest = 0

        for r in range(len(s)):
            
            while s[r] in numSet:
                numSet.remove(s[l])
                l += 1

            numSet.add(s[r])

            longest = max(r - l + 1, longest)

        return longest





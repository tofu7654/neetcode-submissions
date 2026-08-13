class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        longest = 0

        for n in numSet:
            length = 0
            if (n - 1) in numSet:
                continue
            length += 1
            while n + length in numSet:
                length += 1
            if length > longest:
                longest = length
        
        return longest
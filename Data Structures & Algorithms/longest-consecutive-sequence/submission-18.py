class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        longest = 0

        # start from beginning
        for i in range(len(nums)):
            count = 0 

            # start counting if it is the beginning of the sequence
            if nums[i] - 1 not in numSet:
                count += 1
                
                counter = 1
                # if we found the beginning, we check if there is another
                while nums[i] + counter in numSet:
                    count += 1
                    counter += 1

                if count > longest:
                    longest = count

        return longest



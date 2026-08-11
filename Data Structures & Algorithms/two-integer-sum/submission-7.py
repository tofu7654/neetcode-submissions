class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict1 = {}

        for i, n in enumerate(nums):

            search = target - n

            if search in dict1:
                return [dict1[search], i]

            dict1[n] = i
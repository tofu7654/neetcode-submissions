class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            search = target - n
            if search in prevMap:
                return [prevMap[search], i]
            prevMap[n] = i
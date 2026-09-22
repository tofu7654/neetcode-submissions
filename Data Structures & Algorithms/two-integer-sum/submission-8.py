class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, n in enumerate(nums):
            search = target - n
            if search in hashMap:
                return [hashMap[search], i]
            else:
                hashMap[n] = i
        return
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = len(nums) - 1
        res = []
        nums = sorted(nums)

        for a in range(len(nums)):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            l = a + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[a] + nums[l] + nums[r]

                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    res.append([nums[a], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    r -= 1
        
        return res

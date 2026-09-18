class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[l]

        while l <= r:
            # first check if this array is sorted
            if nums[r] > nums[l]:
                res = min(nums[l], res)
                break
            
            # otherwise run search
            m = (l + r) // 2
            res = min(nums[m], res)

            if nums[m] < nums[l]:
                r = m - 1
            elif nums[m] >= nums[l]:
                l = m + 1
        
        return res





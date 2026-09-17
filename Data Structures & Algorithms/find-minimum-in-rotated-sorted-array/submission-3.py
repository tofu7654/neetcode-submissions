class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0] 

        while l <= r: 
            # if this array is sorted already
            if nums[r] > nums[l]:
                res = min(nums[l], res)
                break

            m = (l + r) // 2

            # check against result
            res = min(nums[m], res)

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return res
            

            

            
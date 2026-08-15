class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l ,r = 0, len(heights) - 1

        res = 0

        while l < r:
            width = r - l
            height = min(heights[r], heights[l])
            area = width * height
            res = max(res, area)

            # move the pointer with the smallest height
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            
        return res

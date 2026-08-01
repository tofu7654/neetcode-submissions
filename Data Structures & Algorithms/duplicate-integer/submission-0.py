class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        book = set()
        for num in nums:
            if num in book:
                return True
            book.add(num)
        return False

        